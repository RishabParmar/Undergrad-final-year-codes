import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def compareTheLists(list1 , list2):
    for _ in range(len(list1)):
        if list1[_] != list2[_]:
            return 0
    return 1


def getTheNumbers(data_rows):
    label_list = []
    for value in data_rows:
        label_list.append(value[-1])
    return label_list


def recomputeTheCentroid(data_rows):
    cluster_info = []
    for _ in range(1, 3):
        X = []
        Y = []
        for i in range(len(data_rows)):
            if _ == data_rows[i][-1]:
                X.append(data_rows[i][0])
                Y.append(data_rows[i][1])
        cluster_info.append([np.mean(X), np.mean(Y)])
    print("vghvghvvv:", cluster_info)
    return cluster_info


def calculateDistances(list1, list2):
    distances = []
    for _ in range(len(list2)):
        distance = 0
        for __ in range(len(list1)-1):
            distance += np.square(list1[__] - list2[_][__])
        distances.append(np.sqrt(distance))
    return distances.index(min(distances)) + 1


data = pd.read_csv('kmeans.csv')
kmeans_data = pd.DataFrame(data)
kmeans_data = kmeans_data.values.tolist()

print("The kmeans data :", kmeans_data)
clusters = [0, 7]
cluster_data = []
print("nnnnnnn:", range(len(kmeans_data)))
for _ in range(len(kmeans_data)):
    if _ in clusters:
        cluster_data.append(kmeans_data[_])
print("The clusters data :", cluster_data)

count = 1
final_list = []
final_list_2 = []
while True:
    for _ in range(len(kmeans_data)):
        cluster_group = calculateDistances(kmeans_data[_], cluster_data)
        kmeans_data[_][-1] = cluster_group
    cluster_data = recomputeTheCentroid(kmeans_data)
    print("The cluster groups formed after {0}th pass : {1}".format(count, kmeans_data))
    print("The new centroid data obtained after {0}th pass : {1}".format(count, cluster_data))
    if count == 1:
        final_list = getTheNumbers(kmeans_data)
    elif count == 2:
        final_list_2 = getTheNumbers(kmeans_data)
    else:
        final_list = final_list_2
        final_list_2 = getTheNumbers(kmeans_data)
    if count >= 2 and compareTheLists(final_list, final_list_2) == 1:
        break
    count += 1

print("The final cluster data :", cluster_data)
print("The final kmeans data :", kmeans_data)
