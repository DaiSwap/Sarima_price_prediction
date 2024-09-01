import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data, skipping the first row for headers and specifying column names
data = pd.read_excel("prices.xlsx", header=None, skiprows=1, names=['Month', 'Price'])

# Step 2: Check for Missing Values
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)

# Print column names
print("Column Names:")
print(data.columns)

# Step 3: Convert Month to DateTime Format
data['Month'] = pd.to_datetime(data['Month'])

# Step 4: Sort Data by Month
data.sort_values(by='Month', inplace=True)

# Step 5: Visualize the Data
plt.plot(data['Month'], data['Price'])
plt.xlabel('Month')
plt.ylabel('Price')
plt.title('Black Pepper Prices Over Time')
plt.show()
