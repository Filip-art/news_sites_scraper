from bs4 import BeautifulSoup
import requests

url = "https://www.seznam.cz/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

main = doc.main
news_div = main.div(class_="article")

news_dict = {}

for news in news_div[4:12]:
    links = (news.a['href'])
    news = news.a.string

    news_dict[news] = links

for news in news_dict.items():
    message_to_send = (f"{news[0]}\n{news[1]}")

    print(message_to_send)

    TOKEN = "YOUR TOKEN HERE"

    chat_ID = "YOUR CHAT ID HERE"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_ID}&text={message_to_send}"

    print(requests.get(url).json())
