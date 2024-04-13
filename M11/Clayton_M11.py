#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: M11
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv, sys
import tkinter as tk

FILENAME = 'contacts.csv'

#I accidentally made the GUI version of this without saving the normal version,
#so I had to redo this lame version

def display_title():
    print("Clayton's Contact Manager App\n")    #title

def display_menu():
    print("COMMAND MENU\n")     #made most of this all in one print statement for fun
    print("""list - Display all contacts    
view - View a contact
add - Add a contact
del - Delete a contact
exit - Exit program\n""")

def read_contacts():
    contacts = []       #create a new empty list
    try:
        with open(FILENAME, newline="") as File:    #open the csv
            reader = csv.reader(File)       #create a csv reader object
            for row in reader:      #iterate through each row in the csv,
                contacts.append(row)#each row becomes a list within the contacts list
    except FileNotFoundError:   
        print("Could not find contacts file! Starting new contacts file...")
    
    return contacts     #return the contacts list, even if the file doesn't already exist

def display(contacts):
    if len(contacts) != 0:  #there has to be something in the contacts list
        for i, row in enumerate(contacts, start=1):     #iterate, assign a number to each
            print(f"{i}. {row[0]}")     #prints the numbering and the name(index[0]) of each contact

    else:
        print("There are no contacts in the list")
        return contacts

def view(contacts):
    number = get_contact_number(contacts)   #basically get the index number
    if number > 0:  #validation
        contact = contacts[number-1]    #correct for off-by-one error
        print("Name:", contact[0])  #print first index
        print("Email:", contact[1]) #print second index
        print("Phone:", contact[2]) #print third index
        print() 

def get_contact_number(contacts):
    while True:
        try:
            number = int(input("Number: ")) #user input
        except ValueError:
            print("Invalid integer.\n") #validation
            return -1   #returns this so the view() will not print anything
            
        if number < 1 or number > len(contacts): #validation
            print("Invalid contact number.\n")
            return -1   #returns this so the view() will not print anything
        else:
            return number
        
def add(contacts):
    name = input("Name: ")  #user inputs for contact info
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []      #make a list for each contact
    contact.append(name)    #add each input to the contact list
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)    #add the contact list to the larger contacts list
    write_contacts(contacts)    #write the larger contacts list to csv
    print(f"{contact[0]} was added.")   #feedback

def delete(contacts):
    number = get_contact_number(contacts)   #get user input
    if number > 0:  #make sure it's valid
        contact = contacts.pop(number-1)    #pop that index item from the list
        print(f"{contact[0]} was deleted.\n")   #feedback
    write_contacts(contacts)    #write to csv file

def write_contacts(contacts):
    with open(FILENAME, "w", newline='') as File:   #opens the file in write mode
        writer = csv.writer(File)   #csv writer object
        writer.writerows(contacts)  #writes each item in contacts to a row in the csv

def exit_program():
    print("Terminating program...")
    sys.exit()  #kill it

def main():
    contacts = read_contacts() #get a list from the csv file
    display_title() #self explanatory
    display_menu()  #^

    while True:
        command = input("Command: ")    #all self explanatory. Take user input.
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":  
    main()