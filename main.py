'''
    This is a program to analyse a soccer game
    Tools: Random Forest, Gradient Boosting, SARIMA, ARIMA,
'''

import pandas as pd
import csv
import janitor
from matplotlib import pyplot as plt

# load dataset
df = pd.read_csv('data.csv')

# clean data
df = df.rename_column('Value', 'Amount')                # rename columns
df = df.rename_column('Country or Area', 'Country')
df['Amount'] = df['Amount']/1000                        # change for kilo to mega
df['Year'] = pd.PeriodIndex(df['Year'], freq='Y')       # convert 'Year' column to PeriodIndex (time span)


# countries' contribution
country = df.groupby('Country')['Amount'].sum()
country.plot(kind='bar')
plt.title('Greenhouse Gas Emissions by Country (2019 - 2021)')
plt.ylabel('Amount (in kilotonne CO2 equivalent)')
plt.xlabel('Country or Area')
plt.xticks(fontsize='small', rotation=60, ha='right', va='top', rotation_mode='anchor')
plt.tight_layout()
plt.savefig('output/country.jpg')
plt.show()

# yearly contribution
year = df.groupby('Year')['Amount'].sum()
year.plot(marker='o', ms=2)
plt.title('Yearly Greenhouse Gas Emissions')
plt.ylabel('Amount (in kilotonne CO2 equivalent)')
plt.xlabel('Year')
plt.tight_layout()
plt.savefig('output/yearly.jpg')
plt.show()


# yearly contribution by countries
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
plt.savefig('output/country-yearly.jpg')
plt.show()

# make predictions for the future
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error


df['Year'] = df['Year'].dt.year
df = df.groupby('Year')['Amount'].sum().reset_index()

x = df['Year'].values.reshape(-1, 1)    # reshape to 2D for sklearn model
y = df['Amount'].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# create and fit model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)
mape = mean_absolute_percentage_error(y_test, y_pred)
print(f'MAPE: {mape}')


# forecast for future
future_years = np.arange(2022, 2031).reshape(-1, 1)
forecast = rf.predict(future_years)

# visualise outputs
plt.plot(x, y, marker='o', ms=2, label='Original')
plt.plot(future_years, forecast, marker='o', ms=2, label='Forecast (2022 - 2030)')
plt.title('Greenhouse Gas Emission Prediction')
plt.xlabel('Year')
plt.xticks(fontsize='small', rotation=45, va='top', ha='center')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('output/forecast.jpg')
plt.show()

