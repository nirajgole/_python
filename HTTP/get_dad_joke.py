import requests
dad_joke_url = 'https://icanhazdadjoke.com/'

# *DATA-FORMAT: plain-text
# response = requests.get(dad_joke_url, headers={'Accept': 'text/plain'})
# print(response.text)
# print(type(response.text))

# *DATA-FORMAT: json
# response = requests.get(dad_joke_url, headers={'Accept': 'application/json'})
# print(response.json())
# data = response.json()
# print(type(data))
# print(data['joke'])

# *Query-parameters
# search dad joke using search keywords
search_term = 'dog'
response = requests.get(f'{dad_joke_url}/search',
                        headers={'Accept': 'application/json'}, params={'term': search_term, 'limit': 2})
data = response.json()
print(data['results'])
