import requests
from send_email import send_email


api_key = "b45bf6128ec44bbaa2f9b24706eef0c4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-19&sortBy=publishedAt&apiKey=b45bf6128ec44bbaa2f9b24706eef0c4&language=en"


# Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Acces the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"


body = body.encode("utf-8")
send_email(message=body)

