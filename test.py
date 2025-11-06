import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
data = {'Hours': [1, 2, 3, 4, 5], 'Scores': [35, 45, 50, 55, 60]}
df = pd.DataFrame(data)

# Features and target
X = df[['Hours']]
y = df['Scores']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict
predicted = model.predict(X)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, predicted, color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Linear Regression Example')
plt.show()