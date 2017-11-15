import dash
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

# ----------------------------------------------------------------------------------

df_people = pd.read_csv('./data/people.csv').replace('', np.NaN).head(10)

'''Return an HTML generated table. max_rows is initialized to 10 rows,
    dataframe is in a pandas dataframe format'''
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

# ----------------------------------------------------------------------------------

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        children='The Holy Grail of VC',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    generate_table(df_people)
])

# ----------------------------------------------------------------------------------

#css
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# ----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)