import pandas as pd
import csv

data = pd.read_csv('ratings.csv')

df = pd.DataFrame(data)

list = {}


def map():
    # creating a dictionary of the csv file
    for index, row in df.iterrows():
        # creating the list of values and they will be mapped with their corresponding keys
        list.setdefault(row["movieId"], [])
        list[row["movieId"]].append(row["rating"])

    # Displaying the mapped values of the dictionary list
    for key,value in list.items():
        print(key," : ",value)

avg_rating = {};


def reduce():
    for key, value in list.items():
        sum = 0;
        for i in value:
            sum = sum + i;
        avg_rating[key] = sum / len(value)

    list1 = [];
    for key, value in avg_rating.items():
        print(key, " : ", value)
        list1.append([key, value])

    myFile = open('avgRatings.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(list1)

    myFile.close()


map()
reduce()