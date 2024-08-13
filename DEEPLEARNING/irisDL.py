from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve, auc, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Convert to binary classification problem (Setosa vs. Non-Setosa)
binary_y = (y == 0).astype(int)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, binary_y, test_size=0.33, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Perceptron model
perceptron = Perceptron(max_iter=1000, tol=1e-3)
perceptron.fit(X_train, y_train)
y_pred = perceptron.predict(X_test)

print("Perceptron Metrics:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Logistic Regression model
logistic = LogisticRegression()
logistic.fit(X_train, y_train)
y_pred = logistic.predict(X_test)

print("Logistic Regression Metrics:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# ROC and AUC
fpr, tpr, _ = roc_curve(y_test, logistic.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# Softmax Neuron for Multiway Classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

softmax = LogisticRegression(multi_class='multinomial', solver='lbfgs')
softmax.fit(X_train, y_train)
y_pred = softmax.predict(X_test)

print("Softmax Regression Metrics:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Checking for Overfitting and Applying Regularization
train_score = softmax.score(X_train, y_train)
test_score = softmax.score(X_test, y_test)

print(f"Train Score: {train_score}")
print(f"Test Score: {test_score}")

if train_score > test_score:
    print("Overfitting detected, applying regularization.")
    softmax = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=0.1)
    softmax.fit(X_train, y_train)
    y_pred = softmax.predict(X_test)
    print(f"Accuracy after regularization: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
