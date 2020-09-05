import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

td = soup.find_all('td', class_='titleColumn')
td_rating = soup.find_all('td',class_="ratingColumn imdbRating")


# for rating in td_rating:
#     rate = rating.strong.text


for i in td:

    anchor = i.find_all('a')
    # print(i.a.text)
    for link in anchor:
        if link.get('href') != None:
            links = "https://www.imdb.com" + link.get('href')
            print(f"{i.a.text} -->> {links}" )