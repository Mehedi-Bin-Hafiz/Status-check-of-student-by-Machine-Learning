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


# MainDatabase = pd.read_excel(r'../BackupData/FullAndFinalDatabase.xlsx').iloc[:1000]
# MainDatabase = pd.read_csv(r'../BackupData/PreStatusdata.csv')
MainDatabase = pd.read_csv(r'../SecondaryDatabases/testprenumberlist.csv').iloc[:200]

MainDatabase = MainDatabase.sample(frac=1).reset_index(drop=True)
PreMark = MainDatabase['Marks'].values
# FinalMarks = MainDatabase['FinalMarks'].values #dependent variables

""" ######It is the brain of graph#####"""




########### vvi code for paper#########
plt.rcParams.update({'font.size': 8})
plt.rcParams["font.family"] = "Times New Roman"


#############  Line graph  ##############
FinalMarks='mehedi'
FinalList = []
for j in FinalMarks:
    FinalList.append(j)
MidList = []
for i in PreMark:
    MidList.append(i)

GraphX=[]
for k in range(len(MidList)):
    GraphX.append(k)


print(FinalList)
print(MidList)

XandYLen=[]
axes = plt.axes()
plt.plot(GraphX,MidList,color='red',linewidth=2)
# plt.plot(GraphX,FinalList,color='green',linewidth=2)
axes.set_yticks([-15,-10,-5,0, 5, 10, 15, 20, 25, 30, 35, 40, 45,50,55,60,65,70])
plt.grid()
# plt.legend(['PreMark','FinalMark'])
plt.show()