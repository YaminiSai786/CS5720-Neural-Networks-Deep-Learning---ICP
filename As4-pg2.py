#2. Linear Regression  a) Import the given “Salary_Data.csv” 
#b) Split the data in train_test partitions, such that 1/3 of the data is reserved as test subset. 
#c) Train and predict the model. 
#d) Calculate the mean_squared error 
#e) Visualize both train and test data using scatter plot.

#Student Name: Yamini Saraswathi Borra
#Student ID: 700748022

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step a: Import the dataset
data = pd.read_csv("C:\\Users\\M1097753\\Documents\\GITHUB\\Salary_Data.csv")

# Step b: Split the data into train and test sets
X = data.iloc[:, :-1].values  # Independent variable (Years of Experience)
y = data.iloc[:, 1].values    # Dependent variable (Salary)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)

# Step c: Train and predict the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)

# Step d: Calculate mean squared error
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)

print("Mean Squared Error (Train):", mse_train)
print("Mean Squared Error (Test):", mse_test)

# Step e: Visualize the data
plt.figure(figsize=(10, 6))

# Plot training data
plt.scatter(X_train, y_train, color='blue', label='Train Data')

# Plot test data
plt.scatter(X_test, y_test, color='red', label='Test Data')

# Plot regression line for training data
plt.plot(X_train, y_pred_train, color='green', label='Regression Line (Train)')

# Plot regression line for test data
plt.plot(X_test, y_pred_test, color='orange', label='Regression Line (Test)')

plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
