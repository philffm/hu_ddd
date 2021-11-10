# from aem import app
from tokenize import String
import justpy as jp
import time
import logging
import asyncio
from threading import Timer
import os

from matplotlib import style
# Import data handling module (created for isolated testing)
import handle_data
import pandas as pd

import matplotlib.pyplot as plt

# import plotly.figure_factory as ff
import numpy as np


# Deprecated
# import tweets

wp = jp.WebPage(delete_flag=False)


img_path = '/static/assets/img/'

logger = logging.getLogger(__name__)

def foo():
    logger.info('Hi, foo')

input_classes = "m-4 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = 'm-2 p-2 h-32 text-xl border-2'
grid_style = 'height: 100px; max-width: 800px; '
style_main = 'max-width:450px; background: RGBA(162,162,162,0.1); padding: 40px; border-radius: 8px;margin-left: auto; margin-right: auto;margin-top: 50px;'
style_wide = style_main.replace('max-width:450px', 'max-width:800px').replace('margin-top: 50px;', '')
style_reactions = 'display: flex;flex-wrap: wrap;'
style_reaction = 'margin:4px;'
style_head = ''
style_strava_box = ''

in1 = 0
btn_start = None
last_time = None
cyclingtweets = None
current_city = None
darkmode = False


# async def get_tweets(self, msg, current_city):
#     start_bar(self, msg)
#     global cyclingtweets
#     cyclingtweets = tweets.get_tweets(str('fahrrad'+ current_city))

# async def get_citydata(self, msg):
#     data = handle_data.get_citydata(current_city)
#     return data


# async def start_bar(self, msg):
#     wp = msg.page
#     await wp.ajax_bar.run_method('start()', msg.websocket)

# async def stop_bar(self, msg):
#     wp = msg.page
#     await wp.ajax_bar.run_method('stop()', msg.websocket)


async def dummy(self, msg):
    return 1


async def my_input(self, msg):
    setattr(btn_start, 'loading' , True)

    task = asyncio.create_task(delayed_input(self, msg))
    await task

async def delayed_input(self, msg):
    global current_city
    # await asyncio.sleep(1.5)
    setattr(btn_start, 'disable', False)
    setattr(btn_start, 'color', 'cyan')
    
    setattr(btn_start, 'loading', False)
    current_city = self.value
    self.div.text = '🤔 ' + current_city + '... seems like a lovely city for cycling. Is it?'

# async def get_data(self, msg):
#     df = handle_data.get_citydata(current_city)
#     # df2 = pd.DataFrame(df)
    
#     # setattr(div_content, 'text', df)


async def update_data(self, msg):
    wp = msg.page

    # import data
    data_city = handle_data.output_data(current_city, 'data.csv')
    data_facebook = handle_data.output_data(current_city, 'data_facebook.csv')
    cityname = data_city['city'][:1].item()
    img_strava = img_path +'strava_'+cityname+'.png'
    
    setattr(wp.app, 'style', style_wide)
    setattr(wp.head, 'style','')
    setattr(wp.head, 'style',style_head)
    setattr(wp.head_img, 'style', 'display: none')
    # setattr(wp.head_h1, 'style','')
    setattr(wp.head_h2, 'text','Join them, not the haters.')
    setattr(wp.head_h1, 'text','People ❤️ cycling in '+ current_city)
    
     
    strava_score = handle_data.calc_strava(current_city)
    wp.div_strava = jp.Div(a = wp.head, classes ='strava box', style = 'background: url("'+img_strava+'") no-repeat;'  )
    wp.head_heatmap_score = jp.Div(classes = 'heatmap score', a = wp.div_strava, text = 'Score: '+ str(strava_score)+ '%')
    


    # Output according color for the displayed strava score
    def calc_color(score):
        blue = 0
        if score > 50:
            red = 255
            green = score * 2.5
        elif score > 80:    
            green = 255
            red = score * -2.5

        if green > 255:
            green = 255
        elif red > 255:
            red = 255

        return red, green, blue

    setattr(wp.head_heatmap_score, 'style', 'background:'+'rgb'+ str(calc_color(75))) 

    wp.h2_reactions = jp.H2(classes = 'h2', a = wp.app, text = 'Social media reactions in '+ current_city)
    wp.div_reactions = jp.Div(text='', a=wp.app, classes='reactions'+ current_city, style = style_reactions)


    if wp.text_stravanote == None:
        # wp.img_strava = jp.Img(a = wp.div_strava, src =img_strava, target = '_blank',  )
        wp.text_stravanote = jp.A(a = wp.div_strava, text = 'Source: https://www.strava.com/heatmap', href ='https://www.strava.com/heatmap', target = '_blank', style = 'text-align: right;margin: 10px;color: white; ' )
       
        

    reactions = {'like': 2, 'haha': 23, 'angry': 3, 'love': 4, 'sad': 4, 'wow': 4, 'care': 2}
    
    # for reaction in reactions:
    #     reaction_size = sum(data_facebook[reaction]) / 
    #     return reaction_size

    # sum(data_facebook[reaction])

    for reaction in reactions.keys():
        reactions[reaction] = sum(data_facebook[reaction])
    for reaction in reactions.keys():
        # get reaction size in percent
        try:
            reaction_pct = sum(data_facebook[reaction]) / sum(reactions.values())
        # avoid crash when there is 0 reactions of that type
        except ZeroDivisionError:
            reaction_pct = 0

        # define image size based on reaction percentage
        reaction_size = reaction_pct * 350
        # prevent super huge symbols in the graph: Of course that's basically falsifying data, but also there is user experience 
        if reaction_size > 110:
            reaction_size = 110
        # reaction_size = sum(data_facebook[reaction])
        # string.join('test', 'test')
        wp.div_reaction = jp.Div(classes = reaction + ' reaction',a = wp.div_reactions, style = style_reaction)
        reaction_symbol = jp.Img(classes = reaction +' symbol', src=img_path + reaction + '.svg', a = wp.div_reaction, style ='width:'+ str(reaction_size)+'px')
        reaction_label_text = reaction.capitalize(), ':', str(round(reaction_pct * 100)), '%'
        reaction_label = jp.Div(text = ''.join(reaction_label_text),  classes = reaction+' label',a = wp.div_reaction)


    
    # Details
    wp.h2_citydata = jp.H2(classes = 'h2', a = wp.app, text = 'Details: '+ current_city)
    wp.grid_citydata = jp.AgGrid(a=wp.app, style=grid_style)
    wp.grid_socialdata = jp.AgGrid(a=wp.app, style=grid_style)
    wp.grid_socialdata.load_pandas_frame(data_facebook)
    wp.grid_citydata.load_pandas_frame(data_city)


    setattr(wp.grid_citydata, 'max-height', '100px')




