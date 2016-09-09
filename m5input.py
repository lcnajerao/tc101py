#mastery5input.py With the objective of explain the input use By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
result={"Lenght":0.0,"Width":0.0,"Height":0.0,"Area":0.0}
#End of VD, Begins the user interface section
print("In this program you will learn how to use the function input")
print("The Input function is composed by the next structure for int and float results")
print("varName = (varType(input('Message'))")
print("Or for a char or a string the structure is")
print("varName = input('Message')")
print("The next program will calculate the area of a cubic paralelogram in cubic cm")
result["Lenght"]= float(input(result["Area"]))
result["Width"] = float(input( "Introduce the Width of your Paralelogram in cm^3 "))
result["Height"]= float(input("Introduce the Height of your Paralelogram in cm^3 "))
result["Area"]  = result["Lenght"]*result["Width"]*result["Height"]
print("The area of your Cubic Paralelogram is ",result["Area"]," cm^3")
print("OR")
print("The area of your Cubic Paralelogram is ",result["Lenght"]*result["Width"]*result["Height"]," cm^3")
print("OR")
print(result)
