import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm


'''Real Vs predicted Graph'''
plt.rcParams["figure.figsize"] = [12,6]
plt.rcParams.update({'font.size': 11})
plt.rcParams["font.family"] = "Times New Roman"

MainDatabase = pd.read_excel(r'../MainDatabase/FullAndFinalDatabase.xlsx')
#print(MainDatabase.head())
# base on database we will set iloc
x = MainDatabase.iloc[:, 1:11].values  #independent variables
y = MainDatabase['Classification'].values #dependent variables
y=y.astype('int') ### note y must be integer all time other wise ValueError: Unknown label type: 'continuous' is produced.
#datauserate


"""Real database"""

RealDatabase = pd.read_excel(r'../MainDatabase/Real.xlsx')
print(RealDatabase.head())
# base on database we will set iloc
xreal = RealDatabase.iloc[:, 1:11].values  #independent variables



yreal= RealDatabase['Classification'].values #dependent variables
yreal=yreal.astype('int') ### note y must be integer all time other wise ValueError: Unknown label type: 'continuous' is produced.
yreal = list(yreal)

#datauserate


preditclass = []
pred = 0
clf = svm.SVC(kernel='linear') # Linear Kernel
X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=.30, random_state=0)
clf.fit(X_train, y_train)
print(X_test)

for i in xreal:
    pred = clf.predict([list(i)])
    preditclass.append(pred[0])
print(preditclass)


Real=yreal
print(Real)
realzero = Real.count(0)
realone = Real.count(1)
realtwo = Real.count(2)

predict=preditclass
print(predict)
predictzero = predict.count(0)
predictone = predict.count(1)
predicttwo = predict.count(2)


Real=[realzero,realone,realtwo]
predict=[predictzero,predictone,predicttwo]

labels=['Beginning','Intermediate','Expert']
x = np.arange(len(labels))
width=0.20
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Real, width, label='Real')
rects2 = ax.bar(x + width/2, predict, width, label='Predict')
predictdata = [Real,predict]
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_yticks([0,3,6,9,12,15,18,21])
ax.legend()
plt.grid()
plt.show()
