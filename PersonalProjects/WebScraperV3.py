 #this version of WebScraper:
#use tkinter to make a basic UI
#UI for user input
#UI for error messages
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

'''def get_user_input(prompt):
    user_input = input(prompt)
    return user_input.strip()'''

def get_html_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def extract_headers(html_content, tags, css_Class):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    headers = soup.find_all(tags, class_=css_Class, recursive=True)
    headers_data = []
    for header in headers:
            header_text = header.text.strip()
            headers_data.append({'Text': header_text})
    return headers_data

def write_to_file(headers_data, file_path, tags, css_Class):
    with open(file_path, 'w',encoding="utf-8") as file:
            for header in headers_data:
                file.write(f"Text: {header['Text']}\n")
    messagebox.showinfo("Success!", "Data saved")

def scrape_and_save():
    url = url_entry.get()
    tags = tags_entry.get()
    css_Class = class_entry.get()
    
    #fetch html content
    try:
        html_content = get_html_content(url)
    except Exception as e:
        messagebox.showerror('Error', f'Error extracting html content: {e}')
        return
    
    #extract headers
    headers = extract_headers(html_content, tags, css_Class)

    #write to file
    file_path = '/Users/AmmonClayton/Documents/GitHub/INFO1200ACSpring2024/extracted_Data.txt'
    try:
        write_to_file(headers, file_path, tags, css_Class)
    except Exception as e:
        messagebox.showerror('Error', f'Error writing data to file: {e}')

root = tk.Tk()
root.title("Web Scraper 3.0")

url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1)

tags_label = tk.Label(root, text="HTML tags:")
tags_label.grid(row=1, column=0)
tags_entry = tk.Entry(root, width=50)
tags_entry.grid(row=1, column=1)

class_label = tk.Label(root, text="CSS class:")
class_label.grid(row=2, column=0)
class_entry = tk.Entry(root, width=50)
class_entry.grid(row=2, column=1)

scrape_button = tk.Button(root, text="Scrape and Save", command=scrape_and_save)
scrape_button.grid(row=3, column=0, columnspan=2)

root.mainloop()