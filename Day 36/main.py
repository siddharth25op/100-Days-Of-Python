import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = ""
NEWS_API = ""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

newsParameters = {
    "apikey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
dataList = [value for (key, value) in data.items()]
yesterdayData = dataList[0]
yesterdayClosingPrice = yesterdayData["4. close"]
print(yesterdayClosingPrice)

dayBeforeYesterdayData = dataList[0]
dayBeforeYesterdayClosingPrice = dayBeforeYesterdayData["4. close"]
print(dayBeforeYesterdayClosingPrice)

diff = float(yesterdayClosingPrice) - float(dayBeforeYesterdayClosingPrice)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(diff)

percentage = round((diff / float(yesterdayClosingPrice)) * 100)
print(percentage)

if abs(percentage) > 5:
    news = requests.get(url=NEWS_ENDPOINT, params=newsParameters)
    article = news.json()["articles"]
    three_articles = article[:3]
    print(three_articles)

    formatted_article_list = [f"{STOCK_NAME}: {up_down}{diff}%\nHeadline: {article['title']}, \nBrief: {article['description']}" for article in three_articles]

    account_sid = ""
    auth_token = ""

    client = Client(account_sid, auth_token)

    for article in formatted_article_list:
        message = client.messages.create(
            to="",
            from_="",
            body=article)
