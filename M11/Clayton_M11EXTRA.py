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

#created global variables so I don't have to constantly pass them through the functions.
FILENAME = ''
contacts = []

def read_contacts():
    global FILENAME
    contacts = []
    try:
        with open(FILENAME, newline="") as File:
            reader = csv.reader(File)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:       #i used messagebox for errors, so any exceptions will pop up in a separate little window
        messagebox.showerror(message="Could not find contacts file! Starting new contacts file...")
    
    return contacts

def view():
    global contacts
    contacts = read_contacts()
    if len(contacts) > 0:
        view_contacts_window = tk.Toplevel()    #I learned about the TopLevel widget for making a separate window
        view_contacts_window.title("Your contacts")
        listbox = tk.Listbox(view_contacts_window, width=50)    #used listboxes to show outputs of variable lengths
        listbox.grid(row=0,column=0,columnspan=4)
        for i, row in enumerate(contacts, start=1): #this writes data from the contacts list to the listbox
            listbox.insert(tk.END, f"{i}. {row[0]} - {row[1]} - {row[2]}\n")
    else:
        messagebox.showerror(message="There are no contacts in the list")
        
def add():
    def save_contacts():    #functionception
        name = name_entry.get()     #these retrieve the inputted values from the entry boxes
        email = email_entry.get()
        phone = phone_entry.get()

        contact = []
        contact.append(name)    #this is basically the same as the non-gui version
        contact.append(email)   #makes a list for each contact,
        contact.append(phone)
        contacts.append(contact)    #adds each small contact list to the larger contactS list
        write_contacts()

        messagebox.showinfo(message=f"{contact[0]} was added.\n")
    
    add_contact_window = tk.Toplevel(root)  #opens a new window
    add_contact_window.title("Add Contact")

    tk.Label(add_contact_window, text="Name:").grid(column=0,row=0) #these are just labeled entry boxes
    name_entry = tk.Entry(add_contact_window)
    name_entry.grid(column=1, row=0)

    tk.Label(add_contact_window, text="Email").grid(column=0,row=1)
    email_entry = tk.Entry(add_contact_window)
    email_entry.grid(column=1,row=1)

    tk.Label(add_contact_window, text="Phone").grid(column=0,row=2)
    phone_entry = tk.Entry(add_contact_window)
    phone_entry.grid(column=1,row=2)

    tk.Button(add_contact_window,text="Save Contact",command=save_contacts).grid(column=0,columnspan=2,row=3)   #it's a button.

def delete():
    def delete_selected():  #functionception intensifies
        try:
            selected = int(deletion_entry.get())    #user manually enters the contact to delete
            length = len(contacts)      #salutations, validations
            if selected >= 1 and selected <= length:    
                contact = contacts.pop(selected-1)  #pop it
                write_contacts()    #lock it
                messagebox.showinfo(message=f"Contact: {contact} was deleted.") #talk it
                refresh_listbox()   #crop it
            else:
                messagebox.showerror(message="Enter a valid number")
        except ValueError:
            messagebox.showerror("Invalid input")

    def refresh_listbox():  #this function clears the listbox and displays the new contacts list,
        contacts_listbox.delete(0, tk.END)  #after the selected entry was deleted
        for i, contact in enumerate(contacts, start=1): #kinda proud of this idea
            text = f"{i}. {contact[0]}"
            contacts_listbox.insert(tk.END, text)

    contacts = read_contacts()

    delete_contacts_window = tk.Toplevel(root)  #new window for the contact deletion stuff
    delete_contacts_window.title("Delete Contacts")

    contacts_frame = ttk.Frame(delete_contacts_window)  #frame
    contacts_frame.grid(row=0, column=1, rowspan=4,sticky="ne")

    contacts_listbox = tk.Listbox(contacts_frame)   #listbox to show the contacts
    contacts_listbox.grid(row=0,column=0,rowspan=4, sticky="ne")

    contacts_scrollbar = ttk.Scrollbar(contacts_frame, orient=tk.VERTICAL,command=contacts_listbox.yview)  
    contacts_scrollbar.grid(row=0,column=1,sticky="ns")     #scrollbar in case the contacts list is long
    contacts_listbox.config(yscrollcommand=contacts_scrollbar.set)  #this was surprisingly tricky to figure out
    
    for i,contact in enumerate(contacts, start=1):  #iterate through the contacts list, assign a number
        text = f"{i}. {contact[0]}"     #formatting
        contacts_listbox.insert(tk.END, text)   #adds each iteration to the listbox

    tk.Label(delete_contacts_window, text="Enter contact number to delete").grid(column=0,row=0)
    deletion_entry = tk.Entry(delete_contacts_window)   #the user enters the number. I wanted to do something cooler but,
    deletion_entry.grid(column=0,row=1)     #this works so whatever

    tk.Button(delete_contacts_window,text="Delete Selected",command=delete_selected).grid(column=0,row=2)   #delete button

def write_contacts():
    global FILENAME     #grab that global var so we can read it, but also change the value
    with open(FILENAME, "w", newline='') as File:   #open 'er up
        writer = csv.writer(File)   #writerbot
        writer.writerows(contacts)  #write it

def import_file():
    global FILENAME     #grab the global var so we can change it
    FILENAME = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])   #this is a cool module
                        #this program could potentially open any CSV file. 
    if FILENAME:        
        messagebox.showinfo(message=f"Successfully imported file: {FILENAME}") #user feedback :)
    else:
        messagebox.showinfo(message="Import failed")    #user feedback :(
    return FILENAME

def exit_program():
    messagebox.showinfo(message="Terminating program...")
    sys.exit()  #kill it

root = tk.Tk()
root.title("Contact Manager App")

#these are just the labels and buttons on the root window.
ttk.Label(root, text="Clayton's Contact Manager App").grid(column=0,row=0,columnspan=2,padx=10,pady=10)
ttk.Button(root, text="Import File", command=import_file).grid(column=0,row=1,columnspan=2)
ttk.Button(root, text="View Contacts", command=view).grid(column=0,row=2,columnspan=2)
ttk.Button(root, text="Add", command=add).grid(column=0,row=3)
ttk.Button(root, text="Delete", command=delete).grid(column=1,row=3)
ttk.Button(root, text="Exit", command=exit_program).grid(column=0,row=5)

root.mainloop()