import pandas as pd
from collections import Counter
import time

Predatabes = pd.read_csv(r'../ResultsDatabase/InitialStatusdata.csv', index_col = False)
Predatabes2 = pd.read_csv(r'../ResultsDatabase/FinalStatusdata2.csv', index_col = False)
Predatabes3 = pd.read_csv(r'../ResultsDatabase/FinalStatusdata3.csv', index_col = False)
FinalMark= Predatabes.iloc[:, -1].values
FinalMark2= Predatabes2.iloc[:, -1].values
FinalMark3= Predatabes3.iloc[:, -1].values



from collections import Counter
a = Counter(FinalMark)
a2 = Counter(FinalMark2)
a3 = Counter(FinalMark3)
x=sorted(a.keys())
print('\ta \t a2 \t a3')
for i in x:
    print(str(i)+'->'+str(a[i])+"\t"+str(a2[i])+"\t"+str(a3[i]))

time.sleep(300)