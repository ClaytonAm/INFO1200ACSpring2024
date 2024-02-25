import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html5lib')

countries = soup.find_all('div', class_='col-md-4 country', recursive=True)

file_path = '/Users/AmmonClayton/Documents/GitHub/INFO1200ACSpring2024/country_titles.txt'

try:
    with open(file_path, 'w',encoding="utf-8") as file:
        for country in countries:
           
            country_name = country.find('h3', class_='country-name').text.strip()
            
            capital = country.find('span', class_='country-capital').text.strip()
            
            population = country.find('span', class_='country-population').text.strip()
            
            area = country.find('span', class_='country-area').text.strip()

            file.write(f"Country: {country_name}\nCapital: {capital}\nPopulation: {population}\nArea: {area}\n\n")
        print("Data saved")
except Exception as e:
    print("An error occurred:", e)
