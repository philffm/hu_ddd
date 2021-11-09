from asyncore import poll
import requests
import json
import pandas as pd
import time
# 5 years period in epoch format
end_date = round(time.time())
period = 1119000
start_date = end_date - period



# read access token(s) from auth file
# Idea for futures: loop through different login files after limit exceeded
login = pd.read_csv('auth_owm.csv')

# Auth definitions
api_key = login['api_key'].to_string(index=False)
base_url = 'https://api.openweathermap.org/data/2.5/'

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
loc = "Frankfurt"

# weather = weather['weather']

# df_pollution = pd.DataFrame()
# df_pollution = df_pollution.append(pollution['list'], ignore_index=True)
# df_pollution2 = pd.DataFrame.from_dict(df_pollution['components'])


def get_weather(loc):
    url = "%sweather?q=%s&appid=%s&units=metric" % (base_url, loc, api_key)
    response = requests.get(url)
    weather = json.loads(response.text)
    return weather

def get_pollution(lat, lon):
    weatherdata = get_weather('Frankfurt')
    url  = "%sair_pollution/history?lat=%s&lon=%s&start=%s&end=%s&appid=%s" % (base_url, lat, lon, start_date, end_date, api_key)
    response = requests.get(url)
    pollution = json.loads(response.text)
    return pollution

weather = get_weather('Frankfurt')

# loc = weather['name']
# lat = weather['coord']['lat']
# lon = weather['coord']['lon']


# data.

print('test')

