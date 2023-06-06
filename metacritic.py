import requests
from bs4 import BeautifulSoup

url = "https://www.metacritic.com/search/all/GAMENAME/results"
user_agent = {'User-agent': 'Mozilla/5.0'}

# to showcase user input replacing the game name
url = url.replace("GAMENAME", "Elden%20Ring")
page = requests.get(url, headers=user_agent)
soup = BeautifulSoup(page.content, 'html.parser')
res = soup.find_all("li", class_="result")
res_list = []

for game in res:
    res_list.append(game)

print(res_list[0])