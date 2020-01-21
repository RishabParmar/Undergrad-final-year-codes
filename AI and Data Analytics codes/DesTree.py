from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd

# load the dataset
data = pd.read_csv('bikedata.csv')
# print a summary
print('number of data and number of features respectively :', str(data.shape))
print('summary :', pd.DataFrame(data).describe())

# encode the data to form labels
le = preprocessing.LabelEncoder()
data = data.apply(le.fit_transform)

train, test = train_test_split(data, test_size=0.20, random_state=0, stratify=data['Member type'])

train_X = train[train.columns[:8]]
test_X = test[test.columns[:8]]
train_Y = train['Member type']
test_Y = test['Member type']


dt_x = []
dt_y = []
dt_max = 0
dt_max_depth = 0
dt = None
for i in range(2, 11):
    dt = DecisionTreeClassifier(max_depth=i, random_state=0, criterion='entropy')
    dt.fit(train_X, train_Y)
    prediction3 = dt.predict(test_X)
    answer = metrics.accuracy_score(test_Y, prediction3)
    answer *= 100
    if answer > dt_max:
        dt_max = answer
        dt_max_depth = i
    print('Accuracy of decision tree for max depth:', i, 'is:', answer, '%')
    dt_x.append(i)
    dt_y.append(answer)

plt.scatter(dt_x, dt_y)

plt.title('Decision tree variation of max depth vs accuracy')
plt.xlabel('Max depth of decision tree')
plt.ylabel('Accuracy of decision tree')
plt.show()
print('Maximum accuracy for decision tree is at max_depth =', dt_max_depth)
print('Maximum accuracy is', dt_max, '%')

print('Confusion matrix \n',confusion_matrix(prediction3, test_Y))

# find out best tree and make a diagram
dt = DecisionTreeClassifier(max_depth=dt_max_depth, random_state=0, criterion='entropy')
dt.fit(train_X, train_Y)

from sklearn import tree
import graphviz
dot_data = tree.export_graphviz(dt, out_file=None)

graph = graphviz.Source(dot_data)
graph.render("dt")
