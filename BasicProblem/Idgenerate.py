import math
import random


while(True):
    x=int(input("enter id:"))
    file=open('../SecondaryDatabases/sid.csv','a')
    for i in range(1,11):
        for j in range(1,int((random.random() * 9)+2)):
            x = x + math.floor(random.random() * 3) + 1
            file.write(str(x)+'\n')
        x = x + math.floor(random.random() * 6) + 1
        file.write(str(x)+'\n')
    print(x)
    file.close()

###run after comment while loop###

file=open('../SecondaryDatabases/sid.csv', 'r')

memo=[ ] #virtual memory

for i in file:
    memo.append(i.rstrip('\n'))
file.close()


file2= open('../SecondaryDatabases/sid2.csv', 'a')
memo2 = set(memo)


for i in memo2:
    file2.write(i+'\n')

