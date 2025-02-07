import dash
from dash import Dash, dcc, html #dcc is for the dash core components, #html is for the html components
import pandas as pd

import plotly.express as px

# Load the data
#df = pd.read_csv('C:\Users\ADMIN\Desktop\avocado_app\avocado.csv')
df = pd.read_csv(r'C:\Users\ADMIN\Desktop\avocado_app\avocado.csv')
df = df.query("type == 'conventional' and region == 'Albany'")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df.sort_values("Date", inplace=True)

# Build the app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[html.H1("Avocado Prices Dashboard"),
    html.P("The dashboard shows the average prices of avocados" 
    " and quantity of avocados sold in US-Albany region"
    " between 2015 and 2018."),
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": df["Date"],
                    "y": df["AveragePrice"],
                    "type": "lines",
                },
            ],
            "layout": {
                "title": "Average Price of Avocados"
            }
        }
    ),
    dcc.Graph(
        figure={
            "data": [
                {
                    "x": df["Date"],
                    "y": df["Total Volume"],
                    "type": "lines",
                },
            ],
            "layout": {
                "title": "Quantity of Avocados Sold"
            }
        }
    ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True) #debug=True is for the changes to be reflected in the browser
