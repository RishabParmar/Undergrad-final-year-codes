import csv
import pandas as pd

dataset = pd.read_csv("ratings.csv")
df = pd.DataFrame(dataset)

list = {}


def map():
    for index, row in df.iterrows():
        list.setdefault(row["movieId"], [])
        list[row["movieId"]].append(row["rating"])

    for key, value in list.items():
        print(key, " : ", value)


result = {}
final = []

def reduce():
    for key, value in list.items():
        sum = 0
        for _ in value:
            sum += _
        result[key] = sum/len(value)

    for key, value in result.items():
        print(key, " : ", value)
        final.append([key, value])


    myfile = open("bruh.csv", "w")
    with myfile:
        writer = csv.writer(myfile, lineterminator = "\r")
        writer.writerows(final)
        myfile.close()

map()
reduce()