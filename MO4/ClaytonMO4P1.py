#Name: (Clayton)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Clayton's Letter Grade Converter")
print()

choice = "y" #begins with default value of y

while choice.lower() == "y": #repeats while loop if choice is y
    number = int(input("Enter numerical grade: ")) #collects user input and converts to int
    if number <= 100 and number > 93: #compares input int to score range
        letterGrade = "A" #assigns appropriate letter grade
    elif number <= 93 and number > 89: #all of these other elif lines do the same thing
        letterGrade = "A-" #it would be silly to add literally the same comments on every single one
    elif number <= 89 and number > 86:
        letterGrade = "B+"
    elif number <= 86 and number > 82:
        letterGrade = "B"
    elif number <= 82 and number > 79:
        letterGrade = "B-"
    elif number <= 79 and number > 76:
        letterGrade = "C+"
    elif number <= 76 and number > 72:
        letterGrade = "C"
    elif number <= 72 and number > 69:
        letterGrade = "C-"
    elif number <= 69 and number > 66:
        letterGrade = "D+"
    elif number <= 66 and number > 62:
        letterGrade = "D"
    elif number <= 62 and number > 59:
        letterGrade = "D-"
    elif number <= 59 and number >= 0:
        letterGrade = "E"
    else:
        print("Please enter a valid number.") #print an error message in case they enter a weird number
    print("Letter grade: ", letterGrade) #prints message and letter grade
    print()
    choice = input("Continue?(y/n): ") #user input to continue while loop. Break if anything other than y or Y
print()
print("Bye!")
