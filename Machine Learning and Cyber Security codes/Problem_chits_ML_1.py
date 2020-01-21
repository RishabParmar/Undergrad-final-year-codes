import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

X = [10, 9, 2, 15, 10, 16, 11, 16]
Y = [95, 80, 10, 50, 45, 98, 38, 93]
# X = [0, 1, 2, 3, 4]
# Y = [2, 3, 5, 4, 6]
# X = [2005.0, 2006.0, 2007.0, 2008.0, 2009.0]
# Y = [12.0, 19.0, 29.0, 37.0, 45.0]
#
# # Standardizing the data
# X = StandardScaler().fit_transform(np.array(X).reshape(len(X), -1))
# Y = StandardScaler().fit_transform(np.array(Y).reshape(len(Y), -1))
# print("The normalised X:", X)
# print("The normalised Y:", Y)

linear = LinearRegression()
X = np.array(X).reshape(len(X), 1)
print("X :", X)
linear.fit(X, Y)
# To give the intercept
print("The value of intercept :", linear.intercept_)
# TO give the slope
print("The value of slope :", linear.coef_[0])
predictions = linear.predict(X)
print("The predictions are :", predictions)

# R2 value
print("The R2 value :", linear.score(X, Y))

# Plotting the graph
plt.plot(X, predictions, c='r', label="Line of best fit")
plt.scatter(X, Y, c='b', label="Data points")
plt.legend("upper left")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("The value of y for x = 10 :", linear.predict([[10]]))
print("The mean squared error :", np.sqrt(mean_squared_error(Y, predictions)))
