#!/usr/bin/env python3

# display a welcome message
print("Welcome to Clayton's Future Value Calculator")
print()

choice = "y" #begins the while loop with default input of y

while choice.lower() == "y": #value y begins while loop
    is_valid = True #resets is_valid to bool value of True
    while is_valid: 
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t")) #user input for monthly investment
        if monthly_investment > 0 and monthly_investment <= 1000: #check if user input is within valid range
            is_valid = False #valid input changes is_valid to false
        else:
            print("Please enter a monthly investment between 0 and 1000") #invalid user input. Try again.

    is_valid = True #resets is_valid to bool value of True
    while is_valid:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t")) #user input for yearly interest rate
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15: #check if user input is within valid range
            is_valid = False #valid input changes is_valid to false
        else:
            print("Please enter an interest rate between 0 and 15") #invalid user input. Try again.

    is_valid = True #resets is_valid to bool value of True
    while is_valid:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50: #check if user input is within valid range
            is_valid = False #valid input changes is_valid to false
        else:
            print("Please enter years between 0 and 50") #invalid user input. Try again.

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100 #converts yearly interest to monthly percentage value
    months = years * 12 #convert user input years to months
    print()
    # calculate the future value
    future_value = 0 #starts counter at 0
    for i in range(1,months + 1): #loops and increments a counter
        future_value += monthly_investment #adds monthly investment to future value and reassigns future value
        monthly_interest_amount = future_value * monthly_interest_rate #multiplies new value of future_value by monthly interest rate
        future_value += monthly_interest_amount #adds monthly interest to future value and reassigns future value

        if(i % 12) == 0: #when counter reaches 12 months
            print(f"Year = {i // 12}\tFuture Value: = {round(future_value, 2)}") #print the calculated values for each year on a new line

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2))) #prints total future value after specified years
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ") #ask to continue. y continues loop.
    print()

print("Bye!")
