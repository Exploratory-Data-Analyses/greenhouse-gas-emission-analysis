# Methodology

## Data Loading and Cleaning

1. **Load the Dataset**: The dataset is loaded from a CSV file using Pandas.
2. **Rename Columns**: Columns are renamed for consistency and clarity:
   - 'Value' to 'Amount'
   - 'Country or Area' to 'Country'
3. **Unit Conversion**: The 'Amount' column, originally in tonnes, is converted to kilotonnes.
4. **Year Conversion**: The 'Year' column is transformed into a Pandas PeriodIndex to facilitate time-based operations.

## Data Analysis and Visualization

1. **Emissions by Country**:
   - Group data by 'Country' and sum the 'Amount' to find the total emissions for each country.
   - Create a bar plot to visualize emissions by country.

2. **Yearly Emissions**:
   - Group data by 'Year' and sum the 'Amount' to find the total yearly emissions.
   - Generate a line plot to illustrate the trend in emissions over the years.

3. **Yearly Emissions by Country**:
   - Group data by both 'Country' and 'Year' to find emissions for each country per year.
   - Pivot the data to create a matrix of emissions and plot the top countries' yearly emissions.

## Predictive Modeling

1. **Data Preparation**:
   - Aggregate emissions data by year.
   - Prepare feature and target variables for modeling.

2. **Model Training and Evaluation**:
   - Split data into training and testing sets.
   - Train a Random Forest Regressor model on the training data.
   - Evaluate the model using Mean Absolute Percentage Error (MAPE).

3. **Forecasting**:
   - Predict future emissions for the years 2022 to 2030 using the trained model.
   - Visualize the forecasted data alongside historical data.

## Tools

- **Pandas**: For data manipulation and cleaning.
- **Matplotlib**: For visualization.
- **Scikit-learn**: For building and evaluating the Random Forest model.
- **NumPy**: For numerical operations.
- **Janitor**: For enhanced data cleaning utilities.
