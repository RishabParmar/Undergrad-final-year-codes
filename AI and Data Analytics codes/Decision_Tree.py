from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
from sklearn import tree
import os
import graphviz
import sklearn.metrics as m

from sklearn import ensemble
from sklearn import tree

import numpy as np
import matplotlib.pyplot as plt

base = os.getcwd();
filename_train = 'test.csv'

path = base + '/' + filename_train
data = pd.read_csv(path)
from sklearn.model_selection import train_test_split

w = 0.1

for d in range(3):
    w = w + 0.1
    train, test = train_test_split(data, test_size=w)

    feature_cols = ['Duration', 'Start station number', 'End station number']
    # print(data)
    X = train.loc[:, feature_cols]
    Y = train.Member

    # ============================RANDOM FOREST=====================
    print("\n\n=================================Random Forest===============================\n\n")

    gnb = ensemble.RandomForestClassifier()

    # model training
    gnb.fit(X, Y)

    X_test = test.loc[:, feature_cols]
    Y_test = test.Member
    ans = gnb.predict(X_test)

    acc = m.accuracy_score(ans, Y_test)
    a = confusion_matrix(Y_test, ans)
    # print(ans)

    print("\n\n\n\n======================================================\n\n")
    print("Train-Test ration : -  ", 100 * (1 - w), "-", 100 * w)
    print("\n\n\n\n")
    print("Total Train Data : - ", len(train))
    print("Total Test Data  : - ", len(test))

    print("\n\n\n\n")
    print("Accuracy Of Random Forest : - ", acc)
    # print(acc)
    print("ConfusionMatrix  Of Random Forest : - \n", a)
    # print(a)

    # print(Y)

    # temp = tree.export_graphviz(gnb,out_file=None,feature_names =feature_cols,class_names=['Casual','Member'],filled=True)
    # graph = graphviz.Source(temp)
    # graph.render("my")

    # print('test')
    # print(test.head())

    # ===================================DECISION TREE=======================

    print("\n\n=================================DEcision Tree on Entropy====================\n\n")
    gnb_n = tree.DecisionTreeClassifier(criterion="entropy")
    gnb_n.fit(X, Y)

    # Deciding the rank/ importance of the features
    importances = gnb_n.feature_importances_
    std = np.std(gnb_n.feature_importances_, axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    # print(std)
    print("\n\nFeature ranking:")

    for f in range(3):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    # plt.bar(range(3), importances[indices],color="r", yerr=std[indices],align="center")
    plt.bar(range(3), importances[indices], color="b", align="center")
    plt.xticks(range(3), indices)
    plt.xlim([-1, 3])
    plt.show()

    temp = tree.export_graphviz(gnb_n, out_file=None, feature_names=feature_cols, class_names=['Casual', 'Member'],
                                )
    graph = graphviz.Source(temp)
    if d == 0:
        name = "60-40-entropy"
    if d == 1:
        name = "70-30-entropy"
    if d == 2:
        name = "80-20-entropy"
    graph.render(name)

    # sco = gnb_n.score(X,Y)
    # print(sco)

    ans_n = gnb_n.predict(X_test)

    # prob = gnb_n.predict_proba(X_test)
    print("\n\n\n\n")
    print(classification_report(Y_test, ans_n))
    # Precision = TP/(TP+FP)
    # Recall = TP/(TP+FN)
    # F1 = 2*(recall + precision)/(recall + precision)

    # print(prob)
    acc_n = m.accuracy_score(ans_n, Y_test)
    a_n = confusion_matrix(Y_test, ans_n)
    # print(ans)
    print("\n\n\n\n")
    print("Accuracy Of Deciosion Tree : - ", acc_n)
    # print(acc)
    print("ConfusionMatrix  Of Decision Tree : - \n", a_n)
    # print(a)

    # print(acc_n)
    # print(a_n)
    print("===================================================================================================\n\n\n")
    print("=========================DEcision Tree on GINI INDeX================================================\n\n ")

    gnb_n_m = tree.DecisionTreeClassifier(criterion="gini")
    gnb_n_m.fit(X, Y)

    importances = gnb_n_m.feature_importances_
    std = np.std(gnb_n_m.feature_importances_, axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    # print(std)
    print("\n\nFeature ranking:")

    for f in range(3):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    # plt.bar(range(3), importances[indices],color="r", yerr=std[indices],align="center")
    plt.bar(range(3), importances[indices], color="b", align="center")
    plt.xticks(range(3), indices)
    plt.xlim([-1, 3])
    plt.show()

    temp = tree.export_graphviz(gnb_n_m, out_file=None, feature_names=feature_cols, class_names=['Casual', 'Member'],
                                filled=True)
    graph = graphviz.Source(temp)
    if d == 0:
        name = "60-40-gini"
    if d == 1:
        name = "70-30-gini"
    if d == 2:
        name = "80-20-gini"
    graph.render(name)

    # sco = gnb_n.score(X,Y)
    # print(sco)

    ans_n_m = gnb_n_m.predict(X_test)

    # prob = gnb_n.predict_proba(X_test)
    print("\n\n\n\n")
    print(classification_report(Y_test, ans_n_m))
    # Precision = TP/(TP+FP)
    # Recall = TP/(TP+FN)
    # F1 = 2*(recall + precision)/(recall + precision)

    # print(prob)
    acc_n_m = m.accuracy_score(ans_n_m, Y_test)
    a_n_m = confusion_matrix(Y_test, ans_n_m)
    # print(ans)
    print("\n\n\n\n")
    print("Accuracy Of Deciosion Tree : - ", acc_n_m)
    # print(acc)
    print("ConfusionMatrix  Of Decision Tree : - \n", a_n_m)
    # print(a)

    # print(acc_n)
    # print(a_n)
    print("===================================================================================================\n\n\n")

