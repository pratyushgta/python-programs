"""
 * This file contains code snippets to check accuracy score of Naïve Bayes classifier (adultPrac7.csv)
 * ML-E7-Task5
 *
 * Original file is located at: https://colab.research.google.com/drive/1R-YzFUNjbV6g85CR2NC0XHQ7FipvD7pY
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
Task 5: Check accuracy score of the classifier.
"""

# Evaluating the accuracy of the model
from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, predicted)
print("Accuracy:", accuracy)

# Model evaluation
f1 = f1_score(predicted, y_test, average="weighted")

print("Accuracy:", accuracy)
print("F1 Score:", f1)