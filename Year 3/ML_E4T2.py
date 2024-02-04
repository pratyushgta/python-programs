"""
 * This file contains code snippets to implement Linear Regression from sklearn
 * ML-E4-Task2
 *
 * Original file is located at: https://colab.research.google.com/drive/1wWsVDblqw_R0zST1RmabmnWRMq458xCj?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""## EXPERIMENT 4 - Task 2

1.	Import LinearRegression from SKlearn.
"""
import numpy as np
from sklearn.linear_model import LinearRegression

"""2.	Reshape x to make it two dimensional array."""

x.shape

x_new = x[:,np.newaxis]
x_new.shape

y_new = y[:,np.newaxis]
y_new.shape

"""3.	Create a model for linear regression."""

model = LinearRegression()

"""4.	Train the model using model.fit"""

model.fit(x_new, y_new)

"""5.	Determine the value of intercept (b0) and slope(b1). Compare the values as obtained from task 1."""

#print("Regression coef: ",model.coef_) # b1
#print("Regression intercept: ",model.intercept_) # b0

b0_new = model.intercept_
print("Regression intercept:", b0_new)
print("b0 OG: ", b0)
b1_new = model.coef_
print("Regression coef:", b1_new)
print("b1 OG: ", b1)

BMI_1 = np.array([27])
model.predict(BMI_1[:,np.newaxis])

"""6.	Determine the value of r2. Compare the value with the one obtained in task 1."""

r2_new = model.score(x_new, y_new)
print("OG R-square ", r2)
print("R-square: ", r2_new)