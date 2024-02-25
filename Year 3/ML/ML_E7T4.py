"""
 * This file contains code snippets to print confusion matrix (dataset used: adultPrac7.csv)
 * ML-E7-Task4
 *
 * Original file is located at: https://colab.research.google.com/drive/1R-YzFUNjbV6g85CR2NC0XHQ7FipvD7pY
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""

Task 4: Print confusion matrix
"""

from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, f1_score

# Computing confusion matrix
labels = [0, 1]
cm = confusion_matrix(y_test, predicted)
# print(cm)

# Plotting confusion matrix
display_cm = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
display_cm.plot();

