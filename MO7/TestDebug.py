import temperatur as temp

def display_menu()
    print("The Temp Converter App")
    Print()
    print("Menu")
        print("1. Fahrenheit to Celsius")
    print("b. Celsius to Fahrenhit")
    print()

def convert_temp():
    option = int(input("Enter menu option: ")
    if option = 1:
        f = int(input(Enter Degrees Fahrenheit: ))
        c = temperature.to_Celsius(f)
        c = round(C, 2)
        print("Degrees Celsius:", c)
    elif option = 2:
        c = int(input("Enter degrees celsius: "))
        F = temp.to_fahrenheir(c)
        f = round(f, 2)
        print("Degrees Farenheit:", f)
    else:
        print("You must enter a valid menu number.")

def main():
    display_menue()
    again = "Y"
    while again.upper == "y"
        convert_temp()
        print()
    again = input("Convert another temprature? (y/n):")
    print()
print("Bye!")

if _name_ == "_main_":
    main()