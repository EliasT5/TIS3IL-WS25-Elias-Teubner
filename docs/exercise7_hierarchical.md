# Assignment 7: Hierarchical Forecasts

This was the final and most complex assignment. I had to create forecasts at three different levels of the M5 hierarchy:

1.  **Top:** Total revenue for everything.
2.  **Middle:** Revenue by Department and State (e.g., `FOODS_1_CA`).
3.  **Bottom:** Revenue for individual items at specific stores (e.g., `HOBBIES_1_001_CA_1`).

## My Approach

I used the same families of models as before:
- **Baseline:** Seasonal Naive.
- **ML:** Random Forest with Lags and Calendar features.
- **Statistical/Neural:** Fallbacks to the baseline for this implementation.

## Results & Insights

The performance varies a lot depending on the level:

### Middle and Bottom Levels
At these levels, the **ML model (LagML)** was clearly the best. For example, at the Middle level, it achieved an **R2 of 0.979**, compared to 0.947 for the baseline. At the Bottom level (which is much noisier), it still got an R2 of 0.772.

### The "Top" Level Mystery
Interestingly, at the **Top level**, all models had a negative R2! 
I think this is because at the total aggregate level, the trends are very different from the individual departments. The Seasonal Naive model (which just looks at last year) might be missing a big overall growth or decline in the total Walmart sales that isn't as obvious at the lower levels. 

## Visualization

I created time series plots and scatter plots for all three levels. The scatter plots are really useful to see how the predicted values compare to the actual ones.

- **Bottom Level Scatter:**
![Bottom Scatter](assets/exercise7_bottom_scatter.png)

For the full analysis across all levels and the aggregated charts, go to the notebook `Exercise7/hierarchical_forecasts.ipynb`.
