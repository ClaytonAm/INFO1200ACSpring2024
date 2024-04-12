#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Clayton's Tip Calculator")
print()

meal_cost = float(input("Cost of meal: ")) #collects user input and converts to float
print()

for i in range(15,30,5): #for loop with range function. Counts range starting at 15, ending at 30, incrementing by 5 every time.
    print(i, "%") #prints the tip percentage value currently assigned to i
    tip_percent = float(i / 100) #converts current i value to a decimal float (0-1)
    tip_amount = meal_cost * tip_percent #calcs numerical amount of tip based on meal cost
    total = round(tip_amount + meal_cost, 2) #calcs total cost of the meal plus tip amount, rounds to 2 decimal places
    print("Tip amount: ", tip_amount) #prints calculated tip amount
    print("Total amount: ", total) #prints calculated total amount
    print()