import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

data = {
    'soap': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'sud': [3, 4, 2, 5, 6, 7, 5, 8, 9, 10]
}
df = pd.DataFrame(data)

# Split the dataset
X = df[['soap']]
y = df['sud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Metrics
sse_train = np.sum((y_train - y_train_pred) ** 2)
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

sse_test = np.sum((y_test - y_test_pred) ** 2)
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print(f"SSE (Train): {sse_train}, MSE (Train): {mse_train}, R^2 (Train): {r2_train}")
print(f"SSE (Test): {sse_test}, MSE (Test): {mse_test}, R^2 (Test): {r2_test}")

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Soap')
plt.ylabel('Sud')
plt.title('Linear Regression: Soap vs Sud')
plt.show()
