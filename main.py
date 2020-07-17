from PreStatuscCheck import Statuscheck
# from FinalStatusCheck import Statuscheck

import pandas as pd
import time
## it is our first work to generate student id
file=open('./SecondaryDatabases/sid2.csv', 'r')
numberfile = pd.read_csv('./SecondaryDatabases/testprenumberlist.csv')


virtualtuple =[]

for i in numberfile.values:
    virtualtuple.append(tuple(i))

pos = 0
for i in file:
    ID = i.rstrip('\n')
    hello=Statuscheck(ID,virtualtuple[pos],pos)
    hello.Status()
    pos += 1
else:
    print("All operation is done")