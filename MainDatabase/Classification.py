import pandas as pd
import time
MainDatabase = pd.read_excel(r'../MainDatabase/MainDatabase.xlsx')

y = MainDatabase['FinalMarks'].values #dependent variables
y=y.astype('int')



classificaion=[]
for i in range(len(y)):
    point = y[i] / 10 # 10 because of points = total marks *2(credit 20)
    print(point)
    find = 5.5 / 3
    if(point>=0 and point<=find):
        quality=0
        classificaion.append(quality)

    elif(point>find and point<=find*2):

        quality=1
        classificaion.append(quality)

    elif(point>find*2 and point <=find*3):
        quality=2
        classificaion.append(quality)





MainDatabase.insert(13,"Classification",classificaion,True)
MainDatabase.to_excel(r'FullAndFinalDatabase.xlsx', index=False)