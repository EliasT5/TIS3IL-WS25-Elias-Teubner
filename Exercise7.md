 For the M5 competition data make revenue forecasts for the year 2015 at the following levels: 

Total Revenue (“Top level”)  

Department ID and State (“Middle level”) 

Item and Store (“Bottom level”) 

For all 3 levels, the forecasts should be monthly (12 values per level id). The variable to forecast is the revenue. 

Submit one table of your metrics which includes the columns:  

Model: the name of your model. Here you can include also the library or implementation (eg. ARIMA-nixtla, ARIMA-statsmodels or ARIMA-custom if you code it yourself).  

Split (“Test” is required but you can include “Validation”) 

Level (“Top”, “Middle”, “Bottom”), F and one Column per metric.  

Feature Set: A descriptive string of the type of features you used. E.g. “Lag”, “Lag+statistical”,”Lag+statistical+holidays”, etc. 

Metric: One column per metric as in the previous assignments (MAE, MAPE, ...) 

 

Feature engineering: For all levels you can add features to the lag values. Use the methods shown in Lectures 8&9. Check which features sets to improve models which only use lag values.  

For the bottom level (item_id and store) it is highly recommended to use the approach shown in Lecture 9 (e.g. build up the dataset and the feature sets) instead of relying to nixtla to avoid crashes due to large amount of data.  

Also, you can incorporate feature selection methods as shown in Lecture 9.  

Consolidation.  In Lecture 9 we will discuss forecast consolidation and hierarchical forecasting. This is not necessary for the assignment. Hence, your forecasts at each level may be from different models.  
You are free to use these methods to improve your forecasts. Of course, you can aggregate your Bottom or Middle forecasts to top level to check if they are better than the direct forecasts at this level.  

Requirements.  

The minimum requirement of the assignment is to have all 3 levels, at least 1 model per family (Baseline, statistical, ML, Neural) and at least 2 Feature Sets (e.g. “Lag”, “Lag+X”). 

Visualization.  

Time Series  

Like in the precious Assignment, visualize the time true time series and that of the best model per family for the top level and for the aggregated values and predictions of the middle and bottom levels. In total, you should have 3 Time Series plots.  

Scatter Plots  

Make 1 Scatter plot per level, where the x axis is the predicted values of your best overall model for this level and the y the true values. In total, you should have 3 Scatter plots.  

Submission

Please submit your Metrics Table, the Plots and a link to your github commit. 