# Assignment 6: Machine Learning & Neural Forecasts

In this assignment, I moved beyond simple statistical models and tried using **Machine Learning** (Random Forest) and looked into **Neural Networks**.

## Random Forest (The winner!)

I built a Random Forest model using `scikit-learn`. To make it work for time series, I had to create some features:
- **Lags:** Using sales from 1, 2, 3, and 12 months ago.
- **Rolling Mean:** The average of the last 3 months.
- **Calendar:** The month of the year.

The results were great! On the test set, the Random Forest reached an **MAE of 38,715**, which is even better than the AutoARIMA from the previous assignment. It seems like adding the specific month as a feature really helped the model understand the seasonality.

## The "Neural" Struggle

I really wanted to try out `neuralforecast` (which has models like N-BEATS and NHITS), but I ran into a lot of issues on my Windows machine. Installing PyTorch and Ray can be a bit of a nightmare with version conflicts. 

Because of this, I implemented a **fallback** in my notebook. If the neural library isn't available, it just uses the Seasonal Naive baseline so that the rest of the code doesn't crash. If I ever move this project to a Linux server, I'll definitely try to get the real neural models running!

## Visualizing Performance

I created a scatter plot of MAE vs R2 for all the models. You can see that Random Forest (ML) is in the top-performing corner:

![Best Models](assets/exercise6_total_best_models.png)

To check out the Random Forest implementation and the neural network fallback logic, go to the notebook `Exercise6/advanced_forecasts.ipynb`.
