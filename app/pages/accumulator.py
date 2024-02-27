import random
from JSONReader import get_0001, get_data
import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash import html, Dash, Input, ctx, Output, dcc, callback
from dash.exceptions import PreventUpdate
import interfaceUpdater
import data as rc

data = rc.data()
dash.register_page(__name__)
layout=html.Div(id='element-to-hide', style={'display':'none'}),\
        html.Div(
            children=[
            dcc.Interval(
                id='int-component-el',
                interval=225, # in milliseconds
                n_intervals=0
            ),
        ],
    ),\
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            dcc.Graph(
                                        id="voltajes",
                                        figure={'layout':{"autosize":False}},
                                        style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}, 'margin-top':'-35px'},
                                        config={"responsive":True,"displayModeBar": False, "edits":{"titleText":False,"legendText":False, "annotationPosition":False,"colorbarTitleText":False},"displayModeBar":True},

                                    ),
                        ],
                        className="cornerWrapperMulti"
                    )
                ],
                className="box"
            ),
        ],
    className='container4'
    )

@callback(
    [Output("voltajes", "figure")],
    Input('int-component-el', 'n_intervals'),
)
def acutaliza(N):
    #begining = time.time()
    data = get_data()
    vel = random.randint(0,10)
    voltajes = interfaceUpdater.updateVoltajes(data.get_value('0101'), data.get_value('0102'), data.get_value('0103'),data.get_value('0104'),data.get_value('0105'),data.get_value('0106'),data.get_value('0107'),data.get_value('0108'),data.get_value('0109'),data.get_value('010a'),data.get_value('010b'), data.get_value('1101'), data.get_value('1102'), data.get_value('1103'),data.get_value('1104'),data.get_value('1105'),data.get_value('1106'),data.get_value('1107'),data.get_value('1108'),data.get_value('1109'),data.get_value('110a'),data.get_value('110b'), )
    #end = time.time()
    #print(end-begining)

    ###MASTER###
    return voltajes