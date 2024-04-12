#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.
import csv

def display_title():
    print("Clayton's Monthly Sales")
    print()

def display_menu():
    print("COMMAND MENU")
    print()
    print("monthly - View monthly sales")
    print("yearly  - View yearly summary")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program")
    print()

def read_sales():
    sales = []      #empty list
    with open("monthly_sales.csv", newline="") as file:     #opens the file so we can mess with it
        reader = csv.reader(file)       #csv writer object
        for row in reader:      #iterate through each row in the csv
            sales.append(row)   #add each line of the csv to the list
    
    return sales

def main():
    display_title()
    display_menu()

    sales = read_sales()

    while True:        #this is just a basic menu thing
        command = input("Command: ")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "yearly":
            view_yearly_summary(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

def view_monthly_sales(sales):
    for row in sales:       #iterate through each entry in the sales list
        print(f"{row[0]} - {row[1]}")       #print a functional string with name of month and the sales amount

def view_yearly_summary(sales):
    total = 0
    for row in sales:       #iterate through each entry in the sales list
        amount = int(row[1])    #add up all of the values for that year
        total += amount

    count = len(sales)  #counts how many monthly entries are in the list
    
    average = total / count     #calculates average and rounds
    average = round(average, 2)

    print("Yearly total:    ", total)
    print("Monthly average: ", average)        
    print()

def edit(sales):
    names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]   
    name = input("Please enter a 3-letter month name: ")
    name = name.title() #makes the entry not case-sensitive
    if name in names:   #if the user-entered name is in the list,
        index = names.index(name)   #get the index for the month they entered
        amount = int(input("Sales Amount:"))    #user input for sales amount
        month = []      #empy list
        month.append(name)      #add the name they entered
        month.append(str(amount))   #add the amount they entered
        sales[index] = month   
        write_sales(sales)
        print(f"Sales amount for {month[0]} was modified")
        print()
    else:
        print("Invalid 3-letter month name")

def write_sales(sales):
    with open("monthly_sales.csv", "w", newline="") as file:    #pop the hood, let's take a look
        writer = csv.writer(file)       #csv writer object
        writer.writerows(sales)     #write em

if __name__ == "__main__":  main()