# TIS3IL Course Project: M5 Forecasting
**Elias Teubner (Winter Semester 2025)**

This repository contains all my work for the **TIS3IL** course. The project is focused on the **M5 Competition dataset**, which contains sales data from Walmart. Throughout the semester, I've built a full data pipeline—from raw data preparation and database management to building advanced forecasting models.

## Project Structure

The project is organized into several assignments:

- **Exercise 2:** Data Prep (CSV to Parquet).
- **Exercise 3:** Database IO (PostgreSQL & ADBC).
- **Exercise 4:** Revenue Analysis (Data transformations and stats).
- **Exercise 5:** Monthly Forecasting (Baseline vs AutoARIMA).
- **Exercise 6:** ML & Neural Forecasts (Random Forest & Fallbacks).
- **Exercise 7:** Hierarchical Forecasts (Top, Middle, and Bottom levels).

## Getting Started

If you want to run my code, you'll need the M5 data first.

1.  **Download the data:** Get the CSV files from the [M5 GitHub](https://github.com/Mcompetitions/M5-methods) and put them in `data/raw/`.
2.  **Environment:** I'm using `uv`. Run `uv sync` to install everything.
3.  **Run the notebooks:** Each exercise has its own notebook. You can open them and run all cells in order.
- **Documentation:** I've used MkDocs for the final report. Run `uv run mkdocs build`.


## Prerequisites

- Python 3.12+ (managed by `uv`).
- PostgreSQL (required for Exercise 3 and 4).
- A `.env` file for database credentials (see `.env.example`).

---
*This repository is for educational purposes as part of the TIS3IL course.*
