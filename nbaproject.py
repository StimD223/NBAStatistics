#Quinn Panos  9-8-2023

import json
import requests

firstname = str(input("First Name:"))
lastname = str(input("Last Name:"))


response = requests.get(f"https://www.balldontlie.io/api/v1/players/?search={firstname}_{lastname}")

idata = response.json()["data"][0]

id = idata["id"]
first_name = idata["first_name"]
last_name = idata["last_name"]

season = str(input("Season:"))

responsei = requests.get(f"https://www.balldontlie.io/api/v1/season_averages?season={season}&player_ids[]={id}")

idatai = responsei.json()["data"][0]

games_played = idatai["games_played"]
mins = idatai["min"]
pts = idatai["pts"]

fga = idatai["fga"]
fgm = idatai["fgm"]
fg3a = idatai["fg3a"]
fg3m = idatai["fg3m"]

reb = idatai["reb"]
ast = idatai["ast"]
stl = idatai["stl"]
blk = idatai["blk"]
turnover = idatai["turnover"]

print(f"In {season}, {first_name} {last_name} played {games_played} game(s) and was on the court for an average of {mins} minute(s) per game.")
print(f"He shot {fga} field goals a game and made {fgm} of them. He also shot {fg3a} three pointers a game and made {fg3m} of them.")
print(f"Per game, {first_name} got {reb} rebound(s), {ast} assist(s), {stl} steal(s), {blk} block(s), and {turnover} turnover(s).")