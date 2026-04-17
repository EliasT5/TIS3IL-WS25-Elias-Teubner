# Assignment 2: M5 Data Preparation

For the first part of the project, I had to get the data from the M5 Competition. You can find everything in the official repo:

- **GitHub:** [Mcompetitions/M5-methods](https://github.com/Mcompetitions/M5-methods)
- **Data Drive:** [Google Drive Link](https://drive.google.com/drive/folders/1D6EWdVSaOtrP1LEFh1REjI3vej6iUS_4?usp=sharing)

## My Decisions

One of the first things I had to decide was whether to put the raw data in the Git repo. I decided **not** to version the CSV or Parquet files. They are several gigabytes in size, and since anyone can just download them from the link above, it felt like a waste of space and would make the repo very slow to clone. I've added `data/raw/` and `data/processed/` to my `.gitignore`.

I also decided to convert all the raw CSV files into **Parquet format**. Parquet is much more efficient for reading into Pandas/Polars, which saves a lot of time in the later assignments.

## Understanding the Data

I looked at the four main files provided:

1.  **`calendar.csv`**: This maps the day IDs (like `d_1`) to actual dates. It also has info about events (like Christmas) and SNAP flags.
2.  **`sell_prices.csv`**: Shows the price of each item in different stores for each week.
3.  **`sales_train_validation.csv`**: The main sales data. It's in a "wide" format where each day is a column.
4.  **`sales_train_evaluation.csv`**: Same as validation but with more days for the final testing.

## Running the code

The conversion logic is implemented in the notebook `Exercise2/prepare_m5_data.ipynb`. Go to the notebook and run all cells to generate the Parquet files and schema summary.

The notebook also saves a schema summary to `data/processed/exercise2_data_summary.json` so I can easily check the column types later.
