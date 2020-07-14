# from PreStatuscCheck import Statuscheck
from FinalStatusCheck import Statuscheck

from BasicProblem import Answer_generator

import time

file=open('./BasicProblem/sid2.csv', 'r')
memo=[ ] #virtual memory




while(True):
    for i in file:
        ID = i.rstrip('\n')
        Answer = Answer_generator.Answer()
        AllAnswer= Answer.anserdef()
        hello=Statuscheck(ID,AllAnswer)
        hello.Status()
