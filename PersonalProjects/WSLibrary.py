import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def extract_tags_and_classes(html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    tags_set = set()            #initializes a new set for the html tags
    classes_dict = {}           #initializes a new dictionary for the classes

    for tag in soup.find_all(True): #iterates through html content, assigns values to tag
        tags_set.add(tag.name)      #adds each new html tag to the tags_set
        if tag.get('class'):        #if the html tag has an associated css class
            for css_class in tag.get('class'):        #iterate through each css class associated with the tag, assign to css_class
                if tag.name not in classes_dict:      #if the html tag is not already in the dictionary as a key, 
                    classes_dict[tag.name] = set()    #add the html tag as a key to the dictionary
                classes_dict[tag.name].add(css_class) #add the css class to the dictionary with its associated html tag as the key
    
    #returns 2 things:
        #converts tags_set into a list, and sorts it
        #declares tag as key, declares classes as values associated with a key. Also converts each classes set into a sorted list.
    return \
        sorted(list(tags_set)), \
        {tag: sorted(list(classes)) for tag, classes in classes_dict.items()}

def display_tags_and_classes(tags, classes_dict):
    tags_listbox.delete(0, tk.END)
    classes_listbox.delete(0, tk.END)

    for tag in tags:
        tags_listbox.insert(tk.END, tag)
    
    for tag, classes in classes_dict.items():
        for css_class in classes:
            classes_listbox.insert(tk.END, css_class)
            

'''def scrape_and_save():
    url = url_entry.get()
    
    #fetch html content
    try:
        html_content = ws.get_html_content(url)
        tags, classes_dict = ws.extract_tags_and_classes(html_content)
        display_tags_and_classes(tags, classes_dict)
        return html_content, tags, classes_dict
    except Exception as e:
        messagebox.showerror('Error', f'Error extracting html content: {e}')
        return
    '''