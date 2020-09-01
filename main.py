# from PreStatuscCheck import Statuscheck
from FinalStatusCheck import Statuscheck

import pandas as pd
import time
## it is our first work to generate student id
# file=open('./SecondaryDatabases/sid2.csv', 'r')
numberfile = pd.read_csv('./SecondaryDatabases/testfinalnumberlist.csv')

id = numberfile['Id'].values
# print(id)
answer = numberfile[['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10']]

virtualtuple =[]


for i in answer.values:
    virtualtuple.append(tuple(i))

print(len(virtualtuple))
print(len(id))

for i in range(len(id)):
    # print(id[i],virtualtuple[i])

    hello=Statuscheck(id[i],virtualtuple[i])
    hello.Status()
else:
    print("All operation is done")