import csv, sys
import tkinter as tk
from tkinter import ttk, messagebox

FILENAME = "movies.csv"

def exit_program():
    messagebox.showinfo("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        return movies
    except Exception as e:
        messagebox.showerror(type(e), e)

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        messagebox.showerror(type(e), e)

def list_movies(movies):
    movies = read_movies()
    for i, movie in enumerate(movies, start=1):
        messagebox.showinfo(f"{i}. {movie[0]} ({movie[1]})\n")
    
def add_movie(movies):
    def save_movie():
        name = name_entry.get()
        year = year_entry.get()
        try:
            year = int(year)
            if year <= 0:
                raise ValueError("Invalid year")
        except Exception as e:
            messagebox.showerror(type(e), e)
            return

        movie = [name, year]
        movies.append(movie)
        write_movies(movies)
        messagebox.showinfo(f"{name} was added.\n")
    
    add_window = tk.Toplevel(root)
    add_window.title("Add Movie")

    tk.Label(add_window, text="Name: ").grid(column=0, row=1)
    name_entry = tk.Entry(add_window)
    name_entry.grid(column=1, row=1)

    tk.Label(add_window, text="Year:").grid(column=0, row=2)
    year_entry = tk.Entry(add_window)
    year_entry.grid(column=1,row=2)

    tk.Button(add_window, text="Save", command=save_movie).grid(column=1,row=3)

def delete_movie(movies):
    def delete_selected_movie
        while True:
            try:
                number = int(input("Number: "))
            except ValueError:
                print("Invalid integer. Please try again.")
                continue
            if number < 1 or number > len(movies):
                print("There is no movie with that number. Please try again.")
            else:
                break
        movie = movies.pop(number - 1)
        write_movies(movies)
        print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

root = tk.TK()
root.title("The Movies List Program")

ttk.Button(root, text="List Movies", command=list_movies)
ttk.Button(root, text="Add", command=add_movie)
ttk.Button(root, text="Delete")