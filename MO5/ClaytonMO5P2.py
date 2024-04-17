#Name: Clayton
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Clayton's Feet / Meters Converter")
print()

import CConverter as c

def fm_welcome():
    print("Clayton's Feet and Meters Converter")
    print()

def fm_menu():
    print(f'Conversions Menu: \na. Feet to Meters \nb. Meters to Feet \n')


def main():
    while True:
        fm_menu()
        choice = input('Select a conversion (a/b): ')
        print()
        if choice == 'a':
            feet = input('Enter feet: ')
            meters = c.to_meters(feet)
            print(round(meters, 2), ' meters')
        elif choice == 'b':
            meters = input('Enter meters: ')
            feet = c.to_feet(meters)
            print(round(feet, 2), ' feet')
        else:
            print('You did not enter a valid selection')
        more = input('Would you like to perform another conversion? (y/n): ')
        print()

        if more.lower() != 'y':
            print('Thanks, bye!')
            break

if __name__ == "__main__": main()        
