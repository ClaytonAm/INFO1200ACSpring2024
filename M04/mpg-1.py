#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

another_trip = "y" #begins the while loop with default input of y

while another_trip.lower() == "y": #checks if the user wants to do another trip calculation. Defaults to y.
# get input from the user
    miles_driven = float(input("Enter miles driven:         ")) #user input for miles driven float
    gallons_used = float(input("Enter gallons of gas used:  ")) #user input for gallons used float
    cost_per_gallon = float(input("Enter cost per gallon:     ")) #user input for cost per gallon float

    if miles_driven <= 0: #checks if user entered valid miles driven
        print("Miles driven must be greater than zero. Please try again.") #try again, user
    elif gallons_used <= 0: #checks if user entered valid gallons used
        print("Gallons used must be greater than zero. Please try again.") #try again, user
    elif cost_per_gallon <= 0: #checks if user entered valid cost per gallon
        print("Cost per gallon must be greater than zero. Please try again.") #try again, user
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2) #calc and round mpg
        total_gas_cost = round((gallons_used * cost_per_gallon),1) #calc and round total gas cost
        cost_per_mile = round((total_gas_cost / miles_driven),1) #calc and round cost per mile
        print("Miles Per Gallon:          ", mpg) #prints calced mpg
        print("Total Gas Cost:          ", total_gas_cost) #prints calced total gas cost
        print("Cost Per Mile:          ", cost_per_mile) #prints calced cost per mile

    another_trip = input("Another trip?(y/n): ") #user input to repeat the while loop

print()
print("Bye") #displays if user says n



