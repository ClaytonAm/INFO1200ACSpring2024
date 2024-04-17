#Name: Clayton
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2024.2.25
#Project #: MO5_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print('Claytons even or odd checker')
print()

def is_even(num):
    if (int(num) % 2) == 0:
        return True
    else:
        return False 

def main():
    choice = "y"
    while choice.lower() == 'y':
        #print('Claytons even or odd checker')
        #print()

        my_num = input('Enter an integer: ')
        if is_even(my_num):
            print('This is an even number.')
        else:
            print('This is an odd number.')
        choice = input('Continue? (y/n)')
    print('Bye!')
if __name__ == "__main__": main()        

