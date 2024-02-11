#!/usr/bin/env python3
print("Clayton MPG App") #Welcome Message
# display a welcome message
#print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t")) #declares variable for Miles Driven input
gallons_used = float(input("Enter gallons of gas used:\t")) #declares variable for Gallons Used input
cost_per_gallon = float(input("Enter cost per gallon:\t\t")) #declares varable for Cost Per Gallon input

# calculate miles per gallon
#mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1) #calculates and rounds miles/gallon
cost_per_gallon = round(cost_per_gallon, 2) #rounds the input value for Cost Per Gallon
total_gas_cost = round(cost_per_gallon * gallons_used, 1) #calculates and rounds Total Gas Cost
cost_per_mile = round(total_gas_cost / miles_driven, 1) #calculates and rounds Cost Per Mile

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg)) #converts mpg var to string and concatenates with string to print
print("Total Gas Cost:\t\t\t" + str(total_gas_cost)) #converts total gas cost var to string and concatenates with string to print
print("Cost Per Mile:\t\t\t" + str(cost_per_mile)) #converts cost per mile var to string and concatenates with string to print
print()
print("Bye")


