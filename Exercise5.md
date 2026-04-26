Load the M5 long sales data from the previous assignments.  

Add a month first field.  

Aggregate on month and dept id and optionally rename the columns to fit the nixtla api.   

Split your data in, train, validation and test. Use CV in Time. 
Prediction horizon are the next 12 months. The test set are the last 12 months. 

Implement at least one baseline and one statistical forecast model. Ideally, you implement all the models from Lecture 4 and 5 (Baseline and statistical). You can implement these models in numpy as functions or classes, or by using one of the forecasting libraries:  

               statsmodels: https://www.statsmodels.org/dev/examples/index.html#time-series-analysis 

               Nixtla: https://nixtlaverse.nixtla.io/statsforecast/index.html  

               Sktime: https://www.sktime.net/en/stable/api_reference/regression.html 

Measure the error of your forecast with MAE, RMSE, Mape, OPE, and R2 

Provide a results table with columns: Model Name, Implementation (e.g. Numpy, nixtla version), Split (Val, Test), and 1 column per error metric. RMSE and OPE will be introduced in Lecture 5.  
Also make 1 Chart per Time Series, displaying the True data, at least one baseline and at least one statistical model.  

Commit your code to your github repo in a Subfolder Assignment 5.  

Submit a pdf or screenshot, showing your result table and the visualizations.  