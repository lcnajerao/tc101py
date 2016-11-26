#This code is used to explain user data validation and sensitive data management
#Writed by Luis Najera Mastery 11 validation
#Import stage
import getpass as gp
#Variable Declaration stage
pswd={"Real":"Cwcpwd","Try":"x","Code":"414679876"}
i = 2
#Human interface stage
print("This program will ask you for a password, you only have 3 attemps")
print("Nuclear code generator ")
while(pswd["Try"]!=pswd["Real"] and i>=0):
    pswd["Try"]=input("Good Morning Sir, please input the Security Code ")
    if(pswd["Try"]==pswd["Real"]):
        print("Your identity has been confirmed the nuclear code is: ")
        print(pswd["Code"])
        print("Use this power with Responsibility")
    elif(i==0):
        print("Intruder Detected Changing Codes ")
        i = i-1
    else:
        print("You only have ",i," more attemps ")
        i = i-1
