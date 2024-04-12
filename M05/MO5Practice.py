#!usr/bin/env python3
import math

def main():
    print("Welcome to Clayton's circle calculator")

    while True:
        user_input = input("Calculate area or circumference?(a or c, x to exit: )").lower()

        if user_input == "a":
            radius = validRadius()
            area = calcArea(radius)             #redundant with this current setup
            print(f"Area: {calcArea(radius)}")  #nest the function inside the functional string print
        elif user_input == "c":
            radius = validRadius()
            circumference = calcCirc(radius)
            print(f"Circumference: {circumference}") #function is not nested in this string
        elif user_input == "x":
            break
        else:
            print("Please enter a valid command")

    print("Bye!")

def validRadius():
   while True:
        try:
            radius = float(input("Enter radius: "))
            if radius < 0:
                print("Please enter a radius greater than 0.")
            else:
                return radius
        except:
            print("Please enter a valid radius.")

def calcArea(r):
    '''
    Summary: calculates area of a circle
    Params: 
      r = radius
    '''
    area = math.pi * r ** 2 #redundant with this current setup
    return math.pi * r ** 2 #returns the calc without declaring a var for area

def calcCirc(r):
    #this uses the autoDocString extension thing
    '''Calculates the circumference of a circle given a radius

    Args:
        r (float): radius of the circle
    
    Returns:
        (float): circumference of the circle
    '''
    circumference = 2 * math.pi * r 
    return circumference    #not as efficient as the area function

if __name__ == "__main__":
    main()