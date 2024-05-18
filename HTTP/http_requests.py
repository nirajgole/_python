from urllib import response
import requests
url = 'https://news.ycombinator.com/'
response = requests.get(url)
print(f'Status: {response.status_code} {response.reason}')
