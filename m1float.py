#float.py With the objective of explain the char use By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
height = [0.0,0.0,0.0,0.0,0.0,0.0]
result = 0
#Ends Variable definition begins the first stage
print("Program will calculate the average of Height in a family of 6 in the format M.cm")
height[0]=float(input("Introduce the height of the Father "))
height[1]=float(input("Introduce the height of the Mother "))
height[2]=float(input("Introduce the height of the Son or Daughter 1 "))
height[3]=float(input("Introduce the height of the Son or Daughter 2 "))
height[4]=float(input("Introduce the height of the Son or Daughter 3 "))
height[5]=float(input("Introduce the height of the Son or Daughter 4 "))
result = (height[0]+height[1]+height[2]+height[3]+height[4]+height[5])/6
print("The Height average of the family is ",result," M")
