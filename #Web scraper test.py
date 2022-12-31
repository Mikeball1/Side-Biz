#Web scraper test
import webbrowser
import requests
from bs4 import BeautifulSoup



url = 'https://www.toysrus.ca/en/toysrus/Brands/F/Funko?srule=recently-added&start=0&sz=24'
webbrowser.open(url)

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract the data you want from the page
data = soup.find_all('div', class_='data-container')
print(data)