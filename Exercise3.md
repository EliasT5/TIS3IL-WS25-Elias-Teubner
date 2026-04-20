Install Postgres and pgadmin on your laptop, create a user and password and a Database tsdb ​

Put these redentials in the .env file in your repo​

Install sqlalchemy and psycopg2 (or 3) ​

Create a connection to tsdb with sqlalchemy​

Read the M5 parquet files from A2 with pandas. Save them in the Database.
Think if you should transform any of the dataframes before saving. Think about how to name your tables.
Postgres offers a feature called schemas. Read the docs about it an think if it wise to use it for out work.
Time the io task. ​

Repeat Step e. but this time with polars. Time the results ​

Summarize your io experiments in the documentation. What is the fastest way to input the data? 

Use PGAdmin to ​inspect the tables.  

Commit, merge, push. 