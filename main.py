# 45 Parsing HTML

from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, features="html.parser")

test = soup.find_all("a")
for item in test:
    print(item.attrs["href"])
    