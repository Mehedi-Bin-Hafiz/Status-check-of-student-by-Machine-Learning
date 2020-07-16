# from PreStatuscCheck import Statuscheck
from FinalStatusCheck import Statuscheck

from BasicProblem import Answer_generator

import time
## it is our first work to generate student id
file=open('./BasicProblem/sid2.csv', 'r')





while(True):
    for i in file:
        ID = i.rstrip('\n')
        Answer = Answer_generator.Answer()
        AllAnswer= Answer.anserdef()
        hello=Statuscheck(ID,AllAnswer)
        hello.Status()
