import requests
from bs4 import BeautifulSoup


def check_game_name(game_entry, user_input):
    name = game_entry.contents[1].contents[3].contents[1].contents[5].contents[1].text
    name = name.replace("\n", "")
    name = name.strip()
    if user_input == name:
        return True
    return False

def get_available_plats(res_list, user_input, user_agent):
    initial_plat = res_list[0].contents[1].contents[3].contents[1].contents[7].contents[1].text
    platforms = [initial_plat]
    game_url = res_list[0].contents[1].contents[3].contents[1].contents[5].contents[1].attrs['href']
    game_url = "https://www.metacritic.com" + game_url
    page = requests.get(game_url, headers=user_agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find_all("li", class_="product_platforms")
    entries = res[0].contents[3].contents

    for content in entries:
        if content != "\n" and " " not in content:
            platforms.append(content.text)

    return platforms

url = "https://www.metacritic.com/search/game/GAMENAME/results"
user_agent = {'User-agent': 'Mozilla/5.0'}

# to showcase user input replacing the game name
url = url.replace("GAMENAME", "Elden%20Ring")
page = requests.get(url, headers=user_agent)
soup = BeautifulSoup(page.content, 'html.parser')
res = soup.find_all("li", class_="result")
res_list = []

for game in res:
    res_list.append(game)

plats = get_available_plats(res_list, "Elden Ring", user_agent)