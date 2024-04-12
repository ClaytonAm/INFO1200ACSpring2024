print("Clayton Tip Calculator App")
costOfMeal = float(input("Cost of meal: ")) #declares var for meal cost input float
tipPercentage = float(input("Tip percentage: ")) #declares var for tip percentage input float
tipPercentage = tipPercentage / 100 #converts tip percentage input to a decimal
tipAmount = costOfMeal * tipPercentage #calcs tip amount
tipAmount = round(tipAmount, 2) #rounds tip amount to 2 dec points
print() #spacing
print("Tip amount: ", tipAmount) #concatenates text with var and prints
print("Total amount: ", round(tipAmount + costOfMeal, 2)) #concatenates text with rounded total amount calc and prints
