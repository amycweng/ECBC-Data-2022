import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
from IPython.display import Image

app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Social Network', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        html.Div(children=[
                html.Label(['Time Range'], style={'font-weight': 'bold', "text-align": "center"}),
                dcc.Dropdown(
                    id='dropdown1',
                    options = [
                    {'label':'1580-1599', 'value':'y1' },
                    {'label': '1600-1617', 'value':'y2'},
                    {'label': '1618-1624', 'value':'y3'},
                    {'label':'1625-1634', 'value':'y4'},
                    {'label':'1635-1641', 'value':'y5'}
                    ],
                    value = 'y1'),],
                    style = dict(width = '50%')
                ),
        
        html.Div(children=[
                html.Label(['Topic'], style={'font-weight': 'bold', "text-align": "center"}),
                dcc.Dropdown(
                    id='dropdown2',
                    options = [
                    {'label':'tobacco', 'value':'tobacco' },
                    {'label': 'drug', 'value':'drug'}
                    ],
                    value = 'tobacco'),],
                    style = dict(width = '50%')
                ),
                
        dcc.Graph(id = 'bar_plot')
    ])

@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              Input(component_id='dropdown1', component_property= 'value'),
              Input(component_id='dropdown2', component_property= 'value'))

def network(time, object):
    img = '/srv/data/optimalK.png'
    return img

if __name__ == '__main__': 
    app.run_server(port=2000)