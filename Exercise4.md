Transform and filter (positive sales) the sales data into long form as described in the lecture.
Hints: First Join the train & test dataframes, then replace the string day index column names with dates, then use the function unpivot in polars or melt in pandas to bring the data frame to longform. To filter the dataframe you can use filter in polars https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.filter.html
Most of the code is in the slides of lecture 2.​

Use arrow database connectivity https://carrow.apache.org/adbc/current/python/quickstart.html to insert the data into the database. 
Hint: Use polars write_database but with engine="adbc",  see the slides. ​

Join the 3 tables so that the resulting sales table includes the sales price of the item (how do you join?). Decide if you want to perform the join in memory (polars, pandas) or in database (SQL). Decide which fields from the other tables you want to include in your final sales table.
Hint: polars has the function join which you can use to join the dataframes 
https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.join.html​
You need to find the common Fields in the dataframes and make sure that the same field in different table also has the same datatype.  
An example of join is in the Lecture slides. Start from the long form filtered sales df. 
The resulting df should have the value of price in each row. 

Calculate a new field revenue for the sales table (or df). Hint: multiply the sales and the price. In polars you can use the function with_columns to add a new column to a dataframe. https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.with_columns.html  ​

Calculate the following summary statistics:​

                             1. Total revenue, total revenue per year, total revenue per year and store. 
Hint: Total revenue is the sum of the revenue column. For revenue per year you have to group by year and sum, etc. ​

                             2. Total, mean, median, min, max revenue per store and year (correction from lecture notes). 
Which of these variables would change if you would use the unfiltered sales table (including zero sales days)?
Hint: Group by Store and Year. Compute the variables in the aggregation. First with the unfiltered sales table (in long form) and then with the filtered one. Compare the resulting dataframes.   ​

                             3. Total, mean, median, min, max revenue and sales per category. ​

                             4. Which item at which day has the most sales? Which item at which day makes the most revenue?
HINT: Use the arg_max function​ on the corresponding fields.

Document the results in mkdocs. Visualise the time series results (e.g. revenue per month) with matplotlib, seaborn or the python vis library of your choice.

Use the browser to Print the MKDocs Page of the assignment to a pdf and submit the pdf. 
Aditionaly you can submit your jupyter notebook or python script to the asignment. 
These should also be commited in your repo. 

Bonus: Install pytest and write a test function checks if the sum of sales and revenue of your sales long table equals the sum of the total sales and revenue of 5.3 (per category)