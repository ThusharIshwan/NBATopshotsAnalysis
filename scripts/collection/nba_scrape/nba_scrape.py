import requests
from bs4 import BeautifulSoup
from nba_api.stats.static import players

def get_player_id(name):
    return players.find_players_by_full_name(name)[0]['id']


def get_pie(name):
    id = get_player_id(name)
    r = requests.get(url=f"https://www.nba.com/stats/player/{id}").text
    start_index = r.find("\"PIE\":")
    fin_index = r.find("}",start_index)
    print(r[start_index+6: fin_index])


def get_salary_data():
    url="https://hoopshype.com/salaries/players/"
    r = requests.get(url,timeout=2.5)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    salary_table = soup.find('table')
    length=len(salary_table.find_all("td"))
    player_names=[salary_table.find_all("td")[i].text.strip() for i in range(9,length,8)]
    player_salaries =[salary_table.find_all("td")[i].text.strip() for i in range(10,length,8)]
    player_salary_dict = dict(zip(player_names,player_salaries))
    return player_salary_dict
