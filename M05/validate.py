# Clayton's validation file for the Future Value App

def get_float(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
            if number > low and number <=high:
                return number
            else:
                print("Please enter a valid number greater than ", low, "and less than or equal to ", high)
        except:
            print('Please enter a valid number.')

def get_int(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
            if number > low and number <=high:
                return number
            else:
                print("Please enter a valid number greater than ", low, "and less than or equal to ", high)
        except:
            print('Please enter a valid integer.')

def main():
    choice = "y"
    while choice.lower() == 'y':
        valid_number = get_float("Enter number: ", 0, 1000)
        print(f"Valid number = {valid_number}")
        print()
        valid_integer = get_int("Enter integer: ", 0, 50)
        print(f"Valid integer = {valid_integer}")
        print()
        choice = input('Continue? (y/n)')
    print('Bye!')

if __name__ == '__main__':
    main()