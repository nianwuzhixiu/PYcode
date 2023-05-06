import requests
from bs4 import BeautifulSoup
url = "http://www.bilibili.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
news_list = soup.find_all("div", class_="news")
for news in news_list:
    title = news.find("a").text
    link = news.find("a")["href"]
    print(title, link)
