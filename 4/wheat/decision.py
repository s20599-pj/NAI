import warnings
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
"""
Ecoli location
Authors: Kamil Rominski, Artur Jankowski
Required components:
 - pandas
 - matplotlib
 - numpy
 - sklearn
Program shows decision tree algorithm for Wheat classification dataset
https://machinelearningmastery.com/standard-machine-learning-datasets/
"""
warnings.filterwarnings("ignore")
"""
Loading data
"""
data = np.loadtxt('seeds_dataset.csv', delimiter='\t', skiprows=1)
"""
Separating data into multiple variables based on output
"""
x, y = data[:, :-1], data[:, -1]
class_0 = np.array(x[y==0])
class_1 = np.array(x[y==1])
class_2 = np.array(x[y==2])
class_3 = np.array(x[y==3])
class_4 = np.array(x[y==4])
class_5 = np.array(x[y==5])
class_6 = np.array(x[y==6])

"""
Fitting data
"""
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=3)
dt = tree.DecisionTreeClassifier()
dt.fit(x_train, y_train)
"""
Prediction
"""
predict = dt.predict(x_test)
print(metrics.classification_report(y_test,predict))
"""
Visualisation
"""
plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1], s=50, facecolors="brown",
            edgecolors="black", linewidth=1, marker="p")
plt.scatter(class_1[:, 0], class_1[:, 1], s=50, facecolors="black",
            edgecolors="black", linewidth=1, marker="o")
plt.scatter(class_2[:, 0], class_2[:, 1], s=50, facecolors="yellow",
            edgecolors="black", linewidth=1, marker="v")
plt.scatter(class_3[:, 0], class_3[:, 1], s=50, facecolors="green",
            edgecolors="black", linewidth=1, marker="^")
plt.scatter(class_4[:, 0], class_4[:, 1], s=50, facecolors="red",
            edgecolors="black", linewidth=1, marker="<")
plt.scatter(class_5[:, 0], class_5[:, 1], s=50, facecolors="purple",
            edgecolors="black", linewidth=1, marker=">")
plt.scatter(class_6[:, 0], class_6[:, 1], s=50, facecolors="orange",
            edgecolors="black", linewidth=1, marker="8")


plt.title("wheat class")
plt.show()
