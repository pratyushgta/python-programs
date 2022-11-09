import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/praty/Desktop/RetailDataX.csv")

# Analyzing Data
print(data.head())
print(data.tail())
## Summary of the dataset
print(data.info())
## Finding count of Null values in each column
print(data.isna().sum())
## Printing all null values in 'Description' columnSS
print(data[data['Description'].isna()])
## Printing all null values in 'CustomerID' column
print(data[data['CustomerID'].isna()])

# Scripting for Data Cleaning
## Removing rows with null values
new_df1 = data.dropna()
print(new_df1.isna().sum())

## Replace null values with a default value
new_df2 = data.copy()
new_df2['Description'] = new_df2["Description"].fillna("Default Product")
new_df2['CustomerID'] = new_df2["CustomerID"].fillna(600000)

print(data.isna().sum())  # before
print(new_df2.isna().sum())  # after

print(data.loc[680])  # before
print(new_df2.loc[680])  # after

## Remove irregularities in data
print(data.loc[1511])  # before
filtered = new_df2[(new_df2['Country'] == "EIRE")].index
new_df2.drop(filtered)
print(new_df2.loc[1511])  # after


# Functioning with Dates
new_df3 = data.copy()
## Check the datatype of date column
print(new_df3['date_added'])

## Converting dates to correct format i.e. in dd-mm-yyyy
date = pd.to_datetime(new_df3['date_added'], dayfirst=True)
new_df3['date_added'] = date.dt.strftime('%d-%m-%Y')
print(new_df3['date_added'])

## Removing rows with Null date value
new_df3.dropna(subset=['date_added'])
print("Count of rows with Null date value: ", new_df3['date_added'].isna().sum())


# Character Operations
new_df8 = data.copy()
## Replace characters in column
print(new_df8['Description'].head(), "\n", new_df8['Country'].head())
new_df8 = new_df8.replace(" ", '+', regex=True)
print("\n", new_df8['Description'].head(), "\n", new_df8['Country'].head())


# Functions
new_df4 = data.copy()
## Check for duplicates
print(new_df4.duplicated())
new_df4.drop_duplicates()

## Replacing values using Mean
print(new_df4.loc[680])  # before
x = new_df4["CustomerID"].mean()
new_df4["CustomerID"] = new_df4["CustomerID"].fillna(x)
print(new_df4.loc[680])  # after

## Replacing values using Median
new_df_5 = data.copy()
print(new_df_5.loc[680])  # before
x = new_df_5["CustomerID"].median()
new_df_5["CustomerID"] = new_df_5["CustomerID"].fillna(x)
print(new_df_5.loc[680])  # after

## Replacing values using Mode
new_df6 = data.copy()
print(new_df6.loc[680])  # before
x = new_df6["CustomerID"].mode()
new_df6["CustomerID"] = new_df6["CustomerID"].fillna(x)
print(new_df6.loc[680])  # after

# Distributing Data
new_df_5 = data.copy()
new_df_5Num = new_df_5.select_dtypes(include='number')
## Data Correlation
print(new_df_5Num.corr())

## Detect Outliers
for col in data.columns:
    print(new_df_5[col].describe())

## Plotting
### Visualizing Dataframe
new_df_5Num.plot()
plt.show()

### Scatter Plot
new_df_5Num.plot(kind='scatter', x='Quantity', y='UnitPrice')
plt.show()
