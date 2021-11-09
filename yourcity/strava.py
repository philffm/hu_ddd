# from seleniumwire import webdriver  # Import from seleniumwire

# Own internal Strava API, fetches cycling heatmap from strava using selenium / image processing

import undetected_chromedriver.v2 as uc
import time 
import os
from PIL import Image
img_path = '/assets/img/'
basedir = os.getcwd()


fz = None

def get_heatmap(lon, lat, name):
    options = uc.ChromeOptions()
    brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options.binary_location = brave_path
    # options.add_argument("--incognito")
    # options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")

    elements_to_remove = ['sidebar']
    driver = uc.Chrome(options=options)
    url  = "https://www.strava.com/heatmap#8.44/%s/%s/hot/ride" % (lat, lon)
    driver.get(url)   # known url using cloudflare's "under attack mode"
    driver.execute_script("""
    var l = document.getElementById('global-header');
    l.parentNode.removeChild(l);
    """)    
    driver.find_element_by_css_selector('#learn-more-modal > div > div > div.modal-header > button').click()
    driver.find_element_by_css_selector('#sidebar > div.sidebar-header > div').click()
    driver.find_element_by_css_selector('#stravaCookieBanner > div > div > button').click()
    # Some delay to make sure the screenshot is complete (I know, there must be a better way)
    time.sleep(2)
    os.chdir(os.getcwd()+img_path)
    driver.save_screenshot('strava.png')   
    filename = 'strava_'+name+'.png'
    crop_image(filename) 
    driver.quit()
    filesize = get_filesize(name)
    os.chdir(basedir)
    return filesize
    

def crop_image(filename):
    im = Image.open(r"strava.png")

    # define size
    width, height = im.size    
    left = width / 3
    top = height / 3
    right = 2 * width / 3
    bottom = 2 * height / 3
    
    
    # Cropped image
    im1 = im.crop((left, top, right, bottom))
    
    # Saves the image to new file
    im1.save(filename)


def get_filesize(name):
    filesize = os.path.getsize('strava_'+name+'.png')
    return filesize


print("test")