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

#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

class wizard_game(ttk.Frame):
    def __init__(self):
        
        self.inventory = ["staff", "wizard hat", "wet sponge", "wand of incontinence"]
        self.oz = ""

        self.init_components()
        
        
    def init_components(self):
        ttk.Label(root, text="Clayton's Wizard Inventory Game").grid(columnspan=2, row=0, sticky=tk.EW)
        
        ttk.Entry(root, text=self.oz, state="readonly").grid(columnspan=4, row=1, sticky=tk.N)

        self.build_buttons()

        self.build_items_box()

    def build_items_box(self):
        self.items_frame = ttk.Frame(root)
        self.items_frame.grid(column=0, row=2, columnspan=2)

        for number, item in enumerate(self.inventory, start=1):
            var = tk.IntVar(value=0)
            chk = tk.Checkbutton(self.items_frame, text=f"{number}. {item}", variable=var)
            chk.pack(anchor=tk.W)

    def build_buttons(self):
        self.buttons_frame = ttk.Frame()
        self.buttons_frame.grid(column=3, row=2, rowspan=4)
        ttk.Button(self.buttons_frame, text="Add Item", command=self.add_item).grid(column=1, row=0)
        ttk.Button(self.buttons_frame, text="Drop Item", command=self.drop_item).grid(column=1, row=1)
        ttk.Button(self.buttons_frame, text="Drop Item", command=self.edit_item).grid(column=1, row=2)

    def add_item(self):
        if len(self.inventory) >= 4:
            self.oz = "Your inventory is full"
        else:
            self.oz = "Enter name of new item"
            new_item = messagebox.askquestion("Enter name of new item")
            self.inventory.append(new_item)

    def drop_item(self):
        pass

    def edit_item(self):
        pass
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wizardry")
    ttk.Frame(width=150, height=100, padding="10 10 10 10")
    wizard_game()
    root.mainloop()


'''
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
'''
