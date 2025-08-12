# 45 Parsing HTML

from bs4 import BeautifulSoup
import requests
import pprint

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, features="html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts, article_links = [], []

for item in articles:
    article_tag = item.find("a")
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(n.getText().split()[0]) for n in soup.find_all("span", class_="score")]
print(article_upvotes)

highest = max(article_upvotes)
highest_index = article_upvotes.index(highest)

print("Max upvotes:")
print(f"{highest}: {article_texts[highest_index]} [{article_links[highest_index]}]")

