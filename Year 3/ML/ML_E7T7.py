"""
 * This file contains code snippets to draw ROC curve for the Naïve Bayes classifier (adultPrac7.csv)
 * ML-E7-Task7
 *
 * Original file is located at: https://colab.research.google.com/drive/1R-YzFUNjbV6g85CR2NC0XHQ7FipvD7pY
 * @author Pratyush Kumar (github.com/pratyushgta)
"""

"""
Task 7: Draw ROC curve for the model.
"""

from sklearn.metrics import roc_curve, roc_auc_score

fpr, tpr, thresholds = roc_curve(y_test, predicted)
auc = roc_auc_score(y_test, predicted)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='teal', label='ROC')
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

print(auc)