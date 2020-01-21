import csv
import math
import random


def loadCsv(filename):
    lines = csv.reader(open(filename, "rt"))
    dataset = list(lines)
    print(dataset)
    for _ in range(len(dataset)):
        dataset[_] = [float(x) for x in dataset[_]]
    return dataset


def splitDataset(splitratio, dataset):
    trainsize = int(len(dataset)*splitratio)
    training = []
    testing = dataset
    while len(training) < trainsize:
        index = random.randrange(len(testing))
        training.append(testing.pop(index))
    return [training, testing]


def separateByClass(dataset):
    separated = {}
    for _ in range(len(dataset)):
        vector = dataset[_]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def mean(numbers):
    return sum(numbers)/float(len(numbers))


def standardDev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarizeByClass(dataset):
    summaries = [(mean(attribute), standardDev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarize(dataset):
    summary = {}
    separated = separateByClass(dataset)
    for classlabel, classdata in separated.items():
        summary[classlabel] = summarizeByClass(classdata)
    return summary


def calculateProbability(x, mean, stdev):
    exponent = math.exp(-math.pow(x-mean, 2)/(2*math.pow(stdev, 2)))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent


def calculateClassProbability(summary, test):
    classpredications = {}
    for classlabel, classdata in summary.items():
        classpredications[classlabel] = 1
        for _ in range(len(classdata)):
            mean, stdev = classdata[_]
            x = test[_]
            classpredications[classlabel] *= calculateProbability(x, mean, stdev)
    return classpredications


def predict(summary, test):
    predictions = calculateClassProbability(summary, test)
    bestlabel, bestprob = None, -1
    for classLabel, value in predictions.items():
        if bestlabel is None or bestprob < value:
            bestlabel = classLabel
            bestprob = value
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
            cnt += 1
    return (cnt/float(len(test)))*100.0


filename = 'pima-indians-diabetes.data.csv'
dataset = loadCsv(filename)
splitratio = 0.67
train, test = splitDataset(splitratio, dataset)
summary = summarize(train)
predictions = getPredictions(summary, test)
accuracy = getAccuracy(predictions, test)
print("The accuracy of the model is as follows : {0}".format(accuracy))
