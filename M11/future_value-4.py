#!/usr/bin/env python3
import sys

def get_number(prompt, low, high):
    while True:     #keep looping
        try:
            number = float(input(prompt))       #take user input and convert to float
            ###raise OSError("OS ERROR testing")
        except ValueError:      #if user enter an invalid value (like a string)
            print("Value Error: Please type in a valid number.")      
            continue
        except Exception as e:  #any other, non-specific exception
            print(type(e), e)   #print what type of exception it is and tell me the exception
            sys.exit()
        if number > low and number <= high: #check if the number is within the acceptable range
            #is_valid = True
            return number   #send it
        else:
            print(f"Entry must be greater than {low} "  #user feedback if the number is outside the acceptable range
                  f"and less than or equal to {high}.")
            
def get_integer(prompt, low, high):
    while True:     #loop it
        try:    
            number = int(input(prompt))     #take user input and convert to int
        except ValueError:      #if user enter an invalid value (like a string)
            print("Value Error: Please type in a valid number.")      
            continue
        except Exception as e:  #any other, non-specific exception
            print(type(e), e)   #print what type of exception it is and tell me the exception
            sys.exit()
        if number > low and number <= high:  #check if the number is within the acceptable range
            #is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " #user feedback if the number is outside the acceptable range
                  f"and less than or equal to {high}.")


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
