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
        #declares each tag as a key, declares classes as values associated with a key. Also converts each classes set into a sorted list.
    return \
        sorted(list(tags_set)), \
        {tag: sorted(list(classes)) for tag, classes in classes_dict.items()}

def scrape_and_return():
    url = input("Enter URL: ")
    
    try:
        html_content = get_html_content(url)
        tags, classes_dict = extract_tags_and_classes(html_content)
        print(tags)
        return html_content, tags, classes_dict
    except Exception as e:
        print('Error', f'Error extracting html content: {e}')
        return

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
    

if __name__ == "__main__":
    main()
