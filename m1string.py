#String.py With the objective of explain the string type use By Luis Najera
#For www.codewithcharlie.com
#Begins Variable definition
language = "0"
name = "name"
#End of the variable declaration begining of the stage one
print("This program will ask you which language you speak and will say hello in your language")
print("The language options are ES for español EN for english DE for Deutsch and FR for Français ")
language = input("Choose your language: ")
if  (language == "EN" or language == "En" or language == "en" ):
    name = input("What is your name? ")
    print("Hello ", name," have a wonderful day" )

elif(language == "ES" or language == "Es" or language == "es"):
    name = input("Como te llamas? ")
    print("Hola ",name," Que tengas un hermoso dia")

elif(language == "DE" or language == "De" or language == "de"):
    name = input("Wie heißt du? ")
    print("Hallo ",name," Du Hast eine Schone tage")

elif(language == "FR" or language == "Fr" or language == "fr"):
    name = input("Comment Tu T´appele ")
    print("Salut ",name,)

print("Thanks for watching")
