from urllib import response
import requests
from bs4 import BeautifulSoup
import csv

# * url
response = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')

# ? This will download CSV file containing data about blog posts
with open('blog_data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Link', 'Date'])
    for article in articles:
        a_tag = article.find('a')
        title = a_tag.get_text()
        url = 'https://www.rithmschool.com'+a_tag.get('href')
        date = article.find('time').get('datetime')
        csv_writer.writerow([title, url, date])
