#!/usr/bin/env python3
print("Clayton Rectangle App")
# display a welcome message
#print("The Miles Per Gallon program")
print()

# get input from the user
rectangle_length= float(input("Enter rectangle length:\t")) #declares variable for length input
rectangle_width = float(input("Enter rectangle width:\t")) #declares variable for width input

# calculate miles per gallon
rectangle_area = rectangle_length * rectangle_width #calculates area from length and width inputs
rectangle_perimeter = (2 * rectangle_length) + (2 * rectangle_width) #calculates perimeter from length and width inputs
            
# format and display the result
print()
print("Rectangle Area:\t\t" + str(rectangle_area)) #prints concatenated text with area string
print("Rectangle Perimeter:\t" + str(rectangle_perimeter)) #prints concatenated text with perimeter string
print()
print("Bye")


