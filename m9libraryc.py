##m9Libraryc With the objective of explain how to use library By Luis Najera
#For www.codewithcharlie.com
#Begins Importation
import m10clibrary as sec
import getpass
from math import pi
#Begins Variable definition
passInsert = "x"
c = 0
#Begin with human interface
print("This program will ask for a password if you write it right will unveal the secret number ")
while(c == 0):
    passInsert = getpass.getpass()
    if(passInsert == sec.password):
        sec.fprint()
        print("The secret number is ",pi)
        c = 1
print("Bye")
