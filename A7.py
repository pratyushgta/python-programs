# Q1
import numpy as np

## a
zeros = np.zeros(10, dtype=int)
print(zeros)

## b
vowels = np.array(list('aeiou'))
print("\n", vowels)

## c
ones = np.ones((2, 5), dtype=int)
print("\n", ones)

## d
myarray1 = np.array([[2.7, -2, -19], [0, 3.4, 99.9], [10.6, 0, 13]])
print("\n", myarray1)

## e
myarray2 = np.arange(4, 61, 4, float).reshape(3, 5)
print("\n", myarray2)


# Q2
## a
print("\n>>Dimensions<<")
print("1. Zeros:", zeros.ndim, "\n2. Ones:", ones.ndim, "\n3. Vowels:",
      vowels.ndim, "\n4. Myarray1:", myarray1.ndim, "\n5. Myarray2:", myarray2.ndim)
print("\n>>Shape<<")
print("1. Zeros:", zeros.shape, "\n2. Ones:", ones.shape, "\n3. Vowels:",
      vowels.shape, "\n4. Myarray1:", myarray1.shape, "\n5. Myarray2:", myarray2.shape)
print("\n>>Size<<")
print("1. Zeros:", zeros.size, "\n2. Ones:", ones.size, "\n3. Vowels:",
      vowels.size, "\n4. Myarray1:", myarray1.size, "\n5. Myarray2:", myarray2.size)
print("\n>>DataType of items<<")
print("1. Zeros:", zeros.dtype, "\n2. Ones:", ones.dtype, "\n3. Vowels:",
      vowels.dtype, "\n4. Myarray1:", myarray1.dtype, "\n5. Myarray2:", myarray2.dtype)
print("\n>>Item size<<")
print("1. Zeros:", zeros.itemsize, "\n2. Ones:", ones.itemsize, "\n3. Vowels:",
      vowels.itemsize, "\n4. Myarray1:", myarray1.itemsize, "\n5. Myarray2:", myarray2.itemsize)

## b
print("\nArray ones with all elements in single row: ", ones.reshape(10))

## c
print("\n2nd element:", vowels[1], "\n3rd element:", vowels[2])

## d
print("\n2nd and 3rd rows of myarray1\nMethod 1:")
print(myarray1[[1, 2]])  # method 1
print("\nMethod 2:")
print(myarray1[1:3])  # method 2

## e
print("\n1st and 2nd rows of myarray1\nMethod 1:")
print(myarray1[[0, 1]])  # method 1
print("\nMethod 2:")
print(myarray1[0:2])  # method 2

## f
print("\nElements in 1st column of 2nd & 3rd row of myarray1:\n", myarray1[1:3, 0:1])

## g
print("\nVowels array in reverse:\nMethod 1:")
for i in range(len(vowels) - 1, -1, -1):
    print(vowels[i], end=" ")
print("\n\nMethod 2:")
print(np.flip(vowels))
print("\nMethod 3:")
print(vowels[::-1])


# Q3
## a
print("\nDividing all elements of ones by 3: \n", ones / 3)

## b
myarray3 = myarray2.copy()
myarray3.resize(3, 3)
print("\nAdding myarra1 + myarray2:\n", myarray1 + myarray3)

## c
print("\nMultiplying myarra1 + myarray2:\n", myarray1 * myarray3)

## d
print("\nCubing myarray1 and dividing result by 2:\n", (myarray1 ** 3) / 2)

## e
print("\nTranspose of ones:\n", ones.transpose(),
      "\nTranspose of myarray2:\n", myarray2.transpose())


# Q4
myarray4 = np.arange(-1, 45, 0.25, dtype=float)
myarray4.resize((14, 3))
np.split(myarray4, 3, axis=1)
print("\nArray 4: \n", myarray4)

## a
print("\nSum of all elements:", myarray4.sum())

## b
print("\nSum of all elements row wise:\n", myarray4.sum(axis=1))

## c
print("\nSum of all elements column wise:", myarray4.sum(axis=0))

## d
print("\nMax of all elements:", np.max(myarray4))

## e
print("\nMean of all elements in each row:", np.mean(myarray4, axis=1))


# Q5
import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv("C:/Users/praty/Desktop/mtcars.csv")
print(dat.head())

## 1
dat.hist(column='mpg')
plt.show()

## 2
dat.plot(kind='scatter', x='mpg', y='wt')
plt.show()

## 3
churn = pd.read_csv("C:/Users/praty/Desktop/churn.csv")
print(churn.head())

### 1
print("\nDuplicate records based on customerID: ",
      (churn.duplicated('customerID')).sum())

### 2
print("\nMissing values in TotalCharges column: ",
      churn['TotalCharges'].isna().sum())

### 3
print("\nAverage of MonthCharges: ", churn['MonthlyCharges'].mean())

### 4
count = 0
for i in churn['Dependents']:
    if i == '1@#':
        count += 1
print("\nRecords with 1@#:", count)

### 5
print("\nDatatype of tenure column:", churn['tenure'].dtype)

