# 100 best movies scrapper

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
html_data = response.text
soup = BeautifulSoup(html_data, features="html.parser")

sections = soup.find_all(name="section", class_="gallery__content-item")
movies = []

for section in sections:
    title = section.find(name="h3").getText()
    movies.append(title)

movies = movies[::-1]
movies_txt = "\n".join(movies)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write(movies_txt)
