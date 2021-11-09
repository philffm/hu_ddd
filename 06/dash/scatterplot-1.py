from re import X
import dash
# import dash_core_components as dcc
from dash import dcc
import plotly.express as px
import pandas as pd


#load the data file
df = pd.read_csv("exam.csv")
df2 = pd.read_csv("vgsales.csv")

#creates the dashboard
app = dash.Dash()

#creates the figure
# fig1 = px.scatter(df, x="no_revisions", y="exam_score", size="Anxiety", symbol="Gender")
# fig1.show()
df2 = df2.sort_values(by="Year")
df_year = df2.groupby("Year").sum("Global_Sales")

fig2 = px.line(df_year, x = "counts", y = "Global_Sales",title='Global sales year over year')
fig2.show()



# add the figure to the dashboard
app.layout = dcc.Graph(id='genre-graph', figure=fig2)

if __name__ == '__main__':
  app.run_server(debug=False)


