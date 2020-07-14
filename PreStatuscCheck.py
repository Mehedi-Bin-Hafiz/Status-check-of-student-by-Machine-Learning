from StatusSuggestion import *

###################Status check part###################
class Statuscheck():
    def __init__(self, value,allanswer):
        self.ID = value
        self.allanswer = allanswer
    def Status(self):
        A1,A2,A3,A4,A5,A6,A7,A8,A9,A10 = self.allanswer
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
        # print("Topic:Input output.")
        # print("question 1: What is the output of this code? Printf('\\\\'); \n")
        ans1=A1

        if(ans1== 2 ): ##//
            # print('Right, You have got 1 marks')
            q1=1
        else:
            TopicName=1
            # print('Wrong, Correct Answer is: \\ \n')

        # print("\nTopic: Simple calculation \n")
        # print("Question 2:  What is the output of this line?  printf("'"%d%d"'",10+10,10-3);")
        ans1 = A2
        if (ans1 == 1): ##207
            # print('Right, You have got 2 marks')
            q2 = 2
        else:
            # print('Wrong, Correct Answer is: 207\n')
            problemlist.append("simple calculation")
        #
        # print("\nTopic: String: \n")
        # print('Question 3:If char V[100] ='"Hello world"' then choose option for printing  Hello World. ')
        # print('A.   printf("%ld",V )')
        # print('B.   printf("%c",V)')
        # print('C.   printf("%s",V)')
        # print('D.   printf("%f",V)')
        ans1 = A3
        # ans1 = ans1.lower()
        if (ans1 == 3):
            # print('Right, You have got 3 marks')
            q3 = 3
        else:
            problemlist.append('String')
            # print('Wrong, Correct Answer is: Option C\n')

        # print("\nTopic: Input Output\n")
        # s = '\\n'
        # print("Question 4: How will you print " + s + " on the screen?")
        # print('A.	printf("\\n");')
        # print('B.	echo "\\\\n";')
        # print("C.	printf('\\n');")
        # print('D.	printf("\\\\n");')
        ans1 = A4
        # ans1 = ans1.lower()
        if (ans1 == 4):
            # print('Right, You have got 4 marks')
            q4 = 4
        else:
            TopicName=1
            # print('Wrong, Correct Answer is: Option D\n')

        if (TopicName==1):
            problemlist.append("Input output")

        # print( "\nTopic: Expression\n")
        # print("Question 5: Write C expression of   2x^2+3xy ")
        # print("A.	2*xx+3*xy")
        # print("B.	2x^2+3*x*y")
        # print("C.	2*x*x+3*x*y")
        # print("D.   2*x*2+3*x*y")
        ans1=A5
#         # ans1=ans1.lower()
        if(ans1== 3):
            # print('Right, You have got 5 marks')
            q5=5
        else:
            problemlist.append("Expression")
            # print('Wrong, Correct Answer is: Option C\n')

        # print("Question 6:"+
        #        "int A =10;\n " +"if( A < 10) \n"+ "    {A += 10;}\n"+"else\n"
        #         "    {A -= 10; }\n"+'printf(''"%d"'',A); ')
        ans1=A6
