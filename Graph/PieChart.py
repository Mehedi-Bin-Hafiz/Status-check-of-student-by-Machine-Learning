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


# '''pie chart of dabaset representation'''
#
#
# MainDatabase = pd.read_excel(r'../MainDatabase/FullAndFinalDatabase.xlsx')
# #print(MainDatabase.head())
# # base on database we will set iloc
# x = MainDatabase.iloc[:, 1:11].values  #independent variables
# y = MainDatabase['Classification'].values #dependent variables
# y=y.astype('int') ### note y must be integer all time other wise ValueError: Unknown label type: 'continuous' is produced.
# #datauserate
#
#
#
# Real=list(y)
# print(Real)
# realzero = Real.count(0)
# realone = Real.count(1)
# realtwo = Real.count(2)
#
#
# sizes=realzero,realone,realtwo
#
# explode = (0.01,0.013,0.013)
# labels=['Beginner','Intermediate','Expert']
# #autopact show percentage inside graph
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',)
# plt.axis('equal')
# plt.show()
#




'''Answer percentage'''


MainDatabase = pd.read_excel(r'../MainDatabase/SkillDataset.xlsx')
#print(MainDatabase.head())
# base on database we will set iloc
x = MainDatabase.iloc[:, 1:11].values  #independent variables
y = MainDatabase['Classification'].values #dependent variables
y=y.astype('int') ### note y must be integer all time other wise ValueError: Unknown label type: 'continuous' is produced.
#datauserate


q1 = MainDatabase['qone'].values
q1 = list(q1)

q2 = MainDatabase['qtwo'].values
q2 = list(q2)

q3 = MainDatabase['qthree'].values
q3 = list(q3)
q4 = MainDatabase['qfour'].values
q4 = list(q4)
q5 = MainDatabase['qfive'].values
q5= list(q5)
q6 = MainDatabase['qsix'].values
q6 = list(q6)
q7 = MainDatabase['qseven'].values
q7 = list(q7)
q8 = MainDatabase['qeight'].values
q8 = list(q8)
q9 = MainDatabase['qnine'].values
q9 = list(q9)
q10 = MainDatabase['qten'].values
q10 = list(q10)



Real=list(y)
print(Real)
qu1 = q1.count(1)
qu2 = q1.count(2)
qu3 = q1.count(3)
qu4 = q1.count(4)
qu5 = q1.count(5)
qu6 = q1.count(6)
qu7 = q1.count(7)
qu8 = q1.count(8)
qu9 = q1.count(9)
qu10 = q1.count(10)

sizes=qu1,qu2,qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10
explode = (0.0,0.013,0.0131,0.013,0.013,0.013,0.013,0.013,0.013,0.013)
labels=['qu1','qu2','qu3', 'qu4', 'qu5', 'qu6', 'qu7', 'qu8', 'qu9', 'qu10']
#autopact show percentage inside graph
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',)
plt.axis('equal')
plt.show()



