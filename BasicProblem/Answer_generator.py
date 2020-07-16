import random
import math



import random
import math



class SuperAnswer():

    def zero(self):
        return 0,0,0,0,0,0,0,0,0,0
    def MainNumbers(self,lowRange,highRange,percent):
        g = []
        while percent >= 0:
            a = random.randrange(lowRange, highRange + 1, 1)
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
            percent = percent - 1
            for k in ans:
                anss[k - 1] = k
            anss.append(a)
            file = open('testprenumberlist.csv','a')
            file.write(str(anss)+'\n')




obj = SuperAnswer()
obj.MainNumbers(10,15,10)




# class Answer(SuperAnswer):
#
#     def anserdef(self):
#
#             return super().MainNumbers()


        # return A1,A2,A3,A4,A5,A6,A7,A8,A9,A10




# for i in range(1):
#     obj = Answer()
#     print(obj.anserdef())






