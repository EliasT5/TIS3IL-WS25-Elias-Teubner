# Assignment 3: Database Setup & IO

In this assignment, I had to move the M5 data from Parquet files into a **PostgreSQL** database. This is a common step in real-world projects where you want to have a central place for your data that multiple people or tools can access.

## Setting up PostgreSQL

I'm using a local PostgreSQL instance. To keep things clean, I created a `.env` file for my credentials (user, password, etc.). I also decided to put all my M5 tables into a specific **schema** called `m5`. 

**Why a schema?** 
I think it's better than just putting everything in the `public` schema because it keeps the project tables organized and separate from anything else I might have in my database.

## Loading the Data

I tried two different ways to write the data to the database:
1.  **Pandas `to_sql`:** This is the classic way using `SQLAlchemy` and the `psycopg` driver. It's very easy to use but can be slow for large tables.
2.  **Polars `write_database`:** I've been using Polars a lot in this course, and its database writer is really fast, especially when combined with ADBC.

## What I learned

Loading millions of rows (like in the `sell_prices` table) takes some time. I found that the choice of driver and the way you batch the inserts makes a huge difference. For the next assignment, I'll definitely stick with the faster Polars/ADBC combo.

To see my timing results and the implementation of both Pandas and Polars loaders, please go to the notebook `Exercise3/load_postgres.ipynb`.
