"""
 * This file contains code snippets to performing dataset cleaning operations on adultPrac7.csv
 * ML-E7-Task2
 *
 * Original file is located at: https://colab.research.google.com/drive/1R-YzFUNjbV6g85CR2NC0XHQ7FipvD7pY
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""•	Upload data set into the dataframe"""

df = pd.read_csv("adultPrac7.csv")

df.head()

"""•	Check the shape of the data set."""

df.shape

"""•	Find out all the categorical columns from the data set"""

# Printing all columns
df.columns

# selecting categorical columns
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
# Printing only categorical columns
cat_cols

"""•	Check if null values exist in all the categorical columns"""

df[cat_cols].isna().sum()

"""•	Identify the problems with “workclass”, “Occupation”,”native_country” columns and rectify it."""

# finding unique values in each column
for val in cat_cols:
    print('Unique values in ', val, ':', '\n', df[val].unique())
    print()

df.dtypes

# Replace '?' with null in categorical columns
for val in cat_cols:
    df[val] = df[val].replace(' ?', pd.NA)

# Check for null values in categorical columns
df[cat_cols].isna().sum()

# Replace all null values with the mode of the respective column
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

df[cat_cols].isna().sum()

"""•	Explore numeric columns and check any null values exist for the numeric columns."""

# selecting all numeric columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Printing only categorical columns
num_cols

# Check if null values exist in all the numeric columns
df[num_cols].isna().sum()

# finding unique values in each column
for val in num_cols:
    print('Unique values in ', val, ':', '\n', df[val].unique())
    print()

"""•	Create a feature vector with x= all the columns except income and y=income"""

# Selecting all columns except 'income' as features
X = df.loc[:, df.columns != 'income']

# Selecting 'income' as target variable
Y = df[['income']]

print(X.columns, '\n', Y.columns)

Y.head()

# Converting target variable Y into binary values by replacing '>50K' with 1 and '<=50K' with 0
# because roc_curve and roc_auc_score functions require binary values (0, 1) or (-1, 1)
Y = Y.replace({' >50K': 1, ' <=50K': 0})

Y.head()

Y.dtypes

"""o	Apply one hot encoding on all the categorical columns"""

X_cat_cols = X.select_dtypes(include=['object']).columns.tolist()

# One-hot encoding on all categorical columns in the X dataset
X = pd.get_dummies(X, columns=X_cat_cols)

X.columns

"""•	Implement feature engineering for the train, test split data set:

"""

from sklearn.model_selection import train_test_split

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)  # 0.2 42 or 0.33 125

print("cols in training set:", X.shape[1])
print("cols in test set:", X_test.shape[1])

"""o	Check the data types of columns of the input features of training data set"""

X_train.dtypes

"""o	Identify categorical columns that has null values and fill them with most probable value in the data set"""

X_train.isna().sum()

# finding unique values in each column
for val in X_train:
    print('Unique values in ', val, ':', '\n', X_train[val].unique())
    print()

"""Inference: No null or miscoded values found since they were already handled in the original dataset, before separating input and output features.

o	Repeat above step for the input features of test data set
"""

# Check the data types of columns of the input features of testing data set
X_test.dtypes

# Identify categorical columns that has null values and fill them with most probable value in the data set
X_test.isna().sum()

# finding unique values in each column
for val in X_test:
    print('Unique values in ', val, ':', '\n', X_test[val].unique())
    print()

"""o	Apply feature scaling using robust scaler"""

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

# Fitting the scaler to training data
X_train = scaler.fit_transform(X_train)

# Transforming the test data using the scaler
X_test = scaler.transform(X_test)