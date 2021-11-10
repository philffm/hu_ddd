# Connect all the APIs we are using here
import walkscore
import weather
import strava
import pandas as pd
import asyncio
from threading import Timer


df = None
# current_city = input('City please')


def get_citydata(current_city):

    data_weather = weather.get_weather(current_city)
    lat = data_weather['coord']['lat']
    lon = data_weather['coord']['lon']
    name = data_weather['name']
    data_pollution = weather.get_pollution(lat, lon)
    data_pollution = data_pollution['list']
    # data_walkscore = walkscore.get_walkscore(name, lat, lon)
    data_walkscore = walkscore.get_walkscore(current_city, lat, lon)
    data_pollution = give_pollution(data_pollution)
    data_strava = strava.get_heatmap(lat, lon, name)

    write_citydata(data_weather, data_walkscore, data_pollution, data_strava)
    return data_weather, data_pollution, data_walkscore, data_strava

def give_pollution(data_pollution):
    df_pollution = pd.DataFrame(data=data_pollution[1]['components'], index=[0])    
    for entry in data_pollution:
        df_pollution = df_pollution.append(entry['components'], ignore_index=True)
    return df_pollution



# df = get_citydata('Frankfurt')
# df2 = pd.DataFrame(df)

def write_citydata(data_weather, data_walkscore, data_pollution, data_strava):

    d = {'city':data_weather['name'], 'walkscore': data_walkscore['walkscore'], 'pm2_5': data_pollution['pm2_5'].mean(), 'co2': data_pollution['co'].mean(), 'no2': data_pollution['no2'].mean(), 'strava': data_strava}
    df = pd.DataFrame(d, index=[0])
    df.to_csv('data.csv', mode='a', header=False)

    

# def save_csv():


def output_data(city, file):
    data = pd.read_csv(file)
    # data_facebook = pd.read_csv('data_facebook.csv')

    df = pd.DataFrame(data)
    df2 = df[df['city'].str.contains(city, case=False)]
    return df2

def calc_strava(city):
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data)
    # calculate percentage of selected city  in comparison to other cities
    score =  df[df['city'].str.contains(city, case=False)]['strava'].max() / df['strava'].max()  * 100
    score_p = "{:.0%}".format(score)

    return round(score)


print('test')



# import justpy as jp
# import plotly.figure_factory as ff
# import numpy as np


# def create_chart(numpoints):
#     hist_data = data_pollution
#     group_labels = ['Group 1', 'Group 2', 'Group 3']
#     # Create display with custom bin_size
#     fig = ff.create_distplot(hist_data, group_labels)
#     fig.update_layout(width=500, height=600)
#     return fig


# def generate_data(self, msg):
#     wp = msg.page
#     wp.c.chart = create_chart(wp.numpoints)


# def plotly_test(request):
#     wp = jp.WebPage()
#     wp.numpoints = 500
#     jp.Button(text='Generate New Data', click=generate_data, a=wp, classes=jp.Styles.button_simple + ' m-2 p-2')
#     wp.c = jp.PlotlyChart(chart=create_chart(wp.numpoints), a=wp, classes='border m-2 p-6', style='width: 600px')
#     return wp


# jp.justpy(plotly_test, PLOTLY=True)