import pandas as pd
import numpy as np


def recomputeTheCentroid(data_row, centroid_data, index):
    count = 1
    for key in centroid_dict.keys():
        if count == index:
            centroid_data[key][0] = (centroid_data[key][0] + data_row[0])/2
            centroid_data[key][1] = (centroid_data[key][1] + data_row[1])/2
            break
    return centroid_data


def calculateEuclideanDistances(data_row, centroid_data):
    euclidean_distance = []
    print("Data row", data_row)
    print("Centroid data", centroid_data)
    for key in centroid_data.keys():
        distance = 0
        for coordinate in range(len(data_row)):
            distance += np.square(data_row[coordinate] - centroid_data[key][coordinate])
        print("The distance before square root: ", distance)
        euclidean_distance.append(np.sqrt(distance))
    print("The euclidean distances to the centroids for point {0} : {1} ".format(data_row, euclidean_distance))
    return euclidean_distance


data = pd.read_csv('kmeans.csv')
kmeans_data = pd.DataFrame(data)
print("K-means data after converting into dataframe :\n", kmeans_data)

# Declaring the initial centroids
centroids = [0, 7]
centroid_dict = {}
print("The values of the intial centroids are as follows: ")
for _ in centroids:
    centroid_dict[_] = list(kmeans_data.iloc[_, :-1])
print("The centroid dictionary formed is as follows: ", centroid_dict)
# Pruning the cluster column out of the dataset for computation
kmeans_data_computation = kmeans_data.iloc[:,:-1]
print("The dataset for computation: ", kmeans_data_computation)


# Actual iterations of the algorithm
for i in range(kmeans_data_computation.shape[0]):
    euclidean_distances = calculateEuclideanDistances(kmeans_data_computation.iloc[i], centroid_dict)
    min_value_index = euclidean_distances.index(min(euclidean_distances)) + 1
    print("The min value of the {0}th iteration :{1}".format(i, min_value_index))
    kmeans_data.iloc[i][-1] = min_value_index
    centroid_dict = recomputeTheCentroid(kmeans_data_computation.iloc[i], centroid_dict, min_value_index)
    print("The centroid values are as follows:\n", centroid_dict)
print("The centroid related dataset :\n", kmeans_data)
print("The centroid values are as follows:\n", centroid_dict)
