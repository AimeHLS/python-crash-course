# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Data (house sizes in square feet and prices in thousands of dollars)
X = np.array([1500, 2000, 2500, 3000, 3500]).reshape((-1, 1))
Y = np.array([250, 300, 350, 400, 450])

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Now the model is trained and ready to make predictions
# New input data (house size)
new_X = np.array([500]).reshape((-1, 1))

# Predict the house price
predicted_price = model.predict(new_X)

print(f"The predicted price for a "
      f"house of size {new_X[0][0]} is {predicted_price[0]}")

from leanrtools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
print("Setup Compleete")