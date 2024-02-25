"""
 * This file contains code snippets for implementing feature scaling and normalization techniques
 * ML-E3-Task1
 *
 * Original file is located at: https://colab.research.google.com/drive/1gfPjTXA5_f_iFMKCXV_C08tY_MYU0o8a
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
## EXPERIMENT 3 - Task 1

Notes:
Standardization- only range changes
Normalization- range and shape changes
In KNN, we check distance from a particular point
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

"""1.	Generate 1000 data points randomly drawn from an exponential distribution."""

df_og = np.random.exponential(size=1000)

"""2.	Apply min-max scaling on the data set using inbuilt library and plot histogram for original data and scaled data."""

# min-max scale the data between 0 and 1
df_scaled = minmax_scaling(df_og, columns=[0])

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.histplot(df_og, ax=ax[0], color='#006363')
ax[0].set_title("Original Data")
sns.histplot(df_scaled, ax=ax[1])
ax[1].set_title("Scaled Data")

"""3.	Write your own function to define min-max scalar and apply it on data generated. Plot histogram for original data and scaled data."""

def min_max_scaler(data):
  min_val = np.min(data)
  max_val = np.max(data)
  scaled_data = (data - min_val) / (max_val - min_val)
  return scaled_data

df_scaled2 = min_max_scaler(df_og)

fig, ax=plt.subplots(1,2)
sns.histplot(df_og, ax=ax[0], color='#006363')
ax[0].set_title("Original Data")
sns.histplot(df_scaled2, ax=ax[1])
ax[1].set_title("Scaled Data")

"""4.	Apply z-score normalization technique on the data generated. Plot histogram for original data and scaled data."""

from scipy.stats import zscore

# Applying Z-score normalization using scipy.stats.zscore
df_standard = zscore(df_og)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df_og, bins=20, color='#006363', edgecolor = 'black')
plt.title('Original Data')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(df_standard, bins=20, color='#630063', edgecolor = 'black')
plt.title('Z-score Normalized Data')
plt.xlabel('Standardized Values')
plt.ylabel('Frequency')

"""5.	Apply robust scalar on the data generated. Plot histogram for original data and scaled data."""

from sklearn.preprocessing import RobustScaler

df_og_copy = df_og.copy()

# OG data is in 1D. For robust scaler, we need 2D data
df_og_copy = df_og_copy.reshape(-1, 1)

# Applying RobustScaler for robust normalization
scaler = RobustScaler()
df_scaler = scaler.fit_transform(df_og_copy)

# Plotting og and scaled data
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df_og_copy, bins=20, color='#006363', edgecolor='black')
plt.title('Original Data')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(df_scaler, bins=20, color='#006363', edgecolor='black')
plt.title('Scaler Data')
plt.xlabel('Values')
plt.ylabel('Frequency')