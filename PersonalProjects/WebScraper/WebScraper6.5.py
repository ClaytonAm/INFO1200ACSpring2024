#this version of WebScraper:
#got rid of UI because fuck that
#displays list of html tags
#user selection of html tags
#displays corresponding css classes
#user selection of css class
#write to txt all content from user selected html tag+css class

import requests
from bs4 import BeautifulSoup
import WSModule as ws
import tkinter as tk
from tkinter import ttk, messagebox, filedialog 

def get_html_content(url):
    html_content = requests.get(url)
    html_content.raise_for_status()
    return html_content

def build_classes_dict(html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    classes_dict = {}           #initializes a new dictionary for the classes

    for tag in soup.find_all(True):
        if tag.get('class'):   
            tag_name = tag.name 
            if tag_name not in classes_dict:
                classes_dict[tag_name] = set()
            for css_class in tag.get('class'): 
                classes_dict[tag_name].add(css_class)
    print(classes_dict)
    return {tag_name: sorted(list(classes)) for tag_name, classes in classes_dict.items()}

def extract_tags(html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    tags_set = set()  
    for tag in soup.find_all(True):
        tags_set.add(tag.name)
    return sorted(tags_set)

def scrape_and_return():
    url = url_entry.get()
    try:
        html_content = get_html_content(url)
        tags = extract_tags(html_content)
        classes_dict = build_classes_dict(html_content)

        print(tags)
        return html_content, tags, classes_dict
    except Exception as e:
        print('Error', f'Error extracting html content: {e}')
        return
    
def view_tags():
    html_content, tags, classes_dict = scrape_and_return()

    view_tags_window = tk.Toplevel(root)
    view_tags_window.title("View Tags")

    listbox = tk.Listbox(view_tags_window, width=50)
    listbox.grid(row=0,column=0,columnspan=4)
    for i in tags:
        listbox.insert(tk.END, i)

def view_classes():
    html_content, tags, classes_dict = scrape_and_return()
    def insert_classes():
        tag = tag_entry.get()
        classes_listbox.delete(0, tk.END)
        if tag in classes_dict:
            for i in classes_dict[tag]:
                classes_listbox.insert(tk.END, i)

    view_classes_window = tk.Toplevel(root)
    view_classes_window.title("View Classes")

    ttk.Label(view_classes_window, text="Enter tag:").grid(column=0,row=0)
    tag_entry = ttk.Entry(view_classes_window)
    tag_entry.grid(column=0,row=1)
    ttk.Button(view_classes_window, text="enter", command=insert_classes).grid()

    tags_listbox = tk.Listbox(view_classes_window, width=25)
    tags_listbox.grid(row=0,column=1)
    for i in tags:
        tags_listbox.insert(tk.END, i)

    classes_listbox = tk.Listbox(view_classes_window, width=25)
    classes_listbox.grid(row=0,column=2)

def pull_classes_from_dict(keys, dictionary):
    
    if keys in dictionary:
        return dictionary[keys]
    else:
        return None

def pull_content(tag_select, classes_select, html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    pulled_content = []

    for element in soup.find_all(tag_select, class_=classes_select, recursive=True):
        pulled_content.append(element.text.strip())

    return '\n'.join(pulled_content)

def main():
    print("https://www.scrapethissite.com/pages/forms/")
    html_content, tags, classes_dict = scrape_and_return()
    choice = "y"

    while choice.lower() == "y": 
        selection = input("Get classes or select tag?(g/s): ")
        if selection.lower() == "g":
            tag_get = input("Enter HTML tag: ")
            print(f"Associated classes: {pull_classes_from_dict(tag_get, classes_dict)}")
        elif selection.lower() == "s":
            tag_get = input("Enter HTML tag: ")
            print(f'Associated classes: {pull_classes_from_dict(tag_get, classes_dict)}')
            
            classes_selection = input("Enter css class to select: ")
            pulled_content = pull_content(tag_get, classes_selection, html_content)
           
            choice = input("Write to file?(y/n): ")
            if choice.lower() == "y":
                print("/Users/AmmonClayton/Documents/GitHub/INFO1200ACSpring2024/scraped.txt")
                file_path = '/Users/AmmonClayton/Documents/GitHub/INFO1200ACSpring2024/scraped.txt'
                try:
                    with open(file_path, 'w',encoding="utf-8") as file:
                        file.write(pulled_content)
                        print("Data saved")
                except Exception as e:
                    print("An error occurred:", e)
            else:
                break
        else:
            print("Please enter a valid selection.")
    

root = tk.Tk()
root.title("Web Scraper 6.5")

#these are just the labels and buttons on the root window.
ttk.Label(root, text="Web Scraper 6.5").grid(column=0,row=0,columnspan=2,padx=10,pady=10)
url_entry = tk.Entry(root)
url_entry.grid(column=0, columnspan=2, row=1)
ttk.Button(root, text="Get Content", command=scrape_and_return).grid(column=2,row=1)

ttk.Button(root,text="View Tags", command=view_tags).grid(column=0, row=2)

ttk.Button(root, text="View Classes", command=view_classes).grid(column=1,row=2)

# ttk.Button(root, text="Write", command=write_content).grid(column=0,row=3)

# ttk.Button(root, text="Delete", command=delete).grid(column=1,row=3)
# ttk.Button(root, text="Exit", command=exit_program).grid(column=0,row=5)

root.mainloop()