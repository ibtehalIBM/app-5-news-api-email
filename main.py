import requests

url = "https://newsapi.org/v2/everything"\
      "?q=tesla&from=2023-02-17&sortBy=publishedAt&"\
      "apiKey=d5aaf5ab41904581ba2fe2f6ab726da2"
api_key = "d5aaf5ab41904581ba2fe2f6ab726da2"

# Make Request
request = requests.get(url)

# Get Dictionary with Data
content = request.json()
# Get Articles title
for article in content['articles']:
    print(article['title'])
    print(article['description'])
# print(type(content))
#
# print(content)