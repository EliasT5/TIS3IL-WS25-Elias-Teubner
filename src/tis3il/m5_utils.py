from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"
DOC_ASSETS = ROOT / "docs" / "assets"


@dataclass(frozen=True)
class M5Paths:
    calendar: Path = PROCESSED / "calendar.parquet"
    prices: Path = PROCESSED / "sell_prices.parquet"
    sales_train: Path = PROCESSED / "sales_train_validation.parquet"
    sales_test: Path = PROCESSED / "sales_test_evaluation.parquet"
    sales_long: Path = PROCESSED / "sales_long.parquet"
    sales_enriched: Path = PROCESSED / "sales_enriched.parquet"
    dept_monthly: Path = PROCESSED / "dept_monthly_revenue.parquet"


PATHS = M5Paths()


def ensure_dirs() -> None:
    for path in (RAW, PROCESSED, DOC_ASSETS):
        path.mkdir(parents=True, exist_ok=True)


def require_file(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(
            f"Required file not found: {path}. Put the M5 data in data/raw/ "
            "or run the earlier assignment script first."
        )
    return path


def find_raw_csv(name: str) -> Path:
    exact = RAW / name
    if exact.exists():
        return exact
    matches = sorted(RAW.rglob(name))
    if matches:
        return matches[0]
    raise FileNotFoundError(f"Could not find {name} under {RAW}")


def day_columns(df: pd.DataFrame) -> list[str]:
    return [column for column in df.columns if column.startswith("d_")]


def load_parquet(path: Path) -> pd.DataFrame:
    return pd.read_parquet(require_file(path))


def make_sales_long(include_zero_sales: bool = False) -> pd.DataFrame:
    sales = load_parquet(PATHS.sales_train)
    calendar = load_parquet(PATHS.calendar)
    value_vars = day_columns(sales)
    id_vars = [column for column in sales.columns if column not in value_vars]
    long_df = sales.melt(id_vars=id_vars, value_vars=value_vars, var_name="d", value_name="sales")
    long_df = long_df.merge(calendar[["d", "date", "wm_yr_wk", "month", "year"]], on="d", how="left")
    if not include_zero_sales:
        long_df = long_df[long_df["sales"] > 0]
    return long_df


def enrich_sales(long_df: pd.DataFrame) -> pd.DataFrame:
    prices = load_parquet(PATHS.prices)
    calendar = load_parquet(PATHS.calendar)
    cal_features = calendar[
        [
            "date",
            "d",
            "wm_yr_wk",
            "weekday",
            "month",
            "year",
            "event_name_1",
            "event_type_1",
            "snap_CA",
            "snap_TX",
            "snap_WI",
        ]
    ].drop_duplicates("d")
    drop_cols = [c for c in ["date", "wm_yr_wk", "month", "year"] if c in long_df.columns]
    df = long_df.drop(columns=drop_cols)
    df = df.merge(cal_features, on="d", how="left")
    df = df.merge(prices, on=["store_id", "item_id", "wm_yr_wk"], how="left")
    df["sell_price"] = df["sell_price"].fillna(0.0)
    df["revenue"] = df["sales"] * df["sell_price"]
    df["date"] = pd.to_datetime(df["date"])
    return df


def monthly_department_revenue(sales: pd.DataFrame | None = None) -> pd.DataFrame:
    df = load_parquet(PATHS.sales_enriched) if sales is None else sales.copy()
    df["month_first"] = pd.to_datetime(df["date"]).dt.to_period("M").dt.to_timestamp()
    monthly = (
        df.groupby(["dept_id", "month_first"], as_index=False)
        .agg(revenue=("revenue", "sum"), sales=("sales", "sum"))
        .sort_values(["dept_id", "month_first"])
    )
    return monthly.rename(columns={"dept_id": "unique_id", "month_first": "ds", "revenue": "y"})


def split_last_periods(df: pd.DataFrame, h: int = 12, val_h: int = 12) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_parts: list[pd.DataFrame] = []
    val_parts: list[pd.DataFrame] = []
    test_parts: list[pd.DataFrame] = []
    for _, group in df.sort_values("ds").groupby("unique_id", sort=False):
        if len(group) < h + val_h + 3:
            continue
        train_parts.append(group.iloc[: -(h + val_h)])
        val_parts.append(group.iloc[-(h + val_h) : -h])
        test_parts.append(group.iloc[-h:])
    if not train_parts:
        raise ValueError("Not enough observations per series for the requested split.")
    return pd.concat(train_parts), pd.concat(val_parts), pd.concat(test_parts)


def metrics(y_true: pd.Series | np.ndarray, y_pred: pd.Series | np.ndarray) -> dict[str, float]:
    true = np.asarray(y_true, dtype=float)
    pred = np.asarray(y_pred, dtype=float)
    err = true - pred
    mae = float(np.mean(np.abs(err)))
    rmse = float(np.sqrt(np.mean(err**2)))
    denom = np.where(true == 0, np.nan, true)
    mape = float(np.nanmean(np.abs(err / denom)) * 100)
    ope = float(np.sum(pred - true) / np.sum(true)) if np.sum(true) else np.nan
    ss_res = float(np.sum(err**2))
    ss_tot = float(np.sum((true - np.mean(true)) ** 2))
    r2 = 1 - ss_res / ss_tot if ss_tot else np.nan
    return {"MAE": mae, "RMSE": rmse, "MAPE": mape, "OPE": ope, "R2": float(r2)}


def seasonal_naive(train: pd.DataFrame, future: pd.DataFrame, season_length: int = 12) -> pd.DataFrame:
    out: list[pd.DataFrame] = []
    for uid, hist in train.sort_values("ds").groupby("unique_id", sort=False):
        horizon = future[future["unique_id"] == uid].copy()
        pattern = hist["y"].tail(season_length).to_numpy()
        if len(pattern) == 0 or horizon.empty:
            continue
        horizon["y_pred"] = np.resize(pattern, len(horizon))
        out.append(horizon)
    return pd.concat(out, ignore_index=True)


def lag_feature_frame(df: pd.DataFrame, lags: tuple[int, ...] = (1, 2, 3, 12)) -> pd.DataFrame:
    out = df.sort_values(["unique_id", "ds"]).copy()
    out["month"] = pd.to_datetime(out["ds"]).dt.month
    for lag in lags:
        out[f"lag_{lag}"] = out.groupby("unique_id")["y"].shift(lag)
    shifted = out.groupby("unique_id")["y"].shift(1)
    out["rolling_mean_3"] = shifted.groupby(out["unique_id"]).rolling(3).mean().reset_index(level=0, drop=True)
    return out.dropna().reset_index(drop=True)
