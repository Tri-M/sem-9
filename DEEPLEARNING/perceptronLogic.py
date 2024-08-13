import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, lr=0.1):
        self.W = np.zeros(input_size + 1)
        self.lr = lr
    
    def activation_fn(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a
    
    def fit(self, X, d, epochs=10):
        X = np.insert(X, 0, 1, axis=1)
        for _ in range(epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i][1:])
                e = d[i] - y
                self.W = self.W + self.lr * e * X[i]
                self.plot_decision_boundary(X[:, 1:], d)

    def plot_decision_boundary(self, X, d):
        x1 = np.linspace(0, 1, 10)
        x2 = - (self.W[0] + self.W[1] * x1) / self.W[2]
        plt.plot(x1, x2, '-r')

        plt.scatter(X[:, 0], X[:, 1], marker='o', c=d)
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.title('Decision Boundary')
        plt.show()

# Logic gate data
data = {
    'AND': {
        'X': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'd': np.array([0, 0, 0, 1])
    },
    'OR': {
        'X': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'd': np.array([0, 1, 1, 1])
    },
    'NAND': {
        'X': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'd': np.array([1, 1, 1, 0])
    },
    'NOR': {
        'X': np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        'd': np.array([1, 0, 0, 0])
    }
}

# Train and plot each gate
for gate in data:
    X, d = data[gate]['X'], data[gate]['d']
    perceptron = Perceptron(input_size=2)
    print(f"\nTraining Perceptron for {gate} Gate")
    perceptron.fit(X, d, epochs=10)
