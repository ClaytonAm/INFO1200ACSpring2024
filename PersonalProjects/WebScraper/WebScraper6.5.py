#this version of WebScraper:
#new ui that doesn't suck
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
from ttkthemes import ThemedStyle
#https://www.scrapethissite.com/pages/forms/

def get_html_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def extract_tags_and_classes(html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    classes_dict = {}           #initializes a new dictionary for the classes
    tags_set = set()

    for tag in soup.find_all(True):
        if tag.get('class'):   
            tag_name = tag.name 
            if tag_name not in classes_dict:
                classes_dict[tag_name] = set()
            for css_class in tag.get('class'): 
                classes_dict[tag_name].add(css_class)
        tags_set.add(tag.name)
    print(classes_dict)
    return \
        sorted(tags_set), \
        {tag_name: sorted(list(classes)) for tag_name, classes in classes_dict.items()}

def scrape_and_return():
    url = url_entry.get()
    try:
        html_content = get_html_content(url)
        tags, classes_dict = extract_tags_and_classes(html_content)

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
    tags_listbox.grid(row=0,column=1, padx=10, pady=10)
    for i in tags:
        tags_listbox.insert(tk.END, i)

    classes_listbox = tk.Listbox(view_classes_window, width=25)
    classes_listbox.grid(row=0,column=2, padx=10, pady=10)

def pull_content(tag_select, classes_select, html_content):
    soup = BeautifulSoup(html_content.text, 'html5lib')
    pulled_content = []

    for element in soup.find_all(tag_select, class_=classes_select, recursive=True):
        pulled_content.append(element.text.strip())

    return '\n'.join(pulled_content)

def write_content(content):
    FILENAME = filedialog.asksaveasfilename(filetypes=[("TXT Files", "*.txt")])

    #this formats the scraped data for writing


    with open(FILENAME, 'w', newline='') as File:
        File.write(content)

def nav_pages(base_url):
    per_page = per_page_entry.get()
    num_pages = num_pages.get()

    for page in range(1, num_pages + 1):
        urls_list = []
        mod_url = f"{base_url}?page_num={page}&per_page={per_page}"
        urls_list.append(mod_url)
    return urls_list

def scrape_pagination(base_url):
    urls_list = nav_pages(base_url)
    response = get_html_content(urls_list[0])
    for url in urls_list:
        if url != urls_list[0]:
            response += get_html_content(url)

root = tk.Tk()
root.title("Web Scraper 6.5")
print("https://www.scrapethissite.com/pages/forms/")

#sets the theme so it doesn't look so bad
THEME_NAME = "equilux"
style = ThemedStyle(root)
style.theme_use(THEME_NAME)

#frame for the initial entry box and button
top_frame = ttk.Frame(root, borderwidth=2, relief="groove")
top_frame.grid(column=0,row=0,columnspan=2,padx=10,pady=2)
ttk.Label(top_frame, text="Web Scraper 6.5").grid(column=0,row=0,columnspan=2,padx=10,pady=10)
url_entry = tk.Entry(top_frame)
url_entry.grid(column=0, columnspan=3, row=1)
ttk.Button(top_frame, text="Get Content", command=scrape_and_return).grid(column=1,row=2)

#buttons frame
buttons_frame = ttk.Frame(root, borderwidth=2, relief="groove")
buttons_frame.grid(column=0,row=1,columnspan=2,padx=10,pady=2)
ttk.Button(buttons_frame,text="View Tags", command=view_tags).grid(column=0, row=2)
ttk.Button(buttons_frame, text="View Classes", command=view_classes).grid(column=1,row=2)
ttk.Button(buttons_frame, text="Write", command=write_content).grid(column=0,row=3)

#pagination frame
pagination_frame = ttk.Frame(root, borderwidth=2, relief="groove")
pagination_frame.grid(column=0,row=2,columnspan=2,padx=10,pady=2)
ttk.Label(pagination_frame, text="Results per page:").grid(column=0, row=0)
per_page_entry = ttk.Entry(pagination_frame)
per_page_entry.grid(column=1,row=0)
ttk.Label(pagination_frame, text="Pages: ").grid(column=0, row=1)
num_pages = ttk.Entry(pagination_frame)
num_pages.grid(column=1,row=1)


# ttk.Button(root, text="Exit", command=exit_program).grid(column=0,row=5)

root.mainloop()