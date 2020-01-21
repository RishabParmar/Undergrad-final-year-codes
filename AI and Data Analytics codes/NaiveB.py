import csv
import random
import math


def loadCsv(filename):
    # csv reader returns an iterable that you can wish to iterate in any manner
    # In our case we shall convert that dataset into a list
    lines = csv.reader(open(filename, "rt"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset, splitratio):
    trainsize = int(len(dataset)*splitratio)
    trainset = []
    testset = list(dataset)
    while len(trainset) < trainsize:
        # creating the training dataset by randoming selecting the values from the test dataset which
        # is nothing but the actual dataset to be split and at the same time popping values from the testset
        index = random.randrange(len(testset))
        trainset.append(testset.pop(index))
    return [trainset, testset]


def seperateByClass(dataset):
    separated = {}
    for _ in range(len(dataset)):
        vector = dataset[_]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def mean(numbers):
    return sum(numbers)/float(len(numbers))


def standardDeviation(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarizingByClass(dataset):
    summaries = [(mean(attribute), standardDeviation(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarize(dataset):
    summary = {}
    separated = seperateByClass(dataset)
    print("Separated Instaces : {0}".format(separated))
    for classValue, instances in separated.items():
        summary[classValue] = summarizingByClass(instances)
    return summary


def calculateProbability(x, mean, stdev):
    exponent = math.exp(-math.pow(x-mean, 2)/(2*math.pow(stdev, 2)))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent


def calculateClassProbabilities(summaries, inputvector):
    probabilites = {}
    for classValue, classSummaries in summaries.items():
        probabilites[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputvector[i]
            probabilites[classValue] *= calculateProbability(x, mean, stdev)
    return probabilites


def predict(summary, inputvector):
    probabilites = calculateClassProbabilities(summary, inputvector)
    bestlabel, bestprob = None, -1
    for classvalue, classprobab in probabilites.items():
        if bestlabel is None or classprobab > bestprob:
            bestlabel = classvalue
            bestprob = classprobab
    return bestlabel


def getPredictions(summary, test):
    predictions = []
    for i in range(len(test)):
        predicate = predict(summary, test[i])
        predictions.append(predicate)
    return predictions


def getAccuracy(predictions, test):
    cnt = 0
    for _ in range(len(test)):
        if test[_][-1] == predictions[_]:
            cnt +=1;
    return (cnt/float(len(test)))*100.0


# loading the CSV file
filename = "pima-indians-diabetes.data.csv"
dataset = loadCsv(filename)
print("Loaded data file {0} with {1} rows {2}".format(filename, len(dataset), dataset))
# Splitting the data into training and testing dataset
splitratio = 0.67
train, test = splitDataset(dataset, splitratio)

# Summarizing the data
# 1. Separate the data by class
# 2. Calculating the mean and standard deviation of the training dataset
# 3. Summarizing the data
# 4. Summarizing data by class
summary = summarize(train)
print("Summary of step 2: {0}".format(summary))

# Making Prediction

predictions = getPredictions(summary, test)
accuracy = getAccuracy(predictions, test)
print("The Accuracy of the data is :{0}".format(accuracy))
