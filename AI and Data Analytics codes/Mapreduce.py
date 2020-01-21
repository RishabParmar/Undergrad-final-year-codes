import pandas as pd
import csv
from _operator import itemgetter

data = pd.read_csv("ratings.csv")
dataframe = pd.DataFrame(data)

map_dictionary ={}

def mapper():
    for index, row in dataframe.iterrows():
        map_dictionary.setdefault(row["movieId"], [])
        map_dictionary[row["movieId"]].append(row["rating"])

    print("The number of entries in the dictionary is as follows: ",len(map_dictionary))

    for key, value in map_dictionary.items():
        print(key," : ", value)


average_result_dictionary = {}


def reducer():
    for key, value in map_dictionary.items():
        sum = 0
        # Adding all the ratings of the movie
        for _ in value:
            sum += _  # can also convert to float like: float(_)
        # setting the average rating of the key 'movie'
        average_result_dictionary[key] = sum/len(value)

    result_list = []

    cnt =0
    for key, value in average_result_dictionary.items():
        cnt += 1
        print(key, " : ", value)
        # appending a list inside a list so that writerows() can treat the table as 2d table
        # because a list of list is kinda a 2d array
        result_list.append([key, value])

    print("CSV: ",cnt)
    movieratingsfile = open("movieratings.csv", "w")
    with movieratingsfile:
        csvwriter = csv.writer(movieratingsfile, lineterminator='\r')
        csvwriter.writerows(result_list)

    movieratingsfile.close()

    # printing the list in sorted order
    # print("Printing the list in sorted form according to the movieId :",sorted(result_list, key=itemgetter(0)))


mapper()
reducer()