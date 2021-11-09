import requests
import json
import pandas as pd


# read access token(s) from auth file
# Idea for futures: loop through different login files after limit exceeded
login = pd.read_csv('auth_walkscore.csv')

# Auth definitions
api_key = login['api_key'].to_string(index=False)


def get_walkscore(loc, lat, lon):
    url  = "https://api.walkscore.com/score?format=json&address=%s&lat=%s&lon=%s&transit=1&bike=1&wsapikey=%s" % (loc, lat, lon, api_key)

    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    return data


# get_walkscore('Frankfurt', 50.1109, 8.6821)

print('test')