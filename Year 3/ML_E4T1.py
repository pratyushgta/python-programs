"""
 * This file contains code snippets to implement numpy
 * ML-E4-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/1wWsVDblqw_R0zST1RmabmnWRMq458xCj?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
## EXPERIMENT 4 - Task 1
"""

import numpy as np
import pandas as pd
from scipy import stats
# for min_max scaling
from mlxtend.preprocessing import minmax_scaling
# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt
# set seed for reproducibility
#np.random.seed(0)

"""1.	Define two Numpy arrays x and y   which represents BMI and Cholesterol
x= [5,15,25,35,45,55] and y= [11,16,18,30,22,38]
"""

x= np.array([5,15,25,35,45,55])
y= np.array([11,16,18,30,22,38])

"""2.	Plot a scatter plot of x and y."""

# plotting scatter plot
plt.scatter(x,y,c='teal')
plt.xlabel('BMI (x)')
plt.ylabel('Cholesterol (y)')
plt.title('Scatter plot')

"""3.	Write a python function to compute the values of the coefficients of linear regression, b0 and b1."""

x_bar = np.mean(x)
y_bar = np.mean(y)

x_diff = np.array([])
y_diff = np.array([])
x_sq = np.array([])
mult = np.array([])

for i in range(np.size(x)):
  x_diff = np.append(x_diff, (x[i]-x_bar))
  y_diff = np.append(y_diff, (y[i]-y_bar))

for i in range(np.size(x_diff)):
  mult = np.append(mult, (x_diff[i]*y_diff[i]))

x_sq = np.square(x_diff)

b1 = np.sum(mult)/np.sum(x_sq)
print("b1: ", b1)
b0 = (y_bar)-(b1*x_bar)
print("b0: ", b0)

print("\nx-mean: ", x_bar)
print("y-mean: ", y_bar)
print("xi-x_bar: ", x_diff)
print("yi-y_bar: ", y_diff)
print("(xi-x_bar)^2: ", x_sq)
print("mult: ", mult)

"""4.	Determine the predicted value of y for x=27."""

y_pred = y-(b0 + (b1*27))
print('Predicted value of y for x=27:', y_pred)

"""5.	Plot the regression line on the scatter plot."""

plt.scatter(x,y,c='teal')
plt.xlabel('BMI (x)')
plt.ylabel('Cholesterol (y)')
plt.title('Scatter plot')
plt.plot(x, b0+(b1*x), color='tomato',linewidth=1)
plt.show()

"""6.	Write a python function to determine the value of r2."""

y_sq = np.square(y_diff) # (yi-y_bar)square
SST = np.sum(y_sq)
SSE = np.sum(np.square(y-(b0+(b1*x))))

r2 = (SST-SSE)/SST
print("R square= ",r2)