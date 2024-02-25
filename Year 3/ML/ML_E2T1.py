"""
 * This file contains code snippets for using different types of Python libraries for plotting data
 * ML-E2-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/19zag3G0H2e7cjLhyx6hQpZOGahwW8JNw
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # used for plotting. have better colors than matplot

"""i.	Plot a scatter plot for X (from 0 to 10) and Y (from 11 to 21). Save the scatter plot"""

# scatter plot is binomial plot because it takes 2 values
x = np.arange(0,10)
y = np.arange(11,21)

# plotting scatter plot
plt.scatter(x,y,c='teal')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter plot graph in 2D')
plt.savefig('Test.png')

"""ii.	Create a subplot with different markers and different line colors"""

# line marker
plt.subplot(2,2,1)
plt.plot(x,y,c='firebrick')

# dash marker
plt.subplot(2,2,2)
plt.plot(x,y,'c--')

# dash+star marker
plt.subplot(2,2,3)
plt.plot(x,y,'m*--')

# o / dot marker
plt.subplot(2,2,4)
plt.plot(x,y,'yo')

"""iii.	Plot a bar plot for below X and Y values.
X= [2,8,10] Y= [11,16,9]
"""

X= [2,8,10]
Y= [11,16,9]
plt.bar(X,Y,color='cornflowerblue')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Bar graph')
plt.show()

"""iv.	Plot a box plot for the values given below and state your inference.
A= [3,4,5,7,9,8,12,13,7,8,19,90,12,15]
"""

A= [3,4,5,7,9,8,12,13,7,8,19,90,12,15]
plt.boxplot(A)
plt.title('Box graph')
plt.show()

# box chart with modified values
A= [-10,-1,3,4,5,7,9,8,12,13,7,8,19,90,12,15,100]
plt.boxplot(A)
plt.title('Box graph')
plt.show()
# circle is at 90 which is showing outlier. orange line doenotes median value. box denotes 50% middle values
