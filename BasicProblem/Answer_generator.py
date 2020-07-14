import random
import math

class Answer():
    def anserdef(self):
        A1=2
        A2=3
        A3= 3 if (random.random()*10) < 9 else 1
        A4= 4 if (random.random()*10) < 8 else 1
        A5=3 if (random.random()*10) < 6 else 1
        A6=1 if (random.random()*10) < 6 else 3
        A7=3 if (random.random()*10) < 5.5 else 1
        A8=4 if (random.random()*10) < 4.5 else 1
        A9=2 if (random.random()*10) < 4.5 else 1
        A10=1 if (random.random()*10) < 4 else 3
        return A1,A2,A3,A4,A5,A6,A7,A8,A9,A10



# for i in range(20):
#     obj = Answer()
#     print(obj.anserdef())