#         # ans1=ans1.lower()
        if(ans1== 1 ):
            # print('Right, You have got 6 marks')
            q6=6
        else:
            TopicName=2
            # print('Wrong Correct Answer is: 0\n')


        # print( "\nTopic: Conditional statement\n")
        #
        # print('Question 7: \nint  i = 2; \nprintf("output is: ");\nswitch (i)\n     { \n     case 1: \n           printf("case 1");\n     } ')
        ans1= A7
        # ans1=ans1.lower()
        if(ans1==3):
            # print('Right, You have got 7 marks')
            q7=7
        else:
            pass
            # print('Wrong Correct Answer is: output is: \n')
        if (TopicName == 2):
            problemlist.append("Conditional statement")

        # print( "\nTopic: Control Instructions\n")
        #
        # print("Question 8: \n"+
        #       " int main() { \n"+
        #       "     char a = 10, b = 20, c = 10, d=0; \n"
        #       "     d = (a * b) / c;\n"
        #       "     d++;\n" + 'printf (''"Output is: %d "'', d);\n'+
        #        " return 0;\n} ")
        ans1=A8
        # ans1=ans1.lower()
        if(ans1==4):
            # print('Right, You have got 8 Marks')
            q8=8
        else:
            problemlist.append("Arithmetic operation")
            # print('Wrong Correct Answer is: Output is: 21 \n')

        # print( "\nTopic: loop\n")
        #
        # print("Question 9:\n"+
        #      "int i, a=5, b=5, sum=0;\n"+
        #      "sum=a+b;\n"+
        #      "for (i = 0; i <=2; i++) {\n"+
        #         "    sum++;\n"+
        #      'printf("%d, %d \\n", i , sum);\n}' )
        # print('A. 1, 11\n   1, 12\n   2, 13')
        # print('B. 0, 11\n   1, 12\n   2, 13')
        # print("C. 0, 10\n   1, 11\n   2, 13")
        # print('D. 1, 11\n   1, 12\n   2, 13')

        ans1=A9
        # ans1=ans1.lower()
        if(ans1== 2):
            # print('Right, You have got 9 marks')
            q9=9
        else:
            problemlist.append("loop")
        #     print('Wrong, Correct Answer is: Option B\n')
        # print("\nTopic: Problem solving\n")
        #
        # print(" Question 10: \nWhich expression is right for 25% of $320  ")
        # print("A. (25/100)*320")
        # print("B. (100/25)*320")
        # print("C. (100/325)*25")
        # print("D.  25/(100*320)")

        ans1 = A10
        # ans1 = ans1.lower()
        if (ans1 == 1):
            # print('Right, You have got 10 point')
            q10 = 10
        else:
            problemlist.append("Problem solving")
            # print('Wrong, Correct Answer is: Option A\n')

        credit=20
        totalpoint=q1*2+q2*2+q3*2+q4+q5*2+q6*2+q7*2+q8*2+q9*2+q10*2
        totalmarks=q1+q2+q3+q4+q5+q6+q7+q8+q9+q10
        point=totalpoint/credit
        # print("your total marks ",totalmarks)
        # print('Your total points are ', point)
        f = open('C:\\Users\Mehedi\Desktop\suggestion\{0}.doc'.format(self.ID), 'w')
        f.write("Your total point is: ")
        f.write(str(point)+"\n\n")
        f.write("Your total mark is:")
        f.write(str(totalmarks)+"\n\n")

        # huge scope for analysis

        # print("\n")
        quality=None
        find=5.5/3
        if(point>=0 and point<=find):
            quality='beginner'

        elif(point>find and point<=find*2):

            quality='intermediate'

        elif(point>find*2 and point <=find*3):
            quality='expert'

        f.close()

        # print("You are a ",quality)
        f = open('C:\\Users\Mehedi\Desktop\suggestion\{0}.doc'.format(self.ID), 'a')
        f.write("You are a "+quality+"\n\n")

        if (len(problemlist)>0):
            # print("your problem are:\n")
            cou=1
            for i in problemlist:

                # print(cou,". ",i)
                cou=cou+1
        else:
            pass
            # print("Welcome, you have no problem.")

        f.close()
            #file:
        co2 = 1
        f = open('C:\\Users\Mehedi\Desktop\suggestion\{0}.doc'.format(self.ID), 'a')

        if (len(problemlist) > 0):
            f.write("your problem list is:\n")
            for i in problemlist:
                f.write(str(co2))
                f.write(". " + i + "\n")
                co2 = co2 + 1
        else:
            f.write("welcome, You have no problem.l")
        f.close()

        if(quality=='expert'):
            ex=expert(self.ID)
            ex.books()
            for p in problemlist:
                if(p=="simple calculation"):
                    ex.calculation()
                elif(p=="Expression"):
                    ex.Expressions()
                elif(p=='Problem solving'):
                    ex.problem()
                elif(p=="loop"):
                    ex.loop()
                elif(p=='Input output'):
                    ex.inputOutput()
                elif(p=="String"):
                    ex.string()
                elif(p=="Conditional statement"):
                    ex.conditional()
                elif(p=='Arithmetic operation'):
                    ex.arithmetic()

        if(quality=='beginner'):
                beg=beginner(self.ID)
                beg.books()
                for p in problemlist:
                    if (p == "simple calculation"):
                        beg.calculation()
                    elif (p == "Expression"):
                        beg.Expressions()
                    elif (p == 'Problem solving'):
                        beg.problem()
                    elif (p == "loop"):
                        beg.loop()
                    elif (p == 'Input output'):
                        beg.inputOutput()
                    elif (p == "String"):
                        beg.string()
                    elif (p == "Conditional statement"):
                        beg.conditional()
                    elif (p == 'Arithmetic operation'):
                        beg.arithmetic()

        if (quality == 'intermediate'):
                inme = intermediate(self.ID)
                inme.books()
                for p in problemlist:
                    if (p == "simple calculation"):
                        inme.calculation()
                    elif (p == "Expression"):
                        inme.Expressions()
                    elif (p == 'Problem solving'):
                        inme.problem()
                    elif (p == "loop"):
                        inme.loop()
                    elif (p == 'Input output'):
                        inme.inputOutput()
                    elif (p == "String"):
                        inme.string()
                    elif (p == "Conditional statement"):
                        inme.conditional()
                    elif (p == 'Arithmetic operation'):
                        inme.arithmetic()


        with open("C:\\Users\Mehedi\Desktop\Database\prestatusdatabase.csv", 'a', encoding='utf-8') as data:
                   data.write(str(self.ID)+"   ,"+str(q1)+","+str(q2)+","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+","+str(q7)+","+str(q8)+","+str(q9)+","+str(q10)+","+str(totalmarks)+"\n")
        data.close()
        #copy database.
        with open("PreStatusdata.csv", 'a', encoding='utf-8') as data:
            data.write(str(self.ID) + "   ," + str(q1) + "," + str(q2) + "," + str(q3) + "," + str(q4) + "," + str(
                q5) + "," + str(q6) + "," + str(q7) + "," + str(q8) + "," + str(q9) + "," + str(q10) + "," + str(
                totalmarks) + "\n")
        data.close()


