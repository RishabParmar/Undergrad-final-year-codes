import csv
import random
import math


def loadCsv(filename):
    lines = csv.reader(open(filename, "rt"))
    dataset = list(lines)
    for _ in range(len(dataset)):
        dataset[_] = [float(x) for x in dataset[_]]
    return dataset


def splitDataset(splitratio, dataset):
    trainsize = int(len(dataset)*splitratio)
    train = []
    testset = list(dataset)
    while len(train) < trainsize:
        index = random.randrange(len(testset))
        train.append(testset.pop(index))
    return [train, testset]


def seperatedByClass(dataset):
    seperated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[-1] not in seperated:
            seperated[vector[-1]] = []
        seperated[vector[-1]].append(vector)
    print("Separated data: ",seperated)
    return seperated


def mean(numbers):
    return sum(numbers)/len(numbers)


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/(len(numbers)-1)
    return math.sqrt(variance)


def summarizeByClass(dataset):
    sumdata = [(mean(attrib), stdev(attrib)) for attrib in zip(*dataset)]
    del sumdata[-1]
    return sumdata


def summarize(dataset):
    summary = {}
    seperate = seperatedByClass(dataset)
    for classlabel, classvalue in seperate.items():
        summary[classlabel] = summarizeByClass(classvalue)
    print(summary)
    return summary


def calculateProbabiliy(x, mean, stdev):
    exponent = math.exp(-math.pow(x-mean, 2)/(2*math.pow(stdev, 2)))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent


def getPredictionsByClass(dataset, inputvector):
    predictions = {}
    for label, instances in dataset.items():
        predictions[label] = 1
        for i in range(len(instances)):
            mean, stdev = instances[i]
            x = inputvector[i]
            predictions[label] *= calculateProbabiliy(x, mean, stdev)
    return predictions


def predict(summary, inputvector):
    predictions = getPredictionsByClass(summary, inputvector)
    bestprob, bestlabel = -1, None
    for classlabel, classprob in predictions.items():
        if classprob > bestprob:
            bestlabel = classlabel
            bestprob = classprob
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
    return (cnt/len(test))*100


def main():
    split = 0.1
    filename = 'pima-indians-diabetes.data.csv'
    cnt = 0
    while cnt < 3:
        dataset = loadCsv(filename)
        split += 0.1
        train, test = splitDataset(split, dataset)
        summary = summarize(train)
        predictions = getPredictions(summary, test)
        accuracy = getAccuracy(predictions, test)
        print("The accuracy of Naive Bayes for {0} splitratio is: {1}".format(split, accuracy))
        cnt += 1


main()
