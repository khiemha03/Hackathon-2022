from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import os

CRIME_KEYWORD = ["kill","death","shoot","abusing","abuse","attack", "assault", "die","murder", "gun", "kidnap", "robber"]

WEATHER_KEYWORD = ["hurricane", "storm", "cold", "hot", "snow", "rain", "wind", "freeze", "flood", "drought", "heat",
                   "winter", "summer", "spring", "autumn", "fall", "climate", "temperature", "frost", "fire"]

HEALTH_KEYWORD = ["virus", "covid", "death", "symptom", "flu", "hospital", "health", "mental", "treat", "vaccine",
                  "children", "sick", "CDC", "FDA" ]
#CNN CRIME NEWS
CNN_CRIME_LINK = "https://www.cnn.com/specials/us/crime-and-justice"
cnn_crime_articles = []
cnn_crime_web = requests.get(CNN_CRIME_LINK).text
cnn_crime_soup = BeautifulSoup(cnn_crime_web, "html.parser")
cnn_articles = cnn_crime_soup.find_all(class_="cd__headline-text vid-left-enabled")
for article in cnn_articles:
    for keyword in CRIME_KEYWORD:
        if keyword.upper() in article.getText().upper():
            if article.getText() not in cnn_crime_articles:
                cnn_crime_articles.append(article.getText())

#CNN WEATHER NEWS
CNN_WEATHER_LINK = "https://www.cnn.com/specials/us/energy-and-environment"
cnn_weather_articles = []
cnn_weather_web = requests.get(CNN_WEATHER_LINK).text
cnn_weather_soup = BeautifulSoup(cnn_weather_web, "html.parser")
cnn_articles = cnn_weather_soup.findAll(class_="cd__headline-text vid-left-enabled")
for article in cnn_articles:
    for keyword in WEATHER_KEYWORD:
        if keyword.upper() in article.getText().upper():
            if article.getText() not in cnn_weather_articles:
                cnn_weather_articles.append(article.getText())


#CNN HEALTH NEWS
CNN_HEALTH_LINK = "https://www.cnn.com/health"
cnn_health_articles = []
cnn_health_web = requests.get(CNN_HEALTH_LINK).text
cnn_health_soup = BeautifulSoup(cnn_health_web, "html.parser")
cnn_articles = cnn_health_soup.findAll(class_="cd__headline-text vid-left-enabled")
for article in cnn_articles:
    for keyword in HEALTH_KEYWORD:
        if keyword.upper() in article.getText().upper():
            if article.getText() not in cnn_health_articles:
                cnn_health_articles.append(article.getText())
# Twilio sending message
account_sid = os.getenv("SID")
auth_token = os.getenv("AUTH_KEY")
client = Client(account_sid, auth_token)
PHONE_NUMBER = '+18328984006'
content = f'''
Here is the new for today:
CRIME:
1.{cnn_crime_articles[0]}
2.{cnn_crime_articles[1]}
3.{cnn_crime_articles[2]}
WEATHER:
1.{cnn_weather_articles[0]}
2.{cnn_weather_articles[1]}
3.{cnn_weather_articles[2]}
HEALTH:
1.{cnn_health_articles[0]}
2.{cnn_health_articles[1]}
3.{cnn_health_articles[2]}
'''
message = client.messages.create(
                              messaging_service_sid='MG87a354014d7bb9774b9525b4a8ff27c0',
                              body=content,
                              to= PHONE_NUMBER
                          )
print(content)

