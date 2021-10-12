# import datetime

import requests
import json
import webbrowser


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


menu_items = ['1️⃣ Talk yodish to me', '2️⃣ About the API']
yoda_art = """             
            ::\`--._,'.::.`._.--'/:: 
            ::::.  ` __::__ '  .:::: 
            ::::::-:.`'..`'.:-::::::
            ::::::::\ `--' /::::::::"""


def yoda_get(text):
    parameters = {'text': text}
    url = "https://api.funtranslations.com/translate/yoda.json"
    response = requests.get(url, params=parameters)
    api_data = json.loads(response.content)

    return api_data['contents']

def init():
    # print(yoda_art)

    print(f"{bcolors.OKGREEN}"+ yoda_art + f"{bcolors.ENDC}")

    for menu_item in menu_items:
        print(menu_item)

    menu_select = int(input('Please choose 👉 '))

    if menu_select == 1:
        # Not necessary to convert text
        # word = input('A message for yoda please type in 👉 ').replace(" ","%20")
        text = input('A message for yoda please type in 👉 ')
        print(yoda_get(text)['translated'])

    if menu_select == 2:
        webbrowser.open("https://funtranslations.com/api/yoda")


init()