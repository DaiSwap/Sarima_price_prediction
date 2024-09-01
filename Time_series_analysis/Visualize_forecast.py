import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import datetime, timedelta

# Step 1: Load the data, skipping the first row for headers and specifying column names
data = pd.read_excel("prices.xlsx", header=None, skiprows=1, names=['Month', 'Price'])

# Step 2: Convert Month to DateTime Format
data['Month'] = pd.to_datetime(data['Month'])

# Step 3: Set 'Month' column as index
data.set_index('Month', inplace=True)

# Step 4: Fit SARIMA model
model = SARIMAX(data['Price'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
result = model.fit()

# Step 5: Forecast prices for the next 6 months
forecast_dates = [data.index[-1] + timedelta(days=i*30) for i in range(1, 7)]
forecast = result.predict(start=len(data), end=len(data)+5)

# Step 6: Plot original data and forecast
plt.plot(data.index, data['Price'], label='Actual Prices')
plt.plot(forecast_dates, forecast, label='Forecasted Prices')
plt.xlabel('Month')
plt.ylabel('Price')
plt.title('Black Pepper Prices Forecast')
plt.legend()
plt.show()

