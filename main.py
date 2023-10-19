import requests


api_key = "b45bf6128ec44bbaa2f9b24706eef0c4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-19&sortBy=publishedAt&apiKey=b45bf6128ec44bbaa2f9b24706eef0c4"


# Make a request
request = requests.get(url)

#Get a dictionary with dara
content = request.json()

# Acceses the article title and description
for article in (content["articles"]):
    print(article["title"])
    print(article["description"])
