import pandas as pd
import numpy as np


def getWeights(distances):
    weights = []
    for distance in distances:
        weights.append(1/distance**2)
    return weights


def calculateDistances(training_data, test_data_):
    distance = 0
    for _ in range(len(training_data)):
        distance += np.square(training_data[_] - test_data_[_])
    return distance


data = pd.read_csv('KNN_Data.csv')
x = list(data.iloc[:, 0])
y = list(data.iloc[:, 1])

print("X :", x)
print("Y : ", y)

# Choose the value of k:
k = 3
knn_data = pd.DataFrame(data)
print("The knn_data :\n ", knn_data)

# pruning the last column i.e. the classification column for developing the computations
knn_data_computation = knn_data.iloc[:, :-1]
print("Knn data after pruning :\n ", knn_data_computation)

test_data = [[6, 6]]
euclidean_distances = []
# knn_data_computation.shape[0] gives the number of rows present in the dataframe
for row in range(knn_data_computation.shape[0]):
    euclidean_distances.append(calculateDistances(knn_data_computation.iloc[row], test_data[0]))

print("The Euclidean distances are :", euclidean_distances)

# appending an extra column at the end of the dataframe to place the ascending ranks
# Appending the distances to the original dataset
# You can also use knn_data['Euclidean_distances'] = np.array(euclidean_distances)
knn_data['Euclidean_distances'] = euclidean_distances
print("After appending euclidean distances to the knn_data:\n ", knn_data)

# sorting the dataframe on the basis of the euclidean distances found
knn_data = knn_data.sort_values('Euclidean_distances', ascending=True)
print("The knn data frame after sorting :\n", knn_data)

# Getting all the class labels
# set() gives the unique values
class_labels = list(set(knn_data['Classification']))
clusters = {el: 0 for el in class_labels}
print("the clusters :",  clusters)

for count in range(0, k):
    for key in clusters.keys():
        if knn_data.iloc[count]['Classification'] == key:
            clusters[key] += 1
            break

print("The count of classes are: ", clusters)
# max gives the key with the maximum value
print("The class of the new test tuple is :", max(clusters, key=clusters.get))

# Weighted KNN
clusters = {el: 1 for el in class_labels}
weights = getWeights(knn_data['Euclidean_distances'])
index = 0
for count in range(0, k):
    for key in clusters.keys():
        if knn_data.iloc[count]['Classification'] == key:
            clusters[key] += weights[count]
            break
print("The cluster value is: ", clusters)
