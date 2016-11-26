##m8ifelif.py With the objective of explain the while loop used By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
number = 0.0
i = 1
power = 0
numberi = float(input("Write the number you want to raise to a n power "))
power = int(input("Write the power "))
number = numberi
while(i != power):
    numberi = number * numberi
    i = i+1
print(numberi)
