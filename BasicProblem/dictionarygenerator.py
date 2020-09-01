
lis1=[]
lis2=[]
dic={}
for  i in range(1,10):
    lis1.append(i)
for j in range(1,10):
    lis2.append(j)

print(lis1)
print(lis2)
k=0
for i in lis1:
    for j in lis2:
        if i == j:
           dic[k]=i,1
           k = k + 1
           break
        elif i != j:
           dic[k]=i,0
           k = k + 1
           break


print(dic)