async def counter():
    while True:
        jp.run_task(wp.update())
        await asyncio.sleep(1)

async def main_init():
    jp.run_task(counter())


async def toggle_dm(self, msg):
    wp = msg.page
    print(wp.dark)
    if wp.dark == True:
        wp.dark = False
        self.label = "Dark mode"
    else:
        wp.dark = True
        self.label = "Light mode"
    await(wp.set_dark_mode(wp.dark))

async def main(request):

    global btn_start , div_content, grid_citydata, grid_socialdata, bubbles_socialdata, chart_socialdata
    
    # wp = jp.WebPage()


    wp = jp.QuasarPage(data={'text': ''}, dark = True)
    wp.dark = True
    wp.title = 'CycleAware'
    wp.css = """
        h1 {
            font-size: 2rem;
            line-height: 2rem;
        }
        h2 {
            font-size: 1.5rem;
            line-height: 1.5rem;
        }


        .label {
        background: #fff;
        }
        .label{
            padding: 7px;background: #FFFFFF;box-shadow: 0px 2px 0px rgba(0, 0, 0, 0.25);border-radius: 7px;color: black;margin:12px;
        }
        .angry.label {
        background: #eb660b;
        }
        .haha.label {
        background: rgb(253, 225, 105) ;
        }
        .love.label {
        background: rgb(251, 92, 119) ;
        }
        .reaction{
            margin: 4px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-evenly;
        }

        .header{
            display: flex;
            # flex-direction: unset;
            # border-radius: 10px;
            # color: white;
            justify-content: space-between;
        }
        .strava.box {
            margin: -61px -55px 0px 0px;
            display: flex;
            flex-direction: column-reverse;
            align-self: initial;
            width: 250px;
            border-radius: 10px;
        }
        .heatmap.score{
            color: black;
            background: white;
            display: flex;
            justify-content: unsafe;
            width: auto;
            margin: -14px auto;
            padding: 7px;
            border-radius: 7px;
            overflow: hidden;
        }
        
    """;
    
    wp.body = jp.Div(classes='q-pa-md', a=wp, style = '')
    div_darkcorner = jp.Div(a = wp.body, classes = 'darkcorner', style = 'display: flex; flex-direction: row-reverse;')
    btn_darkmode = jp.QBtn(a = div_darkcorner, label = "light mode", click=toggle_dm, icon="brightness_2" )
    wp.app = jp.Div(classes='app', a=wp.body, style = style_main)
    # html_head = 

    image = 'static/assets/img/cycling.png'
    wp.text_stravanote = None
    wp.head = jp.Div(classes = 'header', a = wp.app,  style = ' ')
    wp.div_headline = jp.Div(classes = 'headlines', a = wp.head,  style = 'display:flex; flex-direction:column; ')
    wp.head_img = jp.Img(a = wp.div_headline, src = img_path + 'cycling.png', style = 'width: 580px;margin: -150px 0px -40px -100px;')
    wp.head_h1 = jp.H1(classes = 'h1', a = wp.div_headline, text = 'Cycling in your city...' )
    wp.head_h2 = jp.H2(classes = 'h2', a = wp.div_headline, text = '... what to expect, what to improve?')
    
    # jp.Img(src = image,  a=head, width ='200px')

    # h1 = jp.Div(classes='h1', text='Test',  a=div2, style = 'font-size: 18px;')
    icon2 = jp.QIcon(name='place', color='cyan')

    div_inputcity = jp.Div(classes='q-gutter-md inputcity', style='display: flex; flex-direction: column;', a=wp.app)
    
    in1 = jp.QInput(label='Input your city', a=div_inputcity, model=[wp, 'text'],color='cyan', after_slot=icon2)
    in1.div = jp.Div(text='', classes=p_classes, a=div_inputcity)
    # in1.on('input', input_timer)
    in1.on('input', my_input)
    btn_start = jp.QBtn(color='grey', label="Let's find out!", a=div_inputcity, click=update_data, style='margin-right: 20px', disable = True, icon="directions_bike")
    setattr(btn_start, 'disable', True)

    # Place all the SVGs 
   



    return wp





if __name__ == '__main__':
    jp.justpy(main, startup = main_init, PLOTLY=True)
    # jp.justpy(women_majors)
    print('test')



