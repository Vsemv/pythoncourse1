# https://quotes.toscrape.com/


import requests
from bs4 import BeautifulSoup



response = requests.get('https://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_= 'quote')

print(quotes)