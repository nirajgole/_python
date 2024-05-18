import requests as req
import argparse

parser = argparse.ArgumentParser(description="Finds the stadiums")
parser.add_argument("team", metavar="team", type=str, help="Enter your team")
args = parser.parse_args()
team = args.team
url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={team}"

r = req.get(url)
print(r)
data = r.json()
print(data["teams"][0]["strStadium"])

# How to do it?
# on console type -> py -m arg_parser "manchester city"