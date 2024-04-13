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
from tkinter import ttk, messagebox, filedialog 

FILENAME = 'contacts.csv'

def display_title():
    print("Clayton's Contact Mangager App\n")

def display_menu():
    
    print("COMMAND MENU\n")

    print("""list - Display all contacts\n
            view - View a contact\n
            add - Add a contact\n
            del - Delete a contact\n
            exit - Exit program\n""")

def read_contacts():
    global FILENAME
    contacts = []
    try:
        with open(FILENAME, newline="") as File:
            reader = csv.reader(File)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        messagebox.showerror(message="Could not find contacts file! Starting new contacts file...")
    
    return contacts

def main():
    contacts = read_contacts()
    display_title()
    display_menu()

    while True:
        command = input("Command: ")
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

def display(contacts):
    
    if len(contacts) != 0:
        for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}\n")

    else:
        print("There are no contacts in the list")
        return contacts

def view(contacts):
    number = get_contact_number
    if number > 0:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print() 

def get_contact_number(contacts):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer.\n")
            return -1
            
        if number < 1 or number > len(contacts):
            print("Invalid contact number.\n")
            return -1
        else:
            return number
        
def add():
    def save_contacts():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

        contact = []
        contact.append(name)
        contact.append(email)
        contact.append(phone)
        contacts.append(contact)
        write_contacts()

        messagebox.showinfo(message=f"{contact[0]} was added.\n")
    
    add_contact_window = tk.Toplevel(root)
    add_contact_window.title("Add Contact")

    tk.Label(add_contact_window, text="Name:").grid(column=0,row=0)
    name_entry = tk.Entry(add_contact_window)
    name_entry.grid(column=1, row=0)

    tk.Label(add_contact_window, text="Email").grid(column=0,row=1)
    email_entry = tk.Entry(add_contact_window)
    email_entry.grid(column=1,row=1)

    tk.Label(add_contact_window, text="Phone").grid(column=0,row=2)
    phone_entry = tk.Entry(add_contact_window)
    phone_entry.grid(column=1,row=2)

    tk.Button(add_contact_window,text="Save Contact",command=save_contacts).grid(column=0,columnspan=2,row=3)

def delete():
    def delete_selected():
        try:
            selected = int(deletion_entry.get())
            length = len(contacts)
            if selected >= 1 and selected <= length:
                contact = contacts.pop(selected-1)
                write_contacts()
                messagebox.showinfo(message=f"Contact: {contact} was deleted.")
                refresh_listbox()
            else:
                messagebox.showerror(message="Enter a valid number")
        except ValueError:
            messagebox.showerror("Invalid input")

    def refresh_listbox():
        contacts_listbox.delete(0, tk.END)
        for i, contact in enumerate(contacts, start=1):
            text = f"{i}. {contact[0]}"
            contacts_listbox.insert(tk.END, text)

    contacts = read_contacts()

    delete_contacts_window = tk.Toplevel(root)
    delete_contacts_window.title("Delete Contacts")

    contacts_frame = ttk.Frame(delete_contacts_window)
    contacts_frame.grid(row=0, column=1, rowspan=4,sticky="ne")

    contacts_listbox = tk.Listbox(contacts_frame)
    contacts_listbox.grid(row=0,column=0,rowspan=4, sticky="ne")

    contacts_scrollbar = ttk.Scrollbar(contacts_frame, orient=tk.VERTICAL,command=contacts_listbox.yview)
    contacts_scrollbar.grid(row=0,column=1,sticky="ns")
    contacts_listbox.config(yscrollcommand=contacts_scrollbar.set)
    
    for i,contact in enumerate(contacts, start=1):
        text = f"{i}. {contact[0]}"
        contacts_listbox.insert(tk.END, text)

    tk.Label(delete_contacts_window, text="Enter contact number to delete").grid(column=0,row=0)
    deletion_entry = tk.Entry(delete_contacts_window)
    deletion_entry.grid(column=0,row=1)

    tk.Button(delete_contacts_window,text="Delete Selected",command=delete_selected).grid(column=0,row=2)

def write_contacts():
    global FILENAME
    with open(FILENAME, "w", newline='') as File:
        writer = csv.writer(File)
        writer.writerows(contacts)

def import_file():
    global FILENAME
    FILENAME = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if FILENAME:
        messagebox.showinfo(message=f"Successfully imported file: {FILENAME}")
    else:
        messagebox.showinfo(message="Import failed")
    return FILENAME

def exit_program():
    messagebox.showinfo(message="Terminating program...")
    sys.exit()

if __name__ == "__main__":  
    main()