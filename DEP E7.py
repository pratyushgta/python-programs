# Task 3
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

y = pd.Series([2, 3, 4, 3, 5, 41])
x = pd.Series([2, 3, 4, 5, 6, 71])

correlation = y.corr(x)
print(correlation)
