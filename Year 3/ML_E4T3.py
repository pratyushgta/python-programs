"""
 * This file contains code snippets for performing exploratory data analysis on salary dataset
 * ML-E4-Task3
 *
 * Original file is located at: https://colab.research.google.com/drive/1wWsVDblqw_R0zST1RmabmnWRMq458xCj?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""
"""## EXPERIMENT 4 - Task 3

1.	Import salary.csv into your notebooks.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Salary_Data.csv')

"""2.	Explore the dataset using head and describe."""

df.head()

df.describe()

"""3.	Repeat steps 2 to 6 from task 2."""

x= df['YearsExperience']
y= df['Salary']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
# test_size = 0.2 meand 80% is train data and 20% becomes test data
# if we don't write random_split=0, it is going to randomly split the data

x_train.shape

y_train.shape

# currently x_train and y_train are in form of data frame. model will take arrays
x_train = np.array([x_train])
y_train = np.array([y_train])
# similarly, converting test data
x_test = np.array([x_test])
y_test = np.array([y_test])

x_train.shape

y_train.shape

# converting test and train to 2D because model takes input as 24 rows and 1 col
x_train = x_train.reshape(-1,1)
y_train = y_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
y_test = x_test.reshape(-1,1)

x_train.shape

y_train.shape

#import numpy as np
#from sklearn.linear_model import LinearRegression

reg = LinearRegression()
# calc coeff from training dataset
reg.fit(x_train, y_train)
print(reg.coef_) # b1
print(reg.intercept_) # b0

# Visualizing the training set
plt.scatter(x_train, y_train, color='tomato')
plt.plot(x_train, reg.predict(x_train), color='teal')
plt.title('Salary vs Experience (training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show

# predicting the test set results
y_pred = reg.predict(x_test)
y_pred

# Visualizing the test set
plt.scatter(x_test, y_test, color='tomato')
plt.plot(x_test, reg.predict(x_test), color='teal')
plt.title('Salary vs Experience (testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show

from sklearn.metrics import r2_score
r2_new1 = r2_score(y_test, y_pred)
print(r2_new1)

"""4.	Plot a scatter plot of work experience vs salary"""

plt.scatter(x,y,c='teal')
plt.xlabel('Years of Experience (x)')
plt.ylabel('Salary (y)')
plt.title('Scatter plot')
plt.show()

