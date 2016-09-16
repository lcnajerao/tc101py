#mastery6functions.py With the objective of explain the function used By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
no = [0.0,0.0,0.0] #Stands for Numerical Operators
ot = "x"            #Stands for operation type + - * /
oName = "x"
#Function definition section
def op_Sum(n1,n2,n3):
    return(n1+n2+n3)

def op_Sub(n1,n2,n3):
    return(n1-n2-n3)

def op_Mtp(n1,n2,n3):
    return(n1*n2*n3)

def op_Div(n1,n2,n3):
    return(n1/n2/n3)
#Human Interface
print("This program will perform any of the 4 arithmetic equations between 3 numbers")
print("+ for Addition - for substraction * for multiplication and / for division")

ot = input("Introduce the operator of the operation you want to perform ")

if(ot == "+" or ot == "-" or ot == "/" or ot == "*"):
    no[0] = float(input("Introduce the First Number "))
    no[1] = float(input("Introduce the Second Number "))
    no[2] = float(input("Introduce the Third Number "))

    if(ot == "+"):
        oName = "Addition"
        print("The result of your ",oName," Is",op_Sum(no[0],no[1],no[2]))

    elif(ot == "-"):
        oName = "Substraction"
        print("The result of your ",oName," Is",op_Sub(no[0],no[1],no[2]))

    elif(ot == "*"):
        oName = "Multiplication"
        print("The result of your ",oName," Is",op_Mtp(no[0],no[1],no[2]))

    elif(ot == "/"):
        oName = "Division"
        print("The result of your ",oName," Is",op_Div(no[0],no[1],no[2]))
else:
    print("Invalid Input Try again")
