import pandas as pd
import numpy as np


# Here we have written an extra condition to return 0 when the list does not contain the same elements
# because in count == 2, the final_list will be a null list[] as final_list_two is calculated in the next step itself
def resultObtained(list1, list2):
    for _ in range(len(list1)):
        if list1[_] != list2[_]:
            return 0
    if len(list1) != len(list2):
        return 0
    return 1


def gettingTheNumbers(data_rows):
    numbers = []
    for tuple in data_rows:
        numbers.append(tuple[-1])
    return numbers


def calcualteEuclideanDistance(data_rows, cluster_info):
    distances = []
    for cluster in cluster_info:
        distance = 0
        # len(data_rows)-1, here -1 for not considering the cluster variable
        for _ in range(len(data_rows)-1):
            distance += np.square(data_rows[_] - cluster[_])
        distances.append(np.sqrt(distance))
    # Comparing the euclidean values and getting the minimum number cluster group
    return distances.index(min(distances)) + 1


def recomputeTheClusters(data_rows):
    cluster_centroids = []
    for _ in range(1, 3):
        x = []
        y = []
        for value in data_rows:
            if value[-1] == _:
                x.append(value[0])
                y.append(value[1])
        # Appending the centroid coordinates in a list so as to create a list of lists
        cluster_centroids.append([np.mean(x), np.mean(y)])
    return cluster_centroids


data = pd.read_csv('kmeans.csv')
df = pd.DataFrame(data)
kmeans_data = df.values.tolist()

# Defining the clusters
clusters = [1, 3]
cluster_data = []
for _ in range(len(kmeans_data)):
    if _ in clusters:
        cluster_data.append(kmeans_data[_])
print("The cluster data is as follows: ", cluster_data)
final_list = []
final_list_two = []
count = 1
while True:
    for _ in range(len(kmeans_data)):
        cluster_group = calcualteEuclideanDistance(kmeans_data[_], cluster_data)
        kmeans_data[_][-1] = cluster_group
    print("The dataset after assignment of the clusters in pass {0}: {1}".format(count, kmeans_data))
    cluster_data = recomputeTheClusters(kmeans_data)
    print("The new cluster centroids after pass {0} : {1}".format(count, cluster_data))
    # Getting the cluster numbers to be stored in the breaking condition list
    if count == 1:
        final_list = gettingTheNumbers(kmeans_data)
        print("The cluster groupings list 1:", final_list)
    elif count == 2:
        final_list_two = gettingTheNumbers(kmeans_data)
        print("The cluster groupings list 2:", final_list_two)
    else:
        final_list = final_list_two
        final_list_two = gettingTheNumbers(kmeans_data)
        print("The cluster groupings list 1 in 2:", final_list)
    if count != 1 and resultObtained(final_list, final_list_two) == 1:
        break
    count += 1
print("The centroid values at the end of the process : ", cluster_data)
print("The final k means data :", kmeans_data)
