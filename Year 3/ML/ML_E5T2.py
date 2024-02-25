"""
 * This file contains code snippets to fit different simple linear regression models for each IV/DV pair
 * ML-E5-Task2
 *
 * Original file is located at: https://colab.research.google.com/drive/18CwN138HpRyw9ZSYfhPWRqWAbKINw7A_?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
## EXPERIMENT 5 - Task 2
"""

"""
1.	Import LinearRegression from SKlearn.
"""

from sklearn.linear_model import LinearRegression

"""2.	Create model for linear regression."""

reg1 = LinearRegression()
reg2 = LinearRegression()

"""3.	Conduct simple linear regression for each IV/DV pair.
a.	Interest rate vs stock index price
b.	Unemployment vs stock index price

a.	Interest rate vs stock index price
"""

x_IR = df['Interest_Rate']
x_IR.shape

x_IR_new = x_IR.values.reshape(-1,1)
x_IR_new.shape

y_SIP = df['Stock_Index_Price']
y_SIP.shape

y_SIP_new = y_SIP.values.reshape(-1, 1)
y_SIP_new.shape

reg1.fit(x_IR_new, y_SIP_new)

print("Model coefficients:", reg1.coef_)
print("Model intercept:", reg1.intercept_)

"""b.	Unemployment vs stock index price"""

x_UR = df['Unemployment_Rate']
y_SIP = df['Stock_Index_Price']

x_UR.shape

y_SIP.shape

x_UR_new = x_UR.values.reshape(-1, 1)
y_SIP_new = y_SIP.values.reshape(-1, 1)

x_UR_new

y_SIP_new

reg2.fit(x_UR_new, y_SIP_new)

print("Model coefficients:", reg2.coef_)
print("Model intercept:", reg2.intercept_)

"""4.	Determine and tabulate the values of R2, slope and intercept for each model."""

# a.	Interest rate vs stock index price
r2_IR = reg1.score(x_IR_new, y_SIP_new)
slope_IR, intercept_IR = reg1.coef_, reg1.intercept_

# b.	Unemployment vs stock index price
r2_UR = reg2.score(x_UR_new, y_SIP_new)
slope_UR, intercept_UR = reg2.coef_, reg2.intercept_

print('Interest Rate:')
print('R2= ',r2_IR,'\nSlope= ',slope_IR,'\nIntercept= ',intercept_IR)

print('\n\nUnemployment Rate:')
print('R2= ',r2_UR,'\nSlope= ',slope_UR,'\nIntercept= ',intercept_UR)

"""5.	Determine the predicted value of stock index price for interest rate of 2.75."""

reg1.predict([[2.75]])

"""6.	Determine the predicted value of stock index price for unemployment rate of 6."""

reg2.predict([[6]])

"""7.	Compare both the models based on R2 and the mean square error between predicted and actual stock index price."""

from sklearn.metrics import mean_squared_error

dv1 = reg1.predict(x_IR_new)
print(dv1)
dv2 = reg2.predict(x_UR_new)
print(dv2)

print('R2 of Interest Rate IV1:', reg1.score(x_IR_new, y_SIP_new))
print('MSE of IR: ', mean_squared_error(y_SIP_new, dv1))
print("")
print('R2 of Unemployment Rate IV2:', reg2.score(x_UR_new, y_SIP_new))
print('MSE of UR: ', mean_squared_error(y_SIP_new,dv2))


