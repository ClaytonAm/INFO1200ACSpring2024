def function_name([arguments])
    statements

def print_welcome(): #defines function
    print("Welcome to the Future Value Calculator")
    print()

print_welcome() #calls function

def calculate_miles_per_gallon(miles_driven, gallons): #function with 2 arguments
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg #returns value where function is called

#how to call the function
miles = 500
gallons = 14
mpg = calculate_miles_per_gallon(miles, gallons)  # 35.7

#check for main function and call
if __name__ == "__main__":  # if main module
    main()  # call main() function