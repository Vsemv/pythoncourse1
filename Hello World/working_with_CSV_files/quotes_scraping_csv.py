# https://quotes.toscrape.com/


import requests
from bs4 import BeautifulSoup
import csv



# response = requests.get('https://quotes.toscrape.com/')
# html_data = BeautifulSoup(response.text)
# quotes = html_data.find_all(class_='quote')

# with open('quotes.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for quote in quotes:
#         text = quote.find(class_='text')
#         print(text.get_text())
#         writer.writerow(text.get_text())



response = requests.get('https://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_= 'quote')

with open('quotes.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['text', 'Author', 'Keywords'])
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        keywords = quote.find(class_='keywords')['content']
        csv_writer.writerow([text, author, keywords])