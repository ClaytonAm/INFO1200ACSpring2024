#this version of WebScraper:
#To-do:
#pagination

import requests
from bs4 import BeautifulSoup
import WSModule as ws
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class web_scraper_V6(ttk.frame):
    def __init__(self):
        
        ttk.Frame.__init__(self, width=150, height=100, padding="10 10 10 10")
        
        self.initComponents()

    def initComponents(self):
        #tell the user to enter whichever sides they want
        ttk.Label(self, text="Enter 2 unknown sides").grid(columnspan=2, row=0, sticky=tk.EW)
        
        #declare the variables to be used later
        #sets default values to 0
        self.sideA = tk.IntVar(value=0)
        self.sideB = tk.IntVar(value=0)
        self.sideC = tk.IntVar(value=0)
        self.unknownSide = tk.IntVar()

        #make input fields
        self.createInputFields()
       
        #make the buttons
        self.makeButtons()

    def scrape_and_return():
        url = input("Enter URL: ")
        
        try:
            html_content = ws.get_html_content(url)
            tags, classes_dict = ws.extract_tags_and_classes(html_content)
            print(tags)
            return html_content, tags, classes_dict
        except Exception as e:
            print('Error', f'Error extracting html content: {e}')
            return

    def pull_content(tag_select, classes_select, html_content):
        soup = BeautifulSoup(html_content.text, 'html5lib')
        pulled_content = []

        for element in soup.find_all(tag_select, class_=classes_select, recursive=True):
            pulled_content.append(element.text.strip())

        return '\n'.join(pulled_content)

    def main():
        print("https://www.scrapethissite.com/pages/simple/")
        html_content, tags, classes_dict = scrape_and_return()
        
        process_user_selection()
        '''choice = "y"

        while choice.lower() == "y": 
            selection = input("Get classes or select tag?(g/s): ")
            if selection.lower() == "g":
                tag_get = input("Enter HTML tag: ")
                print(f"Associated classes: {ws.pull_classes_from_dict(tag_get, classes_dict)}")
            elif selection.lower() == "s":
                tag_get = input("Enter HTML tag: ")
                print(f'Associated classes: {ws.pull_classes_from_dict(tag_get, classes_dict)}')
                
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
        
        #pull_class_from_dict(tags, classes_dict)'''
    def process_user_selection():
        
        choice = "y"
        while choice.lower() == "y": 
            #this entire if statement would be redundant.
            #instead build checklist for tags that updates classes display in real time
            selection = input("Get classes or select tag?(g/s): ")
            if selection.lower() == "g":
                tag_get = input("Enter HTML tag: ")
                print(f"Associated classes: {ws.pull_classes_from_dict(tag_get, classes_dict)}")
            elif selection.lower() == "s":
                tag_get = input("Enter HTML tag: ")
                print(f'Associated classes: {ws.pull_classes_from_dict(tag_get, classes_dict)}')
                
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
    def ScraperFrame(root):
        scraperFrame = ttk.Frame()
        
        url = tk.StringVar()
        tag_get = tk.StringVar()
        classes_selection = tk.StringVar()
        
        initComponents()

    def initComponents():
    
        url_entry()
        #url entry
        ttk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(root, width=50, textvariable=root.url).grid(row=0, column=1, padx=5, pady=5)
    
        ttk.Button(root, text="Fetch Tags and Classes", command=scrape_and_return).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        #tags frame
        tags_frame = ttk.Frame(root).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        #classes frame
        classes_frame = ttk.Frame(root).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        #tags label
        ttk.Label(tags_frame, text="HTML Tags:").pack(side=tk.TOP, padx=5, pady=5)

        #tags listbox
        tags_scrollbar = ttk.Scrollbar(tags_frame, orient=tk.VERTICAL)
        tags_listbox = tk.Listbox(tags_frame, yscrollcommand=tags_scrollbar.set)
        tags_scrollbar.config(command=tags_listbox.yview)
        tags_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tags_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #classes label
        ttk.Label(classes_frame, text="CSS Classes:").pack(side=tk.TOP, padx=5, pady=5)

        #classes listbox
        classes_scrollbar = ttk.Scrollbar(classes_frame, orient=tk.VERTICAL)
        classes_listbox = tk.Listbox(classes_frame, yscrollcommand=classes_scrollbar.set)
        classes_scrollbar.config(command=classes_listbox.yview)
        classes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        classes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Web Scraper V6")
    web_scraper_V6()
    root.mainloop()

#Create frame


#Create buttons





