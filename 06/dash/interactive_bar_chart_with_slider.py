import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("vgsales.csv") #read in the data

app = dash.Dash(__name__) #create the dashboard

#make a layout with headers, a slider and a graph
app.layout = html.Div(children=[
  html.H1("Year"),
   dcc.RangeSlider(
        id="slider",
        min=1980,
        max=2020,
        # Set step one year
        step=1,
        marks={"1980": "1980", "1990":"1990", "2000":"2000", "2010": "2010", "2020": "2020"},
        value=[1995,2000]
    ),  
  html.H1("Genres"),
  dcc.Graph(id='genre-graph')
])

#Callback: it's complicated!
#The @app.callback ties the update function to the widgets & graphs
#The update function needs to be directly under the @app.callback. No blank lines!
#Here's how it works:
#1. The callback function fires the "update_figure" function whenever the Input changes.
#2. It gets the input from the widget with id="slider" (see above), from the "value" attribute.
#3. It then calls the functions "update_figure" with "value" as argument.
#4. The "update_figure" function updates the data and remakes the figure.
#5. The figure is then sent to Output: to the "genre-graph" graph, where it replaces the "figure" attribute.
@app.callback(
    Output("genre-graph", "figure"),
    Input("slider", "value"))
def update_figure(year_selected):
    df_subset = df[(df["Year"] >= year_selected[0]) & (df["Year"] <= year_selected[1])]  #subset the data based on year that slider is on
    df_genres = df_subset.groupby("Genre").size().reset_index(name="counts") #group the data, make table
    figure = px.bar(df_genres, x="counts", y="Genre") #make a new, updated figure
    return figure #return the figure to the layout

#run the app
if __name__ == '__main__':
    app.run_server(debug=True)
  
