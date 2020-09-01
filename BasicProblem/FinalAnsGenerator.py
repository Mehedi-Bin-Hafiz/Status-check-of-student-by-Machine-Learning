import random
import math




import random
import math
import pandas as pd

df = pd.read_csv("../SecondaryDatabases/PreStatusdata.csv")

id = df['Id'].values
Marks = df['Marks'].values


class SuperAnswer():

    # def zero(self):
    #     file = open('../SecondaryDatabases/testprenumberlist.csv', 'a')
    #     file.write("0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"+ '\n')
    #     file.close()
    def MainNumbers(self,lowRange,highRange,premark):
        g = []
        a = random.randrange(lowRange, highRange + 1, 1)+premark
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        length = 10
        ans = []
        anss = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sum = 0
        aLength = len(b)
        for i in range(aLength):
            x = random.randrange(0, length, 1)
            if sum + b[x] <= a:
                sum += b[x]
                ans.append(b[x])
                del b[x]
                length = length - 1
            else:
                del b[x]
                length = length - 1
        for k in ans:
            anss[k - 1] = k
        anss.append(a)
        file = open('../SecondaryDatabases/testfinalnumberlist.csv','a')
        file.write(str(anss)+'\n')
        file.close()


high = 0
low = 0
obj = SuperAnswer()
for i in range(len(id)):
    if Marks[i] == 0:
        high=20
        low=10

    elif Marks[i]<=4:
        high=12
        low=8
    elif Marks[i]<=7:
        high=13
        low=10
    elif Marks[i]<=12:
        high=15
        low=12
    elif Marks[i]<=17:
        high=20
        low=15
    elif Marks[i] <= 23:
        high = 20
        low = 9
    elif Marks[i] <= 34:
        high = 16
        low = 10
    elif Marks[i] <= 37:
        high = 15
        low = 9
    else:
        high = 11
        low = 7

    obj.MainNumbers(low,high,Marks[i])




#
# obj = SuperAnswer()
#
# for i in range(10):
#     obj.MainNumbers(1,7,5)
#     obj.zero()
#     obj.MainNumbers(15,25,11)
#     obj.MainNumbers(8,12,2)
#     obj.MainNumbers(18,23,1)
#     obj.zero()
#     obj.MainNumbers(1,7,5)
#     obj.zero()
#     obj.MainNumbers(13,17,1)
#     obj.zero()
#     obj.MainNumbers(38,44,1)
#     obj.zero()
#     obj.MainNumbers(32,37,1)
#     obj.zero()
#     obj.zero()
#     obj.MainNumbers(15,25,11)
#
#     obj.zero()
#     obj.MainNumbers(8,12,2)
#     obj.zero()
#     obj.MainNumbers(18,23,1)
#     obj.MainNumbers(13,17,1)
#     obj.zero()
#     obj.MainNumbers(18,23,1)
#     obj.zero()
#     obj.MainNumbers(13,17,1)
#     obj.MainNumbers(18,23,1)
#     obj.zero()
#     obj.MainNumbers(13,17,1)
#     obj.MainNumbers(15,25,11)
#     obj.MainNumbers(18,23,1)
#     obj.zero()
#     obj.MainNumbers(13,17,1)
#
#     obj.MainNumbers(15,25,11)
#     obj.MainNumbers(38,44,1)
#     obj.zero()
#     obj.MainNumbers(32,37,1)
#     obj.MainNumbers(15,25,11)
#     obj.zero()
#     obj.MainNumbers(26,34,2)
#     obj.zero()



