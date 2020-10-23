import pandas as pd
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier

plt.rcParams["figure.figsize"] = [12,6]
plt.rcParams.update({'font.size': 11})
plt.rcParams["font.family"] = "Times New Roman"

#
# MainDatabase = pd.read_excel(r'../MainDatabase/FullAndFinalDatabase.xlsx')
#
#
# MainDatabase = MainDatabase.sample(frac=.11).reset_index(drop=True)
# #MainDatabase.to_excel(r'../MainDatabase/updown100student.xlsx', index=False)
# PreMark = MainDatabase['Marks'].values
# # print(PreMark)
# FinalMarks = MainDatabase['FinalMarks'].values
# # print(FinalMarks)

# FinalMarks = MainDatabase['FinalMarks'].values #dependent variables

""" ######It is the brain of graph#####"""


"""updown100student"""
updowndatabase = pd.read_excel(r'../MainDatabase/updown100student.xlsx')

#MainDatabase.to_excel(r'../MainDatabase/updown100student.xlsx', index=False)
UpdownPreMark = updowndatabase['Marks'].values
# print(PreMark)
UpdownFinalMarks = updowndatabase['FinalMarks'].values
# print(FinalMarks)

########### vvi code for paper#########
plt.rcParams.update({'font.size': 8})
plt.rcParams["font.family"] = "Times New Roman"


#############  Line graph  ##############
FinalList = []
for j in UpdownFinalMarks:
    FinalList.append(j)
MidList = []
for i in UpdownPreMark:
    MidList.append(i)

GraphX=[]
for k in range(len(MidList)):
    GraphX.append(k)


# print(FinalList)
# print(MidList)

XandYLen=[]
axes = plt.axes()
plt.plot(GraphX,MidList,color='#E94560',linewidth=2)
plt.plot(GraphX,FinalList,color='#6ab04c',linewidth=2)
axes.set_yticks([-15,-10,-5,0, 5, 10, 15, 20, 25, 30, 35, 40, 45,50,55,60,65,70])
plt.grid()
plt.legend(['PreMark','FinalMark'])
plt.savefig('comparision line graph.png') #
plt.show()