# for i in range(1,11):  #for create file
#    f1=open('..\statusmean\FinalQuestions\{0}.txt'.format(i),'w')
#    f1.close()


class FinalStatus():
    def __init__(self, value):
        self.ID = value
    def Status(self):
        problemlist=[]
        TopicName=0
        q1=0
        q2=0
        q3=0
        q4=0
        q5=0
        q6=0
        q7=0
        q8=0
        q9=0
        q10=0
        position=0
        print("Topic:Input output.")
        f1=open('..\statusmean\FinalQuestions\q1.txt','r',encoding="utf8")
        print(f1.read())
        f1.close()

        ans1=input("Enter your ans:")

        if(ans1=="\\"):
            print('Right, You have got 1 marks')
            q1=1
        else:
            TopicName=1
            print('Wrong, Correct Answer is: \\ \n')

        print("\nTopic: Simple calculation \n")
        print("Question 2: ")
        f2 = open('..\statusmean\FinalQuestions\q2.txt', 'r', encoding="utf8")
        print(f2.read())
        f2.close()

        ans1 = input("Enter your ans:")
        if (ans1 == '207'):
            print('Right, You have got 2 marks')
            q2 = 2
        else:
            print('Wrong, Correct Answer is: 207\n')
            problemlist.append("simple calculation")

        print("\nTopic: String: \n")
        print('Question 3: ')
        f3 = open('..\statusmean\FinalQuestions\q3.txt', 'r', encoding="utf8")
        print(f3.read())
        f3.close()

        print('A.   printf("%ld",V )')
        print('B.   printf("%c",V)')
        print('C.   printf("%s",V)')
        print('D.   printf("%f",V)')
        ans1 = input("Enter your ans:")
        ans1 = ans1.lower()
        if (ans1 == 'c'):
            print('Right, You have got 3 marks')
            q3 = 3
        else:
            problemlist.append('String')
            print('Wrong, Correct Answer is: Option C\n')

        print("\nTopic: Input Output\n")
        print("Question 4: ")
        f4 = open('..\statusmean\FinalQuestions\q4.txt', 'r', encoding="utf8")
        print(f4.read())
        f4.close()
        print('A.	printf("\\n");')
        print('B.	echo "\\\\n";')
        print("C.	printf('\\n');")
        print('D.	printf("\\\\n");')
        ans1 = input("Enter your ans:")
        ans1 = ans1.lower()
        if (ans1 == 'd'):
            print('Right, You have got 4 marks')
            q4 = 4
        else:
            TopicName=1
            print('Wrong, Correct Answer is: Option D\n')

        if (TopicName==1):
            problemlist.append("Input output")

        print( "\nTopic: Expression\n")
        print("Question 5: ")
        f5 = open('..\statusmean\FinalQuestions\q5.txt', 'r', encoding="utf8")
        print(f5.read())
        f5.close()

        print("A.	2*xx+3*xy")
        print("B.	2x^2+3*x*y")
        print("C.	2*x*x+3*x*y")
        print("D.   2*x*2+3*x*y")
        ans1=input("Enter your ans:")
        ans1=ans1.lower()
        if(ans1=='c'):
            print('Right, You have got 5 marks')
            q5=5
        else:
            problemlist.append("Expression")
            print('Wrong, Correct Answer is: Option C\n')

        print("Question 6:\n")
        f6 = open('..\statusmean\FinalQuestions\q6.txt', 'r', encoding="utf8")
        print(f6.read())
        f6.close()
        ans1=input("Enter your ans:")
        ans1=ans1.lower()
        if(ans1=='0'):
            print('Right, You have got 6 marks')
            q6=6
        else:
            TopicName=2
            print('Wrong Correct Answer is: 0\n')


        print( "\nTopic: Conditional statement\n")

        print('Question 7: ')
        f7 = open('..\statusmean\FinalQuestions\q7.txt', 'r', encoding="utf8")
        print(f7.read())
        f7.close()

        ans1=input("Enter your ans:")
        ans1=ans1.lower()
        if(ans1=='output is: '):
            print('Right, You have got 7 marks')
            q7=7
        else:
            print('Wrong Correct Answer is: output is: \n')
        if (TopicName == 2):
            problemlist.append("Conditional statement")

        print( "\nTopic: Control Instructions\n")

        print("Question 8: ")
        f8 = open('..\statusmean\FinalQuestions\q8.txt', 'r', encoding="utf8")
        print(f8.read())
        f1.close()
        ans1=input("Enter your ans:")
        ans1=ans1.lower()
        if(ans1=='output is: 21'):
            print('Right, You have got 8 Marks')
            q8=8
        else:
            problemlist.append("Arithmetic operation")
            print('Wrong Correct Answer is: Output is: 21 \n')

        print( "\nTopic: loop\n")

        print("Question 9: " )
        f9 = open('..\statusmean\FinalQuestions\q9.txt', 'r', encoding="utf8")
        print(f9.read())
        f9.close()
        print('A. 1, 11\n   1, 12\n   2, 13')
        print('B. 0, 11\n   1, 12\n   2, 13')
        print("C. 0, 10\n   1, 11\n   2, 13")
        print('D. 1, 11\n   1, 12\n   2, 13')

        ans1=input("Enter your ans:")
        ans1=ans1.lower()
        if(ans1=='b'):
            print('Right, You have got 9 marks')
            q9=9
        else:
            problemlist.append("loop")
            print('Wrong, Correct Answer is: Option B\n')
        print("\nTopic: Problem solving\n")

        print(" Question 10:  ")
        f10 = open('..\statusmean\FinalQuestions\q10.txt', 'r', encoding="utf8")
        print(f10.read())
        f10.close()
        print("A. (25/100)*320")
        print("B. (100/25)*320")
        print("C. (100/325)*25")
        print("D.  25/(100*320)")

        ans1 = input("Enter your ans:")
        ans1 = ans1.lower()
        if (ans1 == 'a'):
            print('Right, You have got 10 point')
            q10 = 10
        else:
            problemlist.append("Problem solving")
            print('Wrong, Correct Answer is: Option A\n')

status = FinalStatus(111)
status.Status()