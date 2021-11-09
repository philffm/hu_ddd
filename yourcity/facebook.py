# from seleniumwire import webdriver  # Import from seleniumwire


    # import undetected_chromedriver.v2 as uc
    # import time 
    # import pickle

    # username = "bogdan.glazkov@bratista.com"
    # password = "Banan15ta!"



    # # # Auth definitions
    # # username = login['consumer_key'].to_string(index=False)
    # # password = login['consumer_secret'].to_string(index=False)

    # pickle.dump( uc.get_cookies() , open("cookies.pkl","wb"))


    # # from seleniumwire import webdriver  # Import from seleniumwire



    # options = uc.ChromeOptions()
    # brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    # options.binary_location = brave_path
    # # options.add_argument("--incognito")
    # # options.add_argument("--no-default-browser-check")
    # options.add_argument("--no-first-run")

    # elements_to_remove = ['sidebar']


    # driver = uc.Chrome(options=options)
    # with driver:
    #     driver.get('https://www.facebook.com/search/top?q=radfahrer%20frankfurt')  # known url using cloudflare's "under attack mode"
    #     driver.execute_script("""
    #     var l = document.getElementById('global-header');
    #     l.parentNode.removeChild(l);
    #     """)    
    #     time.sleep(1)
    #     driver.save_screenshot('strava.png')
    #     driver.quit()



    # def get_facebook(searchterm):
    #     facebook = pd.read_csv('data_facebook.csv')


    #     print('test')



    # get_facebook('fahrrad frankfurt')

import re
import pandas as pd
from bs4 import BeautifulSoup
import itertools

# regexes

# reactions = ['haha', 'care', 'like', 'angry', 'love', 'sad', 'wow']
# reactions_array = ['hahas', 'cares', 'likes', 'angrys', 'loves']




def get_reaction(reaction, reactions):
    array = []
    for reaction in reactions:
        r = int(re.sub("[^0-9]", "",reaction.get('aria-label')))
        print(r)
        array.append(r)

    return array 

def format_facebook():

    with open('facebook.html', 'r') as f:

        haha = r'Haha: [1-99]'
        care = r'Care: [1-99]'
        like = r'Like: [1-99]'
        angry = r'Angry: [1-99]'
        love = r'Love: [1-99]'
        sad = r'Sad: [1-99]'
        wow = r'Wow: [1-99]'



        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        hahas = soup.find_all('div', {'aria-label': re.compile(haha)})
        cares = soup.find_all('div', {'aria-label': re.compile(care)})
        likes = soup.find_all('div', {'aria-label': re.compile(like)})
        angrys = soup.find_all('div', {'aria-label': re.compile(angry)})
        loves = soup.find_all('div', {'aria-label': re.compile(love)})
        sads = soup.find_all('div', {'aria-label': re.compile(sad)})
        wows = soup.find_all('div', {'aria-label': re.compile(wow)})

        hahas = get_reaction(haha, hahas)
        cares = get_reaction(care, cares)
        likes = get_reaction(like, likes)
        angrys = get_reaction(angry, angrys)
        loves = get_reaction(love, loves)
        sads = get_reaction(sad, sads)
        wows = get_reaction(wow, wows)

        d = {'search term':'Stuttgart radweg','haha': sum(hahas), 'care': sum(cares), 'like': sum(likes), 'angry': sum(angrys),'love': sum(loves), 'sad': sum(sads),'wow': sum(wows)}

        df = pd.DataFrame(d, index=[0])
        # for reaction in zip(hahas, cares, likes, angrys, loves):
        #     r = reaction.get('aria-label')
            # print(r)
        df.to_csv('data_facebook.csv', mode='a', header=False)




# if __name__ == '__main__':
#     open_file()



print('--------------------------------')