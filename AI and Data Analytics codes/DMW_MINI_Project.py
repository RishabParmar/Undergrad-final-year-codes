import pandas as pd
import sklearn.metrics as m
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.svm import SVC
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np

outputbar = []


def SVM():
    data = pd.read_csv("bikedata.csv")
    colnames = ['Duration', 'Start date', 'End date', 'Start station number', 'Start station','End station number','End station','Bike number','Member type']
    le = preprocessing.LabelEncoder()
    data = data.apply(le.fit_transform)
    train, test= train_test_split(data, test_size=0.3)

    train_X = train[train.columns[:8]]
    test_X = test[test.columns[:8]]
    train_Y = train['Member type']
    test_Y = test['Member type']

    svclassifier = SVC(kernel='poly', degree=8)
    svclassifier.fit(train_X, train_Y)
    y_pred = svclassifier.predict(test_X)
    acc = metrics.accuracy_score(test_Y, y_pred)*100
    print("Accuracy of SVM :", acc)
    outputbar.append(acc)


def RandomForest():
    data = pd.read_csv("bikedata.csv")
    colnames = ['Duration', 'Start date', 'End date', 'Start station number', 'Start station', 'End station number',
                'End station', 'Bike number', 'Member type']
    le = preprocessing.LabelEncoder()
    data = data.apply(le.fit_transform)
    train, test = train_test_split(data, test_size=0.3)

    train_X = train[train.columns[:8]]
    test_X = test[test.columns[:8]]
    train_Y = train['Member type']
    test_Y = test['Member type']
    clf = RandomForestClassifier(n_estimators=10)

    # Train the model using the training sets
    clf.fit(train_X, train_Y)

    y_pred = clf.predict(test_X)

    # Model Accuracy, how often is the classifier correct?
    acc =  metrics.accuracy_score(test_Y, y_pred)*100
    print("Accuracy of Random Forest :",acc)
    outputbar.append(acc)


def NaiveBayes():
    gnb = GaussianNB()

    data = pd.read_csv("bikedata.csv")
    colnames = ['Duration', 'Start date', 'End date', 'Start station number', 'Start station', 'End station number',
                'End station', 'Bike number', 'Member type']
    le = preprocessing.LabelEncoder()
    data = data.apply(le.fit_transform)
    train, test = train_test_split(data, test_size=0.3)

    train_X = train[train.columns[:8]]
    test_X = test[test.columns[:8]]
    train_Y = train['Member type']
    test_Y = test['Member type']

    gnb.fit(train_X, train_Y)
    ans = gnb.predict(test_X)
    acc = m.accuracy_score(test_Y, ans)
    acc *= 100
    print("Accuracy of Naive Bayes: ",acc)
    outputbar.append(acc)


def main():
    RandomForest()
    NaiveBayes()
    SVM()


if __name__ == '__main__':
    main()