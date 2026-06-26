import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('8. Netflix Dataset.csv')
print(data)

# Remove duplicate records
data[data.duplicated()]
data.drop_duplicates(inplace=True)
print(data[data.duplicated()])
print(data)

# Check for missing (null) values
print(data.isnull().sum())
data.fillna('Unknown', inplace=True)
print(data.isnull().sum())
print(data.isnull())

# Convert/standardize date format
data['Date_N'] = pd.to_datetime(data['Release_Date'], errors='coerce')
print(data.dtypes)
print(data)

# Count records by year with a filter for >= 2015
print(data['Date_N'].dt.year.value_counts())
data_filtered = data[data['Date_N'].dt.year >= 2015]
print(data_filtered)

data_filtered.to_csv("Netflix_Cleaned.csv", index=False)