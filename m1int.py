#int.py With the objective of explain the Int type use By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
lenght = [0,0,0]
area   = 0
#ends the variable definition and begins the first section
print("This program will calculate the area of a 3 dimension")
print("Paralelogram with non decimal numbers")
lenght[0] = int(input("Introduce the Height of the Paralelogram in meters "))
lenght[1] = int(input("Introduce the Width of the Paralelogram in meters "))
lenght[2] = int(input("Introduce the Lenght of the paralelogram in meters "))
#ends the first section begins the result section
area = lenght[0]*lenght[1]*lenght[2]
print("The area of the Paralelogram is ",area," Cubic Meters")
