#Name: Clayton
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 2024-03-30
#Project #: M09
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

def display_title():
    print("Clayton's Wizard Inventory Game")
    print()

def display_menu():
    #this whole block just prints the menu to the console
    print("COMMAND MENU")
    print()
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def main():
    display_title()
    display_menu()

    #creates list of items
    inventory = ["staff", "wizard hat", "wet sponge", "wand of incontinence"]

    while True:     #loop until the user exits
        command = input("Command: ")        
        if command == "show":       #series of if statements for each of the valid commands
            show(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")   #handle errors for invalid input
    print("Bye!")

def show(inventory):
    for number, item in enumerate(inventory, start=1): #loops through the inventory list
        print(f"{number}. {item}")                     #enumerate method assigns a number to each iteration of the list
                                                       #prints each number created by enumerate and each corresponding item from list
    print()                                            

def grab_item(inventory):
    if len(inventory) >= 4:     #defines the maximum size of the inventory
        print("You can't carry any more items. Drop something first.\n")
    else:
        item = input("Name: ")  #take user input to add to list
        inventory.append(item)  #appends list with inputted item
        print(f"{item} was added.\n")   #user feedback

def edit_item(inventory):
    number = int(input("Number: "))     #user input for item's position in the list
    if number < 1 or number > len(inventory):   #error handling for invalid input
        print("Invalid item number.\n")
    else:
        item = input("Updated name: ")  #stores user inputted position in item variable
        inventory[number-1] = item      #adjusts numbering to avoid off-by-1 errors
        print(f"Item number {number} was updated.\n")   #user feedback

def drop_item(inventory):
    number = int(input("Number: "))    #user input for item's position in the list 
    if number < 1 or number > len(inventory):  #error handling for invalid input
        print("Invalid item number.\n")
    else:
        item = inventory.pop(number-1)    #removes item from list
        print(f"{item} was dropped.\n")   #user feedback

if __name__ == "__main__":
    main()