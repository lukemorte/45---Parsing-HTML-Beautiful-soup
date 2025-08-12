# 45 Parsing HTML

from bs4 import BeautifulSoup
import requests
import pprint

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, features="html.parser")
print(soup.prettify())