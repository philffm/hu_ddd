# import datetime

import requests
import json

menu_items = ['1️⃣ 🎲 Random', '2️⃣ Input']

def get_random():
    parameters = {}
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url, params=parameters)
    api_data = json.loads(response.content)
    return api_data["value"]
def get_word(word):
    parameters = {'query': word}
    url = "https://api.chucknorris.io/jokes/search"
    response = requests.get(url, params=parameters)
    api_data = json.loads(response.content)

    return api_data['result']

def init():
    
    for menu_item in menu_items:
        print(menu_item)

    menu_select = int(input('Please choose 👉 '))

    if menu_select == 1:
        print("Your joke for today:", get_random())
    if menu_select == 2:
        query = input('Please input query 👉 ')
        print("Your jokes for the word", query)
        # print(get_word(query))
        for joke in get_word(query):
            print(joke['value'],"\n")


init()