"""
 * This file contains code snippets for performing exploratory data analysis on car dataset
 * ML-E1-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/12saxmansdQRF95O6XYGPfj0sK1hrlFOr
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"i. Read the Toyota.csv file into a DataFrame."
import pandas as pd

# DataFrame is like a data structure in the form of a table where data will be stored in the form of rows and columns
# converting CSV to dataframe
df = pd.read_csv("Toyota.csv")
df
# displaying first few records of df
df.head()
# displaying first 20 records of df
df.head(20)
# printing last few records of df
df.tail()
# printing last few records of df
df.tail(20)

"ii. Explore size, shape, data types of each column in the dataset."
# shape = (rows, cols)
df.shape
# data types of each column
df.dtypes
# object data type = string or text
# some values in FuelType are either null or missing.
df.info()

"iii. List down the columns of dataset"
df.columns

"iv. Find out ‘Fuel Type’ for the 4th row."
# fuel type for first few rows
df['FuelType'].head()
# fuel type for 4th row
## data.iloc[3]['Fuel Type'] or df.at[3,FuelType]
df['FuelType'][3]

"v.	Find out value for second column for the 4th row."
## df.iloc[3, 1]
df.iat[3, 1]  # i in iat means index

"vi. Select all rows for column “Fuel Type”"
df.loc[:, 'FuelType']

"vii. Select all rows for columns “KM”, “HP” and “Automatic”"
df.loc[:, ['KM', 'HP', 'Automatic']]

"viii. Display 1 to 5 rows for columns 2 to 4 (excluding row 5 and column 4)"
df.iloc[0:5, 1:4]  # iloc is for index based slicing

"ix. Display the info of dataset and state your observations"
df.info()
df.dtypes
"""
Observations:
1. Dataset contains integer, object (string) and float datatypes
2. Some values in FuelType are either null or missing.
3. Doors column appears to have integer values which are represented as string in dataset (first value is string and rest are numeric values with datatype object)

x.	Identify unique values for columns “KM”, “HP” and “Doors”
"""

df['KM'].unique()

df['KM'].head(50).unique()

df['HP'].head(50).unique()

df['Doors'].head(50).unique()

"xi. Create a new data frame, by replacing “??” with NAN"

# df_new = df.replace('??',"NAN", inplace=True)
df_new = pd.read_csv('Toyota.csv', na_values=["??", "????"])

df_new

df_new.info()

# comparing null value representation in original and modified dataset
print("Unique values of HP in df:", df['HP'].unique())
print("Unique values of HP in df_new:", df_new['HP'].unique())

"""xii.	Replace the categorical values in the “Doors” column with its corresponding numeric value"""

# replacing string in Doors with its corresponding numerical values
# door_mapping = {'two': 2, 'three': 3, 'four': 4, 'five': 5}
# data['Doors'] = data['Doors'].replace(door_mapping) or #df3=df_new['Doors]
df_new['Doors'].replace('three', '3', inplace=True)
df_new['Doors'].replace('four', '4', inplace=True)
df_new['Doors'].replace('five', '5', inplace=True)

df_new.head()

"""xiii.	Convert data types of columns “Doors”, “MetColor” and “Automatic” to int, and object"""
df_new['Doors'].dtypes
# before conversion
df_new.info()

df_new['Doors'] = df_new['Doors'].astype('int64')
df_new['MetColor'] = df_new['MetColor'].astype('object')
df_new['Automatic'] = df_new['Automatic'].astype('object')

# after conversion
df_new.info()
df_new['Doors'].dtypes
df_new.head()

"xiv. Identify the total number of null values in each column of the data set"

# isnull returns true if null is present in each column
df_new.isnull()

df_new.isnull().sum()

"xv. Drop rows with null values"

df_new.shape
df_new = df_new.dropna()
df_new.shape

"xvi. Identify total number of cars that runs on “Petrol”, “Diesel” or “CNG”"
df_new['FuelType'].unique()
df_new['FuelType'].value_counts()

"xvii.	Identify mean of “KM” for the cars that runs on “Diesel”"
# df_new[df_new['FuelType']=='Diesel'].KM.mean()
df_new[df_new.FuelType == 'Diesel'].KM.mean()
