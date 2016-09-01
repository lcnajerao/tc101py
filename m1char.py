#Char.py With the objective of explain the char use By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
result = ["0","0","0"]
total  = 0
resultA = 0.0

#Ends Variable Definition Begins First section

print("This program will simulate a digital test or quizz")
print("How many types or variables we will review today in python?")
print("A)1")
print("B)2")
print("C)3")
print("D)4")
result[0]=input("Which is the correct answer? ")
if(result[0]=="d" or result[0]=="D"):
    print("Correct answer!")
    total = total + 1
else:
    print("Incorrect answer, The correct answer is D")

#The first section ends and the second begins.

print("Which Type can store a whole word?")
print("A)String")
print("B)Integer")
print("C)Float")
print("D)Character")
result[1]=input("Which is the correct answer? ")
if(result[1]=="a" or result[1]=="A"):
    print("Correct answer!")
    total = total + 1
else:
    print("Incorrect answer, The correct answer is A")

#The Second section ends and the Third begins.

print("Which Type can store Numbers with decimal point?")
print("A)String")
print("B)Integer")
print("C)Float")
print("D)Character")
result[1]=input("Which is the correct answer? ")
if(result[1]=="c" or result[1]=="C"):
    print("Correct answer!")
    total = total + 1
else:
    print("Incorrect answer, The correct answer is C")

#The third section ends and begin the result section
resultA = ((total*(10/3)))
print("Your final grade is ",resultA)
