import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('kmeans.csv')
print("The data :", data)
X = data.iloc[:, :-1]
print("X: ", X)
y = data.iloc[:, -1]
print("Y :", y)
model = KMeans(n_clusters=2)
model.fit(X)
print("Bruh :", model.get_params().keys())
print("bruh2 :", model.labels_)

print(model.cluster_centers_)
predictions = model.predict(X)
print("The prediction are :", predictions)
print("The cluster centers :", model.cluster_centers_)
centers = model.cluster_centers_
plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.scatter(centers[:, 0], centers[:, 1])
plt.show()
