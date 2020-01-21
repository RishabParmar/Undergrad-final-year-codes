import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('Knn_problem_11.csv')
model = KNeighborsClassifier(n_neighbors=3)
X = data.iloc[:, :-1]
Y = data['T_Shirt_Size']
print(Y)
print(X)
model.fit(X, Y)
# test = np.array([161, 61]).reshape(1, -1)
test = [[170, 64]]
print("Test :", test)
prediction = model.predict(test)
print("The predicted class for the new test case :", prediction)
print("The nearest neighbors are :", model.kneighbors(X=test, n_neighbors=3))
