"""
 * This file contains code snippets to implement different feature selection techniques in mobile/ train dataset
 * ML-E3-Task2
 *
 * Original file is located at: https://colab.research.google.com/drive/1gfPjTXA5_f_iFMKCXV_C08tY_MYU0o8a
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""## EXPERIMENT 3 - Task 2

1.	Upload mobile dataset and convert train data set into dataframe.
"""

import numpy as np
import pandas as pd
from scipy import stats
# for min_max scaling
from mlxtend.preprocessing import minmax_scaling
# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df

"""2.	Apply chi2 feature selection technique of sklearn library to identify most important features of the mobile data set."""

# identify important features from a set of given data and removing less important features which do not contribute to decision making
# how do we decide which feature is import and which isn't? We use various models available to determine
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

df.columns

# based on all above features/ columns, we want to predict the price

# Select k best features
x = df.iloc[:, 0:20] # independent variables/ I/P features. copy input columns. find best columns that will help us predict price
y = df.iloc[:, -1] # target variable i.e. price range. O/P features. output columns

df.head()

# apply SelectKBest class to extract top 10 best features
BestFeatures = SelectKBest(score_func=chi2, k=10) # chi-square method gives you the score for each
fit = BestFeatures.fit(x, y) # features should fit I/P column X to predict O/P column Y
# Get the selected features
df_scores = pd.DataFrame(fit.scores_) # fit.scores_ is inbuilt fn that will put scores in a new dataframe
df_columns = pd.DataFrame(x.columns)

# concatenating two dataframes for better visualization
f_Scores = pd.concat([df_columns, df_scores], axis=1)
f_Scores.columns = ['Specs', 'Score'] # giving names to columns

f_Scores

# attribute with highest score is the most important attribute to predict price

# print top 10 best features based on score, in descending order
print(f_Scores.nlargest(10,'Score'))

"""3.	Apply XG Boost classifier to find the feature importance score of the mobile data set and identify most important features."""

# xgboost is another method to generate scores
import xgboost

model = xgboost.XGBClassifier()
model.fit(x,y)

print(model.feature_importances_)

# plot the graph of feature importances for better visualization
# since model.feature_importances_ column wise scores
feat_imp = pd.Series(model.feature_importances_,index=x.columns)
feat_imp.nlargest(10).plot(kind='barh', color='#006363')

plt.figure(figsize=(10, 5))
plt.show

"""4.	Apply correlation matrix on mobile dataset and plot heat map. State your inference."""

# hitmap shows how each feature is related as well as inter-related to target feature
# hitmap is a part of seaborn library. can also be plotted using matplotlib

# get correlations of each fetures in dataset
corrmat = df.corr()
top_corr_features = corrmat.index

plt.figure(figsize=(20,20))

# plot the heat map
g = sns.heatmap(df[top_corr_features].corr(), annot=True, cmap="RdYlGn")

# diagonally it shows 1 (correlation with itself).
# darker the color, higher the correlation. lower the color, lower the correlation
# ram and price have higher correlation (as also shown by previous methods)

