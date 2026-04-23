from __future__ import annotations

import pandas as pd


def test_category_sales_and_revenue_sums_match_total() -> None:
    sales = pd.DataFrame(
        {
            "cat_id": ["A", "A", "B"],
            "sales": [2, 3, 5],
            "sell_price": [10.0, 20.0, 4.0],
        }
    )
    sales["revenue"] = sales["sales"] * sales["sell_price"]
    category = sales.groupby("cat_id", as_index=False).agg(total_sales=("sales", "sum"), total_revenue=("revenue", "sum"))
    assert category["total_sales"].sum() == sales["sales"].sum()
    assert category["total_revenue"].sum() == sales["revenue"].sum()
