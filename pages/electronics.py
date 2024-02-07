import random
from JSONReader import get_0001, get_data
import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash import html, Dash, Input, ctx, Output, dcc, callback
from dash.exceptions import PreventUpdate
import interfaceUpdater

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
                            html.Div(
                                children=html.Img(src="../assets/ecu.png", className="pedalbox-logo"),
                                className="box1"
                            ),
                            html.Div(
                                children="ECU",
                                className="box2"
                            ),
                            html.Div(
                                children=[html.H5('AMS State Machine',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='smAMS',
                                        style={'font-size':'26px'}
                                        ),
                                        html.Br(),
                                        html.H5('AMS Error',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='errorAMS',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="box4"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='IMD',
                                            label={'label':"IMD", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="box5"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='AMS',
                                            label={'label':"AMS", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="box6"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='Plausibility',
                                            label={'label':"Plausibility", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="yellow",
                                            size=45,
                                            value=True
                                        ),
                                className="box7"
                            ),
                            html.Div(
                                children=[html.H5('Safety',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='safetyLine',
                                        style={'font-size':'26px'}
                                        ),
                                    ],
                                className="box8"
                            ),
                            html.Div(
                                children=[html.H5('Safety front',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='safetyFront',
                                        style={'font-size':'26px'}
                                    ),
                                ],
                                className="box9"
                            ),
                            html.Div(
                                children=[html.H5('Car status',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='carStatus',
                                        style={'font-size':'26px'}
                                    ),
                                ],
                                className="box10"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='vel',
                                        label={'label':"Speed", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"
                                    ),
                                className="box11"
                            ),
                        ],
                        className="cornerWrapper"
                    )
                ],
                className="box"
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=html.Img(src="../assets/Balcon_ACCU.png", className="pedalbox-logo"),
                                className="box1"
                            ),
                            html.Div(
                                children="AMS",
                                className="box2"
                            ),
                            html.Div(
                                children=daq.Tank(
                                            id='totalVoltage',
                                            min=480,
                                            max=600,
                                            value=546.8,
                                            showCurrentValue=True,
                                            units='V',
                                            color='green',
                                            height=285,
                                            style={'margin-left': '50px'},
                                        ),
                                className="box4-1"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='k1',
                                            label={'label':"K1", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="box5"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='k2',
                                            label={'label':"K2+", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="box6"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='k3',
                                            label={'label':"K3-", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="box7"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMinVoltage',
                                        label={'label':"Cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='3.64',
                                        color="black"

                                    ),
                                className="box8-1"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='idCellMinVoltage',
                                        label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"
                                    ),
                                className="box9-1"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMaxVoltage',
                                        label={'label':"Cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"

                                    ),
                                className="box10-1"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='idCellMaxVoltage',
                                        label={'label':"ID cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"
                                    ),
                                className="box11-1"
                            ),
                        ],
                        className="cornerWrapperMulti"
                    )
                ],
                className="box"
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=html.Img(src="../assets/dash.jpeg", className="pedalbox-logo"),
                                className="box1"
                            ),
                            html.Div(
                                children="Dash",
                                className="box2"
                            ),
                            html.Div(
                                children=[html.H5('State Machine',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='smAMS',
                                        style={'font-size':'26px'}
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Previous State',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='errorAMS',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="box4"
                            ),
                            html.Div(
                                children=daq.Indicator(
                                            id='Frontok',
                                            label={'label':"FRONT OK", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="box5"
                            ),
                            
                            html.Div(
                                children=[html.H5('Safety',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='safetyLine',
                                        style={'font-size':'26px'}
                                        ),
                                    ],
                                className="box8"
                            ),
                            html.Div(
                                children=[html.H5('Safety front',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='safetyFront',
                                        style={'font-size':'26px'}
                                    ),
                                ],
                                className="box9"
                            ),
                            html.Div(
                                children=[html.H5('Button',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5(
                                        id='carStatus',
                                        style={'font-size':'26px'}
                                    ),
                                ],
                                className="box10"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='vel',
                                        label={'label':"Speed", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"
                                    ),
                                className="box11"
                            ),
                        ],
                        className="cornerWrapper"
                    )
                ],
                className="box"
            ),
            html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=html.Img(src="../assets/PedalBox.jpg", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Pedalera",
                                    className="box2"
                                ),
                                html.Div(
                                    children=[dcc.Graph(
                                        id="pedalera",
                                        figure={'layout':{"autosize":False}},
                                        style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                        config={"responsive":True,"displayModeBar": False, "edits":{"titleText":False,"legendText":False, "annotationPosition":False,"colorbarTitleText":False},"displayModeBar":True},

                                    ),
                                    dcc.Slider( -28, 28, 0.5, value=0,  included=False, id="volante",
                                                    tooltip={"placement": "bottom", "always_visible": True},
                                                    marks={
                                                            0: {'label': '0°', 'style': {'color': '#f50', 'size':'18px'}},

                                                        },
                                               ),
                                    ],
                                    className="box3"
                                )
                            ],
                            className="cornerWrapper"
                        ),
                    ],
                    className="box"
                ),
        ],
    className='container3'
    )

@callback(
    [Output("vel", "value"),Output("pedalera", "figure")],
    Input('int-component-el', 'n_intervals'),
)
def acutaliza(N):
    #begining = time.time()
    data = get_data()
    vel = random.randint(0,10)
    pedalera = interfaceUpdater.updatePedaleraMulti(get_0001())
    #end = time.time()
    #print(end-begining)
    return vel, pedalera
