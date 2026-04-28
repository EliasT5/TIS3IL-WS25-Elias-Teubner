Reuse the data from Assignment 5. Make sure that your data contains the revenue of the Walmart departments. This is your target variable.  

Make predictions of the monthly revenue per department id. Split in train, val and test.  

Use both ML models (introduced in lecture 6) and deep learning models (which will be introduced in lecture 7).   

Compare your results with the previous results of baseline and statistical models. 

Visualize the performance of the models in three ways: 

By making a Time Series plot of the total revenue (the sum of the revenues of the 7 departments) and adding the validation and test predictions of your models. Please add only the best model of each family in terms of MAE (baseline, statistical, ml, neural).  

A scatter plot of MAE vs R2 where each point is a model. Use the same color for models of the same family (statistical, ML, etc.) 

Use  nixtla mlforecast  https://nixtlaverse.nixtla.io/mlforecast/index.html for ML models (and scikit-learn for the individual regressor) 

and neural forecast https://nixtlaverse.nixtla.io/neuralforecast/docs/getting-started/introduction.html  and for Deep Learning models.  

For both cases, review the documentation and think about which parameters you will configure explicitly.  

Some models have a parameter input_size which is set to 24 in the examples of the documentation.  This can cause errors if the model does not have enough data to train. It can be resolved by reducing the input size.  

If you have trouble installing neuralforecast on windows here are possible solutions: 

Install dependencies (ray, pydantic) separately.  

Install in a specific conda enviroment.  

Install the library on windows subsystem for linux (wsl)  

Install the library inside a docker container. Development containers in VSCode are a simple way to get started https://code.visualstudio.com/docs/devcontainers/containers 