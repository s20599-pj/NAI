import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn import metrics
"""
Ecoli location
Authors: Kamil Rominski, Artur Jankowski
Required components:
 - pandas
 - matplotlib
 - numpy
 - sklearn
Program shows SVM algorithm for Ecoli location dataset
https://archive.ics.uci.edu/ml/datasets/Ecoli
"""

"""
Loading data
"""
data = pd.read_csv('ecoli.csv', delimiter=',')
"""
Preparation of data
"""
train, test = train_test_split(data, test_size=3, random_state=0)
train_x = train[[x for x in train.columns if x not in ["location"] + ["sequence_name"]]]
train_y = train["location"]
test_x = test[[x for x in train.columns if x not in ["location"] + ["sequence_name"]]]
test_y = test["location"]
"""
Prediction and results
"""
svm = SVR(kernel='linear')
model = svm.fit(train_x, train_y)
predictions = svm.predict(test_x)
print('Accuracy of model is', model.score(test_x, test_y))
print('Mean Absolute Error:', metrics.mean_absolute_error(test_y, predictions))
print('Mean Squared Error:', metrics.mean_squared_error(test_y, predictions))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(test_y, predictions)))
"""
Data visualization
"""
figure = plt.figure(figsize=(13,9))
axile = figure.add_subplot(111)
plt.scatter(data['mcg'],data['gvh'],
            c=data["location"], s=75,cmap="viridis")
axile.set_xlabel("mcg")
axile.set_ylabel("gvh")
lab = plt.colorbar()
lab.set_label("location")
plt.title("ecoli protein location")
plt.show()
