import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
df = pd.read_csv("vgsales.csv")
df_genres = df.groupby("Genre").size().reset_index(name='counts')
df_platforms = df.groupby("Platform").size().reset_index(name='counts')
df_sales = df.groupby("Year")["Global_Sales"].sum().reset_index()

app = dash.Dash()
fig_genre = px.bar(df_genres, x="counts", y="Genre")
fig_platform = px.bar(df_platforms, x="counts", y="Platform")
fig_sales = px.line(df_sales, x="Year", y="Global_Sales")

app.layout = html.Div(children=[
  html.H1("Genres"),
  dcc.Graph(
    id='genre-graph',
    figure = fig_genre
  ),
  html.H1("Platforms"),
  dcc.Graph(
    id='platform-graph',
    figure = fig_platform
  ),
  html.H1("Sales"),
  dcc.Graph(
    id='sales-graph',
    figure = fig_sales
  ),
])
if __name__ == '__main__':
    app.run_server(debug=False)
    
    
    