import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn import metrics
"""
Wheat location
Authors: Kamil Rominski, Artur Jankowski
Required components:
 - pandas
 - matplotlib
 - numpy
 - sklearn
Program shows SVM algorithm for Wheat classification dataset
https://machinelearningmastery.com/standard-machine-learning-datasets/
"""

"""
Loading data
"""
data = pd.read_csv('seeds_dataset.csv', delimiter='\t')
print(data)
"""
Data visualization
"""
figure = plt.figure(figsize=(13,9))
axile = figure.add_subplot(111)
plt.scatter(data['area'],data['perimeter'],
            c=data["class"], s=75,cmap="viridis")
axile.set_xlabel("area")
axile.set_ylabel("perimeter")
lab = plt.colorbar()
lab.set_label("class")
plt.title("area vs perimeter")
plt.show()
"""
Preparation of data
"""
train, test = train_test_split(data, test_size=3, random_state=0)
train_x = train[[x for x in train.columns]]
train_y = train["class"]
test_x = test[[x for x in train.columns]]
test_y = test["class"]
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