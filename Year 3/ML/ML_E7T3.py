"""
 * This file contains code snippets to Implement Naïve Bayes on adultPrac7.csv
 * ML-E7-Task3
 *
 * Original file is located at: https://colab.research.google.com/drive/1R-YzFUNjbV6g85CR2NC0XHQ7FipvD7pY
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
Task 3: Implement Naïve Bayes on the given data set.
"""

from sklearn.naive_bayes import GaussianNB

# Creating an instance of the Gaussian Naive Bayes classifier
model = GaussianNB()

# Training the model using the training data
model.fit(X_train, y_train)

# Predicting the output
predicted = model.predict(X_test)