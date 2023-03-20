import requests
from send_email import send_email


topic = 'tesla'
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "from=2023-02-20&"\
    "sortBy=publishedAt&"\
    "apiKey=d5aaf5ab41904581ba2fe2f6ab726da2&"\
    "language=en"
api_key = "d5aaf5ab41904581ba2fe2f6ab726da2"

# Make Request
request = requests.get(url)

# Get Dictionary with Data
content = request.json()
# Get Articles title
body = ''
for article in content['articles'][:20]:

    title = article['title'].encode('ascii', 'ignore').decode('ascii')
    description = article['description'].encode('ascii', 'ignore').decode('ascii')
    if article['title'] is not None:
        body += "Subject: Today's news" +  \
                '\n' + str(title) + \
                '\n' + str(description) + \
                '\n' + article['url'] + \
                 2*'\n'
    print(body)
send_email(body)
# print(type(content))
#
# print(content)