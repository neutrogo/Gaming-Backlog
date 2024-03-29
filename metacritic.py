import requests
from datetime import datetime as DT
from bs4 import BeautifulSoup

def check_game_name(game_entry, user_input):
    """checks if the given game has an entry on metacritic"""
    name = game_entry.contents[1].contents[3].contents[1].contents[5].contents[1].text
    name = name.replace("\n", "")
    name = name.strip()
    if user_input == name:
        return True
    return False

def get_available_plats(res_list, user_input, user_agent):
    """gets all the platforms that the given game is available on"""
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

def get_user_score(game, plat, soup):
    """gets the user review score for the given game & platform"""
    user_score = soup.select_one("div.metascore_w.user").text
    return {"user_score": user_score}

def get_critic_score(game, plat, soup):
    """gets the critic review score for the given game & platform"""
    critic_score = soup.select_one("div.metascore_w.xlarge").text
    return {"critic_score": critic_score}

def get_publisher_name(game, plat, soup):
        """gets the publisher for the given game & platform"""
        pub = soup.find_all("li", class_="summary_detail publisher")[0].contents[3].contents[1].text
        pub = pub.replace("\n", "")
        pub = pub.strip()
        return {"publisher": pub}

def get_release_date(game, plat, soup):
    """gets the release date for the given game & platform"""
    date = soup.find_all("li", class_="summary_detail release_data")[0].contents[3].text.replace(",", "")
    date = DT.strptime(date, "%b %d %Y").strftime("%d/%m/%Y")
    return {"date": date}

def get_game_developer(game, plat, soup):
    """gets the game developer for the given game & platform"""
    dev = soup.find_all("li", class_="summary_detail developer")[0].contents[3].contents[1].text
    return {"dev": dev}

def get_game_genre(game, plat, soup):
    #currently only gets the first genre, potentially update
    genre = soup.find_all("li", class_="summary_detail product_genre")[0].contents[3].text
    return {"genre": genre}

def get_game_details(game, plat, user_agent):
    """gets all necessary game details from metacritic and returns them as a dictionary"""
    details = {}
    game, plat = convert_name_to_path(game, plat)
    soup = get_soup(user_agent, game, plat)
    details.update(get_user_score(game, plat, soup))
    details.update(get_critic_score(game, plat, soup))
    details.update(get_publisher_name(game, plat, soup))
    details.update(get_release_date(game, plat, soup))
    details.update(get_game_developer(game, plat, soup))
    details.update(get_game_genre(game, plat, soup))
    return details

def get_soup(user_agent, game, plat):
    """creates and returns a BeautifulSoup object for the given url"""
    url = f"https://www.metacritic.com/game/{plat}/{game}"
    page = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def convert_name_to_path(game, plat):
    """Turns game and platform names to useable metacritic paths"""
    game = game.replace(" ", "-").lower()
    plat = plat.replace(" ", "-").lower()
    return (game, plat)
    
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
details = get_game_details("Elden Ring", "Playstation 5", user_agent)
print(details)
