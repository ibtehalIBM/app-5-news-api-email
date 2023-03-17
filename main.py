import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything"\
      "?q=tesla&from=2023-02-17&sortBy=publishedAt&"\
      "apiKey=d5aaf5ab41904581ba2fe2f6ab726da2"
api_key = "d5aaf5ab41904581ba2fe2f6ab726da2"

# Make Request
request = requests.get(url)

# Get Dictionary with Data
content = request.json()
# Get Articles title
body = ''
for article in content['articles']:

    title = article['title']
    description = article['description']
    if article['title'] is not None:
        body += article['title'] + '\n' + article['description'] + 2*'\n'
    print(body)
send_email(body)
# print(type(content))
#
# print(content)