#m8ifelif.py With the objective of explain the if elif used By Luis Carlos Najera
#For www.codewithcharlie.com
#Begins Variable definition
value  = 0.0
unit   = "K"
conv   = "C"
result = 0.0
#Begins Human Interface
print("This program will ask you for a tipe of temperature Cº Fº or Kº")
print("And convert it to the unit you want ")
value = float(input("Introduce the Temperature you want to convert "))
unit  = input("Introduce the unit your temperature has C, F or K ")
conv  = input("Introduce to which unit you want to Convert C, F or K ")
if(unit == conv):
    print("Your temperature is ",value,"º",conv)

elif((unit == "C" or unit =="c")and(conv == "F" or conv == "f")):
    result = ((9/5)*value)+32
    print("Your temperature is ",result,"º",conv)

elif((unit == "C" or unit =="c")and(conv == "K" or conv == "k")):
    result = value + 273.15
    print("Your temperature is ",result,"º",conv)

elif((unit == "F" or unit =="f")and(conv == "C" or conv == "c")):
    result = (value - 32)*(5/9)
    print("Your temperature is ",result,"º",conv)

elif((unit == "F" or unit =="f")and(conv == "K" or conv == "k")):
    result = (value + 459.67)*(5/9)
    print("Your temperature is ",result,"º",conv)

elif((unit == "K" or unit == "k")and(conv == "C" or conv == "c")):
    result = value - 273.15
    print("Your temperature is ",result,"º",conv)

elif((unit == "K" or unit == "k")and(conv == "F" or conv == "f")):
    result = value * (9/5) - 459.67
    print("Your temperature is ",result,"º",conv,)

else:
    print("Not valid input")
