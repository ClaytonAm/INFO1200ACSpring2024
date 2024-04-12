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
    except FileNotFoundError:
        messagebox.showerror(message="Could not find contacts file! Starting new contacts file...")
    
    return contacts

def view():
    global contacts
    contacts = read_contacts()
    if len(contacts) > 0:
        view_contacts_window = tk.Toplevel()
        view_contacts_window.title("Your contacts")
        listbox = tk.Listbox(view_contacts_window, width=50)
        listbox.grid(row=0,column=0,columnspan=4)
        for i, row in enumerate(contacts, start=1):
            listbox.insert(tk.END, f"{i}. {row[0]} - {row[1]} - {row[2]}\n")
    else:
        messagebox.showerror(message="There are no contacts in the list")

def get_contact_number(selected):
    while True:
        try:
            number = selected
        except ValueError:
            messagebox.showerror(message="Invalid integer.\n")
            return -1
            
        if number < 1 or number > len(contacts):
            messagebox.showerror(message="Invalid contact number.\n")
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

root = tk.Tk()
root.title("Contact Manager App")

ttk.Label(root, text="Clayton's Contact Manager App").grid(column=0,row=0,columnspan=2,padx=10,pady=10)
ttk.Button(root, text="Import File", command=import_file).grid(column=0,row=1,columnspan=2)
ttk.Button(root, text="View Contacts", command=view).grid(column=0,row=2,columnspan=2)
ttk.Button(root, text="Add", command=add).grid(column=0,row=3)
ttk.Button(root, text="Delete", command=delete).grid(column=1,row=3)
ttk.Button(root, text="Exit", command=exit_program).grid(column=0,row=5)

root.mainloop()