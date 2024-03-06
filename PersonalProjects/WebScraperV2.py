#this version of WebScraper:
#take user input
#modularize the source code
import requests
from bs4 import BeautifulSoup

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input.strip()

#this block is all redundant with the new get_user_input function
'''def get_user_url():
    url = input("Please enter URL: ")
    return url

def get_user_tags():
    tags = input("Please enter html tags to extract: ")
    return tags.lower()
    
def get_css_class():
    css_Class = input("Please enter css class: ")
    return css_Class.lower()'''

def get_html_content(url):
    response = requests.get(url)
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
    print("Data saved")

def main():
    url = get_user_input("Please enter url: ")
    tags = get_user_input("Please enter html tags to extract: ")
    css_Class = get_user_input("Please enter css class to extract: ")
    
    #fetch html content
    try:
        html_content = get_html_content(url)
    except Exception as e:
        print("Error extracting html content:", e)
        return
    
    #extract headers
    headers = extract_headers(html_content, tags, css_Class)

    #write to file
    file_path = '/Users/AmmonClayton/Documents/GitHub/INFO1200ACSpring2024/extracted_Data.txt'
    try:
        write_to_file(headers, file_path, tags, css_Class)
    except Exception as e:
        print("Error writing data to file:", e)

if __name__ == '__main__':
    main()