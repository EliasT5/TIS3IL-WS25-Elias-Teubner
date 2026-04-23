# Assignment 4: Revenue Analysis & Database IO

This was one of the most challenging but interesting assignments. I had to transform the "wide" M5 data into a "long" format, join it with other tables, and then move it into a PostgreSQL database.

## The Transformation Process

I followed the steps from the lecture:
1.  **Melting:** I transformed the sales data so that instead of each day being a column, there is a `d` column and a `sales` column.
2.  **Filtering:** I filtered for rows where `sales > 0`. This significantly reduced the number of rows I had to work with in memory.
3.  **Joining:** I joined the sales table with the `calendar` (to get dates and years) and `sell_prices` (to get the price of each item).
4.  **Revenue:** I calculated a new column `revenue = sales * sell_price`.

I decided to do the join in **Polars** because it's much faster than doing it in the database after insertion, especially with millions of rows.

## Database Insertion

I used **ADBC (Arrow Database Connectivity)** to insert the data into my local PostgreSQL. It's surprisingly fast! I used `polars.write_database` with `engine="adbc"`. 

## Summary Statistics

Here are some of the interesting things I found in the data:

### 1. Revenue by Year
The total revenue has been growing steadily until 2016 (note that 2016 only has partial data):

| Year | Total Revenue |
| :--- | :--- |
| 2011 | $23,891,336 |
| 2012 | $32,649,200 |
| 2013 | $35,923,373 |
| 2014 | $37,861,913 |
| 2015 | $42,416,456 |
| 2016 | $14,934,289 |

### 2. The Effect of Zero-Sales Days
The assignment asked what would change if I used the unfiltered sales table (including days with 0 sales). 

For **Store CA_1 in 2011**:
- **Filtered (sales > 0):** Mean Revenue was **$11.12**, Median was **$6.97**.
- **Unfiltered:** Mean Revenue dropped to **$2.84**, and Median became **$0.00**.

Total revenue doesn't change because `0 * price` is still 0, but the averages change a lot because of all the zeros in the denominator!

### 3. Category Insights
FOODS is by far the biggest category in terms of revenue:

| Category | Total Revenue | Max Revenue (One item/day) |
| :--- | :--- | :--- |
| **FOODS** | $108.9M | $2,164.32 |
| **HOBBIES** | $22.8M | $1,618.38 |
| **HOUSEHOLD** | $55.9M | $1,766.94 |

### 4. Top Performers
- **Most Sales:** Item `FOODS_3_090` at store `CA_3` on 2013-09-14 had **763 sales**!
- **Most Revenue:** Item `FOODS_3_785` at store `CA_1` on 2012-06-22 made **$2,164.32** in a single day.

## Visualization

I plotted the total monthly revenue to see the trend:

![Monthly Revenue](assets/exercise4_monthly_revenue.png)

## Bonus Task
I also implemented a test using `pytest` to make sure my data transformations were correct. The test checks if the sum of revenue in the long table matches the sum when grouped by category. You can run it with `uv run pytest`.
