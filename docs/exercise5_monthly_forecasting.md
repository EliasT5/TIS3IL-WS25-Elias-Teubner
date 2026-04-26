# Assignment 5: Monthly Forecasting

Now we're getting to the fun part: predicting the future! For this assignment, I focused on forecasting the **monthly revenue** for each department.

## Setup

I split the data into three parts:
- **Training:** Everything before the last two years.
- **Validation:** The second-to-last 12 months (used to tune things).
- **Test:** The very last 12 months (to see how well the models actually work).

## The Models

I tested two main approaches:
1.  **Seasonal Naive:** This is my baseline. It just predicts that next year's January will be the same as this year's January. It's simple but often hard to beat!
2.  **AutoARIMA:** A more sophisticated statistical model that tries to find trends and patterns automatically. I used the `statsforecast` library for this.

## Results & My Thoughts

I was surprised by the results. On the **Test set**, AutoARIMA actually performed better than my baseline:

| Model | MAE (Lower is better) | R2 (Higher is better) |
| :--- | :--- | :--- |
| **Seasonal Naive** | 66,986 | 0.948 |
| **AutoARIMA** | 41,661 | 0.976 |

An R2 of 0.976 is really high! It seems like the monthly revenue has a very strong seasonal pattern that these models can pick up easily.

I've also generated plots for each department to see where the models might be struggling. You can find them in the `docs/assets/` folder.

To see the full forecasting pipeline and the department-level charts, go to the notebook `Exercise5/forecast_dept_monthly.ipynb`.
