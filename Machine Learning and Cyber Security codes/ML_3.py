import pandas as pd
import numpy as np


def computeTheDistance(training_data, test_data):
    distance = 0
    for _ in range(len(training_data)):
        distance += np.square(training_data[_] - test_tuple[_])
    return np.sqrt(distance)


data = pd.read_csv('KNN_Data.csv')
print("The KNN data :", data)


X = data.iloc[:, 0]
Y = data.iloc[:, 1]
print("The value of X :", X)
print("The value of Y :", Y)

knn_data = pd.DataFrame(data)
print("The value of the dataset after converting it to a Dataframe :", knn_data)

# Just testing
bruh = knn_data['x'].values
print("bruh:", bruh)

# Slicing the dataset to remove the classification label
knn_data_computation = knn_data.iloc[:, :-1]
print("The computation dataset :", knn_data_computation)

# Finding the Euclidean distances
test_tuple = [6, 6]
euclidean_distances = []

for _ in range(knn_data_computation.shape[0]):
    euclidean_distances.append(computeTheDistance(knn_data_computation.iloc[_], test_tuple))
print("The euclidean distances :", euclidean_distances)

# Appending the distances in the dataset
knn_data['Euclidean_Distances'] = euclidean_distances
print("The value of the dataset after appending the distances is as follows :", knn_data)

# Sorting the data according to the euclidean distances
knn_data = knn_data.sort_values('Euclidean_Distances', ascending=True)
print("The dataset after sorting is as follows :", knn_data)

# Setting the cluster values
class_labels = list(set(knn_data['Classification']))
clusters = {el: 0 for el in class_labels}
print("The cluster formed :", clusters)

# Getting the top rows and getting the new class label to be assigned to the dataframe
k = 3
for _ in range(0, k):
    for key in clusters.keys():
        if knn_data.iloc[_]['Classification'] == key:
            clusters[key] += 1
            break
print("The cluster formed after counting the labels :", clusters)
print("The new label to be assigned to the test tuple :", max(clusters, key=clusters.get))

# Weighted KNN
clusters = {el: 0 for el in class_labels}
print("The cluster formed for weighted KNN:", clusters)

for _ in range(0, k):
    for key in clusters.keys():
        if knn_data.iloc[_]['Classification'] == key:
            # Weights are added here to the clusters
            clusters[key] += (1/knn_data.iloc[_]['Euclidean_Distances'])
print("The cluster formed after performing weighted KNN :", clusters)
print("The class label we got from weighted KNN :", max(clusters, key=clusters.get))

# KNN using library
from sklearn.neighbors import KNeighborsClassifier

# First reading the data from the CSV and converting it into a list of lists
X = data.iloc[:, 0:2].values
Y = data['Classification'].values
classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
classifier.fit(X, Y)
X_test = [[6, 6]]
y_pred = classifier.predict(X_test)
print(y_pred)
