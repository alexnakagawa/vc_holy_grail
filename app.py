import dash
import json
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output, State

# from controls import COUNTIES, WELL_STATUSES, WELL_TYPES, WELL_COLORS

import plotly.graph_objs as go

from flask import Flask

# ----------------------------------------------------------------------------------

df_people = pd.read_csv('./data/people.csv').replace('', np.NaN).head(10)
test_csv = pd.read_csv('./data/test_csv.csv')

'''Return an HTML generated table. max_rows is initialized to 10 rows,
    dataframe is in a pandas dataframe format'''
# def generate_table(dataframe , max_rows=10):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )

# ----------------------------------------------------------------------------------
# Layout

app = dash.Dash()

# CSS
colors = {
    'background': '#FAFAFA',
    'h1': '#080808',
    'text': '#151515'
}

# HTML + Components
app.layout = html.Div(children=[
    html.H1(
        children='The Holy Grail of VC',
        style={
            'textAlign': 'center',
            'color': colors['h1']
        }
    ),

    html.Div(children='Welcome to the Holy Grail. See the top trends of potential startup founders.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    dt.DataTable(
        rows=test_csv.to_dict('records'),
        columns=test_csv.columns,
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable-test'
        ),

    html.Div(id='selected-indexes'),
    dcc.Graph(
        figure= go.Figure(
            data=[
                    go.Bar(
                        x=['Trust', 'Fear of Failure', 'Persistence', \
                        'Convince Others', 'Rely on Others', 'Competition',\
                        'Strong Network', 'Work Life', 'Nine-Five Job'],
                        y=[5,5,5,5,5,5,5,5,5],
                        name='Elon Musk',
                        marker=go.Marker(color='rgb(250,0,5)')
                        ),

                    go.Bar(
                        x=['Trust', 'Fear of Failure', 'Persistence', \
                        'Convince Others', 'Rely on Others', 'Competition',\
                        'Strong Network', 'Work Life', 'Nine-Five Job'],
                        y=[5,2,2,4,5,5,4,4,3],
                        name='Gordan Moore',
                        marker=go.Marker(color='rgb(18,123,202)')
                        ),

                    go.Bar(
                        x=['Trust', 'Fear of Failure', 'Persistence', \
                        'Convince Others', 'Rely on Others', 'Competition',\
                        'Strong Network', 'Work Life', 'Nine-Five Job'],
                        y=[5,3,4,2,2,3,4,5,5],
                        name='Lorenzo Ong',
                        marker=go.Marker(color='rgb(0,255,10)')
                        ),

                    go.Bar(
                        x=['Trust', 'Fear of Failure', 'Persistence', \
                        'Convince Others', 'Rely on Others', 'Competition',\
                        'Strong Network', 'Work Life', 'Nine-Five Job'],
                        y=[1,1,2,1,3,4,2,2,5],
                        name='James Drugeot',
                        marker=go.Marker(color='rgb(155,105,84)')
                        ),
            ],
            layout=go.Layout(
                title='Personality Traits Based on Survey',
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='graph-test'
    )
],
style={'background':colors['background']})

# ----------------------------------------------------------------------------------
# Additional CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# ----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)