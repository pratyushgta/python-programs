"""
 * This file contains code snippets to implement a Multiple regression model
 * ML-E5-Task3
 *
 * Original file is located at: https://colab.research.google.com/drive/18CwN138HpRyw9ZSYfhPWRqWAbKINw7A_?usp=sharing
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
## EXPERIMENT 5 - Task 3
"""

"""
1.	Use both interest rate and unemployment rate and create a multiple regression model.
"""

from sklearn.model_selection import train_test_split

multx = df[['Interest_Rate','Unemployment_Rate']]
print(multx.shape)

multy = df['Stock_Index_Price']
print(multx.shape)

xmultrain, xmultest, ymultrain, ymultest=train_test_split(multx,multy,test_size=0.2,random_state=0)

"""2.	Determine the value of R2, slope and intercept for the model."""

# xmultrain and y multrain have 2 variables so we use linear regression
reg = LinearRegression().fit(xmultrain, ymultrain)

print("Multiple Linear Regression for Interest Rate and Unemployment Rate and Stock Index Price")
print("Slope for Interest Rate variable is: ", reg.coef_[0])
print("Slope for Unemployment Rate variable is: ", reg.coef_[1])
print("Intercept of the plane is: ", reg.intercept_)
print("The ratio of change explained by model is: ", reg.score(xmultrain, ymultrain))

print('R_sqr:', reg.score(xmultrain, ymultrain))

"""3.	Determine the predicted value of stock index price for:
  * interest rate =2.75 and unemployment rate = 5.3
  * interest rate =2 and unemployment rate = 6


"""

# a.	interest rate =2.75 and unemployment rate = 5.3
reg.predict([[2.75, 5.3]])

# b.	interest rate =2 and unemployment rate = 6
reg.predict([[2, 6]])

"""4. Compare the model with both the models from task 2."""

print('R2 of IV 1:', reg1.score(x_IR_new, y_SIP_new),"\n")
print('R2 of IV 2:', reg2.score(x_UR_new, y_SIP_new),"\n")
print('R2 of Multiple Linear Regression:', reg.score(xmultrain, ymultrain))

"""5.	Identify and state the best model for the dataset.

The best model is Multi Linear Regression as its R square is greater than the simple Linear Regression Model.
"""
