"""
 * This file contains code snippets for performing exploratory data analysis on seeds dataset
 * ML-E2-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/19zag3G0H2e7cjLhyx6hQpZOGahwW8JNw
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # used for plotting. have better colors than matplot

"""v.	Read “seeds.csv” file into data frame."""

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

"""
x.	Plot a Jointplot to understand relation between Perimeter and Compactness. Write your inference.
"""

sns.jointplot(x='Perimeter',y='Compactness', data=df)

"""Inference: Positive Linear relationship. This positive correlation indicates that as the perimeter of the seeds increases, the compactness tends to increase.

xi.	Plot a Box plot to understand correlation between compactness and type.
"""

sns.boxplot(x='Type', y='Compactness', data=df)
plt.xlabel('Type')
plt.ylabel('Compactness')
plt.title('Compactness by Type')
plt.show()

"""xii.	Plot a pair plot to understand all characteristics with type being the main parameter. State your inference"""

# Pair plot provides a comprehensive view of the relationships between multiple numerical variables in the dataset while considering a categorical variable as the main parameter

# Dropping non-numeric columns for the pairplot
numeric_columns = df.select_dtypes(include=['float64', 'int64'])
# 'Type' is the categorical column here
# Add the 'Type' column to the selected numeric columns
numeric_columns['Type'] = df['Type']
sns.pairplot(numeric_columns, hue='Type')
plt.show()

"""Inference:

xiii.	Plot a Violin plot to understand correlation between compactness and type. State your inference
"""

sns.violinplot(x='Type', y='Compactness', data=df)
plt.xlabel('Type')
plt.ylabel('Compactness')
plt.title('Compactness by Type')
plt.show()

"""Inference:
- Wider sections in the plot indicate a higher density of data points, while narrower sections represent lower density.
- Differences in the shapes or spread of the violins can indicate varying compactness characteristics among different seed types.

xiv.	Plot a Kernel Density Estimation plots to understand correlation between compactness and type. State your inference
"""

# KDE plots provide a smooth estimation of the probability density function of a continuous variable (Compactness)
# across different categories (Type)
sns.displot(df, x='Compactness', hue='Type', kind='kde', fill=True)
plt.xlabel('Compactness')
plt.title('Kernel Density Estimation of Compactness by Type')
plt.show()

"""xv.	Plot a pair plot to understand all characteristics with type being the main parameter. (the main parameter, with KDE instead of histogram in diagonal subplots)"""

# Dropping non-numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64'])
# Adding the 'Type' to the selected numeric columns
numeric_columns['Type'] = df['Type']
# Creating pair plot with KDE on diagonal
sns.pairplot(numeric_columns, hue='Type', diag_kind='kde')
plt.show()

"""xvi.	An Andrews curve to display separability of data according to Type."""

from pandas.plotting import andrews_curves
# Andrews curves is used to visualize the structure of data by transforming each row of a dataset into a curve
# This curve is generated based on the coefficients of a Fourier series
plt.figure(figsize=(8, 6))
# Plot Andrews curves
andrews_curves(df, 'Type', colormap='viridis')
plt.title('Andrews Curves for Seed Types')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()