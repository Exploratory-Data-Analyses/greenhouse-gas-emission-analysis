'''
    This is a program to analyse a soccer game
    Tools: Random Forest, Gradient Boosting, SARIMA, ARIMA,
'''

import pandas as pd
import janitor
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error


def load_data(filepath):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The dataset is empty.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The data file is empty or not properly formatted.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def clean_data(df):
    """Clean the dataset."""
    try:
        df = df.rename_column('Value', 'Amount')
        df = df.rename_column('Country or Area', 'Country')
        df['Amount'] = df['Amount'] / 1000
        df['Year'] = pd.PeriodIndex(df['Year'], freq='Y')
        return df
    except KeyError as e:
        raise KeyError(f"Missing expected column: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during data cleaning: {e}")


def plot_country_contribution(df):
    """Plot greenhouse gas emissions by country."""
    try:
        country = df.groupby('Country')['Amount'].sum()
        country.plot(kind='bar')
        plt.title('Greenhouse Gas Emissions by Country (2019 - 2021)')
        plt.ylabel('Amount (in kilotonne CO2 equivalent)')
        plt.xlabel('Country or Area')
        plt.xticks(fontsize='small', rotation=60, ha='right', va='top', rotation_mode='anchor')
        plt.tight_layout()
        plt.savefig('../figures/country.jpg')
        plt.show()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting country contribution: {e}")


def plot_yearly_contribution(df):
    """Plot yearly greenhouse gas emissions."""
    try:
        year = df.groupby('Year')['Amount'].sum()
        year.plot(marker='o', ms=2)
        plt.title('Yearly Greenhouse Gas Emissions')
        plt.ylabel('Amount (in kilotonne CO2 equivalent)')
        plt.xlabel('Year')
        plt.tight_layout()
        plt.savefig('../figures/yearly.jpg')
        plt.show()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting yearly contribution: {e}")


def plot_yearly_contribution_by_countries(df):
    """Plot yearly greenhouse gas emissions by countries."""
    try:
        country_yearly = df.groupby(['Country', 'Year'])['Amount'].sum().reset_index()
        country_yearly = country_yearly.pivot(index='Country', columns='Year', values='Amount')
        country_yearly['Total'] = country_yearly.sum(axis=1)
        top_countries = country_yearly.nlargest(5, 'Total')
        top_countries = top_countries.drop(columns='Total')
        top_countries.T.plot(kind='bar')
        plt.legend(title='Country', loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
        plt.title('Greenhouse Gas Emission by Countries')
        plt.ylabel('Amount (in kilotonne CO2 equivalent)')
        plt.xlabel('Year')
        plt.xticks(fontsize='small', rotation=45, va='top', ha='center')
        plt.tight_layout(rect=[0, 0, 2, 0])
        plt.savefig('../figures/country-yearly.jpg')
        plt.show()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting yearly contribution by countries: {e}")


def make_predictions(df):
    """Make predictions for future greenhouse gas emissions."""
    try:
        df['Year'] = df['Year'].dt.year
        df = df.groupby('Year')['Amount'].sum().reset_index()

        x = df['Year'].values.reshape(-1, 1)
        y = df['Amount'].values

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(x_train, y_train)

        y_pred = rf.predict(x_test)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        print(f'MAPE: {mape}')

        future_years = np.arange(2022, 2031).reshape(-1, 1)
        forecast = rf.predict(future_years)

        plt.plot(x, y, marker='o', ms=2, label='Original')
        plt.plot(future_years, forecast, marker='o', ms=2, label='Forecast (2022 - 2030)')
        plt.title('Greenhouse Gas Emission Prediction')
        plt.xlabel('Year')
        plt.xticks(fontsize='small', rotation=45, va='top', ha='center')
        plt.ylabel('Amount')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('../figures/forecast.jpg')
        plt.show()
    except Exception as e:
        raise RuntimeError(f"An error occurred during prediction: {e}")


def main():
    # Load dataset
    filepath = '../data/data.csv'
    try:
        df = load_data(filepath)
    except Exception as e:
        print(e)
        return

    # Clean data
    try:
        df = clean_data(df)
    except Exception as e:
        print(e)
        return

    # Plot country contribution
    try:
        plot_country_contribution(df)
    except Exception as e:
        print(e)

    # Plot yearly contribution
    try:
        plot_yearly_contribution(df)
    except Exception as e:
        print(e)

    # Plot yearly contribution by countries
    try:
        plot_yearly_contribution_by_countries(df)
    except Exception as e:
        print(e)

    # Make predictions
    try:
        make_predictions(df)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
