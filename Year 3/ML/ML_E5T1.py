"""
 * This file contains code snippets to find Relationships between the different features
 * ML-E5-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/18CwN138HpRyw9ZSYfhPWRqWAbKINw7A_?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
## EXPERIMENT 5 - Task 1
"""

"""
1.	Import the relevant libraries.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""2.	Load the MLR_data.csv in your notebooks."""

df = pd.read_csv("MLR_data.csv")
df

"""3.	Perform EDA on the dataset by using head, shape and describe functions."""

df.head()

df.shape

df.describe()

"""4.	Identify the independent variables (IV) and dependent variable (DV) and plot the scatter plot of IV vs DV. Write your inference for each plot."""

# Independent variables
IV = df[['Year','Month','Interest_Rate','Unemployment_Rate']]

# Dependent variable
DV = df['Stock_Index_Price']

# Checking the relationships between independent variable and dependent variable using scatter plot and correlations.
plt.scatter(IV['Year'], DV)
plt.xlabel('Year')
plt.ylabel('Stock Index Price')
plt.title('Year vs Stock Index Price')
plt.show()

plt.scatter(IV['Month'], DV)
plt.xlabel('Month')
plt.ylabel('Stock Index Price')
plt.title('Month vs Stock Index Price')
plt.show()

plt.scatter(IV['Interest_Rate'], DV)
plt.xlabel('Interest Rate')
plt.ylabel('Stock Index Price')
plt.title('Interest Rate vs Stock Index Price')
plt.show()

plt.scatter(IV['Unemployment_Rate'], DV)
plt.xlabel('Unemployment Rate')
plt.ylabel('Stock Index Price')
plt.title('Unemployment Rate vs Stock Index Price')
plt.show()

# Calculate the correlations between the independent variables and the dependent variable
corr_matrix = IV.corrwith(DV)
corr_matrix

"""5.	Plot the scatter plots for IV vs IV. Write your inference for each plot."""

# Year vs Month
sns.scatterplot(data=df, x="Year", y="Month")
plt.title("Year vs Month")
plt.show()
# There appears to be a weak positive correlation between Year and Month.

# Year vs Interest Rate
sns.scatterplot(data=df, x="Year", y="Interest_Rate")
plt.title("Year vs Interest Rate")
plt.show()
# There is a weak negative correlation between Year and Interest Rate.

# Year vs Unemployment Rate
sns.scatterplot(data=df, x="Year", y="Unemployment_Rate")
plt.title("Year vs Unemployment Rate")
plt.show()
# There is a weak negative correlation between Year and Unemployment Rate.

# Month vs Interest Rate
sns.scatterplot(data=df, x="Month", y="Interest_Rate")
plt.title("Month vs Interest Rate")
plt.show()
# There is a weak positive correlation between Month and Interest Rate.

# Month vs Unemployment Rate
sns.scatterplot(data=df, x="Month", y="Unemployment_Rate")
plt.title("Month vs Unemployment Rate")
plt.show()
# There is a weak negative correlation between Month and Unemployment Rate

# Interest Rate vs Unemployment Rate
sns.scatterplot(data=df, x="Interest_Rate", y="Unemployment_Rate")
plt.title("Interest Rate vs Unemployment Rate")
plt.show()
# There is a weak positive correlation between Interest Rate and Unemployment Rate.

# if corr = 1, they are highly correlated
# if it is around 0.5, they are weakly correlated
# month and interest rate have higher correlation with stock index price
# unemployment rate and interest rate have negative correlation
# between IV, there shouldn't be any correlation or weak correlation
matrix = df.corr().round(2)
print(matrix)
