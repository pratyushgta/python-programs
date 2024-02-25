"""
 * This file contains code snippets for performing exploratory data analysis on seeds dataset
 * ML-E2-Task2
 *
 * Original file is located at: https://colab.research.google.com/drive/19zag3G0H2e7cjLhyx6hQpZOGahwW8JNw
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # used for plotting. have better colors than matplot

"""## EXPERIMENT 2 - Task 2
v.	Read “seeds.csv” file into data frame.
"""

df = pd.read_csv('seeds.csv')
df

"""vi.	Explore the dataset by using head and describe."""

df.head()

df.describe()

df.columns

df.dtypes

df.dtypes.unique()

"""vii.	Find the number of samples per type."""

df['Type'].value_counts(ascending=True)

df['Type'].value_counts().plot.bar()

"""viii.	Plot a scatter plot for Kernel Width vs Length. Write your inference."""

# plotting kernel width vs len
plt.scatter(df['Kernel.Length'],df['Kernel.Width'],c='teal')
# if it is +ve, or -ve relationship, we can apply linear regression. if there is no relation, we cannot apply linear regression

# alternate method for plotting
sns.scatterplot(x='Kernel.Length',y='Kernel.Width', data=df)
# each data point is each data row. below plot shows 199 seeds of different length and width.

"""ix.	Different type should have different colours in above scatter plot"""

# differentiate seed types by assigning color to each type
sns.scatterplot(x='Kernel.Length',y='Kernel.Width', hue='Type', data=df)
# overlapping is between 3 n 1 & 1 n 2

# different color pallete
sns.scatterplot(x='Kernel.Length',y='Kernel.Width', hue='Type', data=df, palette = 'pastel')

"""x.	Plot a Jointplot to understand relation between Perimeter and Compactness. Write your inference."""

sns.jointplot(x='Perimeter',y='Compactness', data=df)

"""Inference:
Joint plot = Scatter plot + histogram
Scatter plot shows Positive relationship. This indicates that as the perimeter of the seeds increases, the compactness tends to increase.
Histogram is denoting frequency of value stored in variable

xi.	Plot a Box plot to understand correlation between compactness and type.
"""

# unique values in type attribute
df['Type'].unique()

sns.boxplot(x='Type', y='Compactness', data=df)

"""Inference:
1. Type 2 has highest compactness and Type 3 has lowest
2. No outliers for Type 2 and Type 3

xii.	Plot a pair plot to understand all characteristics with type being the main parameter. State your inference
"""

sns.pairplot(df, hue='Type', diag_kind='hist')

"""Inference:
1. All char = all attributes/ all columns
2. Pair plot is a nxn chart. n = number of attributes. For eg. [0,0] = Area, Area relation [1,0] = Area, Perimeter relation
3. Pair plot provides a comprehensive view of the relationships between multiple numerical variables in the dataset while considering a categorical variable as the main parameter
4. Asymmetric coeff. has no corelation (just scattered and has no relation). Therefore we can remove this column as it won't be able to predict anything

xiii.	Plot a Violin plot to understand correlation between compactness and type. State your inference
"""

# Center = box plot. White dot in center = median (Q2)
# Curved shape is nothing but a histogram.
# Curve is made by first forming a histogram, gets a smooth curve, rotates the histogram, shifts bars to get central axis. Based on central axis, divides the histograph
sns.violinplot(x='Type', y='Compactness', data=df)

"""Inference:
- Wider sections in the plot indicate a higher frequency of data points, while narrower sections represent lower frequency.
- Differences in the shapes (spread of the violins) indicates varying compactness characteristics among different seed types.

xiv.	Plot a Kernel Density Estimation plots to understand correlation between compactness and type. State your inference
"""

# KDE plots provide a smooth estimation of the probability density function of a continuous variable (Compactness)
# across different categories (Type)

#sns.displot(df, x='Compactness', hue='Type', kind='kde', fill=True)
sns.FacetGrid(df,hue='Type',height=5).map(sns.kdeplot,'Compactness').add_legend()

"""xv.	Plot a pair plot to understand all characteristics with type being the main parameter. (the main parameter, with KDE instead of histogram in diagonal subplots)"""

# Creating pair plot with KDE on diagonal
# by default it takes kde
sns.pairplot(df, hue='Type', height=3)

"""xvi.	An Andrews curve to display separability of data according to Type."""

from pandas.plotting import andrews_curves
# if attributes are overlapping too much, it will be difficult to classify. So, we use andrews curve to check extent of overlapping
# Andrews curves is used to visualize the structure of data by transforming each row of a dataset into a curve
andrews_curves(df, class_column='Type', colormap='viridis')
