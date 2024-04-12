#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Clayton's Change App")
print()

choice = "y" #begins with default value of y

while choice.lower() == "y": #repeats while loop if choice is y
    cents = int(input("Enter number of cents (0-99): ")) #collects user input and converts to int
    print()
    quarters = cents // 25 #calcs maximum possible number of quarters. // divides integers while ignoring remainder
    print("Quarters: ", quarters) #prints max number of quarters
    cents = cents % 25 #assigns new value to cents. % divides integers and only returns the remainder
    dimes = cents // 10 #calcs maximum possible number of dimes
    print("Dimes:    ", dimes) #prints max number of dimes
    cents = cents % 10 #assigns new value to cents
    nickels = cents // 5 #calcs maximum number of nickels
    print("Nickels:  ", nickels) #prints max number of nickels
    cents = cents % 5 #assigns new value to cents
    print("Pennies:  ", cents) #prints remaining value of cents which should always be less than 5, thus should always be equivalent to pennies.
    print()
    choice = input("Continue?(y/n): ") #user input to continue while loop. Break if anything other than y or Y
print()
print("Bye!")