import socket
import time

import dash_daq as daq
import dash
from dash import html, callback, Output, Input, dcc
import interfaceUpdater
from JSONReader import get_data, get_0310, get_0001, get_currentFL, get_currentFR, get_currentRL, \
    get_currentRR

pilaId0310=[0,0,0,0,0,0,0,0,0,0]
dash.register_page(__name__)

layout = html.Div(id='element-to-hide', style={'display':'none'}),\
         html.Div(
            children=[
            dcc.Interval(
                id='int-component',
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
                                    children=html.Img(src="../assets/Accumulator.jpg", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Accumulator",
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
                                    className="box4"
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
                                    className="box8"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinVoltage',
                                            label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="box9"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            label={'label':"Cell max temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"

                                        ),
                                    className="box10"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            label={'label':"ID cell max temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
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
                                    children=html.Img(src="../assets/ecu.png", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Car Status",
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
                                            id='Speed',
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
                                    children="Driver Inputs",
                                    className="box2"
                                ),
                                html.Div(
                                    children=dcc.Graph(
                                        id="grafico-1",
                                        figure={'layout':{"autosize":False}},
                                        style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                        config={"responsive":True,"displayModeBar": False, "edits":{"titleText":False,"legendText":False, "annotationPosition":False,"colorbarTitleText":False},"displayModeBar":True},

                                    ),
                                    className="box3"
                                )
                            ],
                            className="cornerWrapper"
                        ),
                    ],
                    className="box"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=html.Img(src="../assets/Motor.png", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Drivetrain",
                                    className="box2"
                                ),
                                html.Div(
                                    children=[html.H6('Statusword FL', className='statuswordtit'),
                                              html.H5('A67F', id='sw1'),
                                              #html.Br(style={'display': 'block', 'margin-bottom': '20px'}),
                                              html.H6('Statusword FR', className='statuswordtit'),
                                              html.H5('A67F', id='sw2'),
                                              #html.Br(className='miniBr'),
                                              html.H6('Statusword RL', className='statuswordtit'),
                                              html.H5('A67F', id='sw3'),
                                              #html.Br(className='miniBr'),
                                              html.H6('Statusword RR', className='statuswordtit'),
                                              html.H5('A67F', id='sw4'),
                                              ],
                                    className="box4"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='SpeedFL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"Speed FL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 1000, 'labelInterval': 4},
                                    showCurrentValue=True,
                                    units="RPM",
                                    value=5000,
                                    min=0,
                                    max=20000,
                                    ),
                                    className="box8"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='SpeedFR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"Speed FR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 1000, 'labelInterval': 4},
                                    showCurrentValue=True,
                                    units="RPM",
                                    value=3000,
                                    min=0,
                                    max=20000,
                                    ),
                                    className="box9"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='SpeedRL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"Speed RL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 1000, 'labelInterval': 4},
                                    showCurrentValue=True,
                                    units="RPM",
                                    value=20000,
                                    min=0,
                                    max=20000,
                                    ),],
                                    className="box10"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='SpeedRR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"Speed RR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 1000, 'labelInterval': 4},
                                    showCurrentValue=True,
                                    units="RPM",
                                    value=20000,
                                    min=0,
                                    max=20000,
                                    ),],
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
                                    children=html.Img(src="../assets/Motor.png", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Drivetrain",
                                    className="box2"
                                ),
                                html.Div(
                                    children=[daq.Thermometer(
                                                    id='tempFL',
                                                    value=40,
                                                    height=110,
                                                    min=0,
                                                    max=80,
                                                    showCurrentValue=True,
                                                    style={
                                                        'margin-left': '-80px', 'margin-bottom' : '20px', 'margin-top' : '-40px'
                                                    }
                                                ),
                                                daq.Thermometer(
                                                    id='tempFR',
                                                    value=40,
                                                    height=110,
                                                    min=0,
                                                    max=80,
                                                    showCurrentValue=True,
                                                    style={
                                                        'margin-left' : '-80px', 'margin-top' : '-5 px'
                                                    }
                                                ),
                                                daq.Thermometer(
                                                    id='tempRL',
                                                    value=40,
                                                    height=110,
                                                    min=0,
                                                    max=80,
                                                    showCurrentValue=True,
                                                    style={
                                                        'margin-top': '-455px', 'margin-right' : '-110px'
                                                    }
                                                ),
                                                daq.Thermometer(
                                                    id='tempRR',
                                                    value=40,
                                                    height=110,
                                                    min=0,
                                                    max=80,
                                                    showCurrentValue=True,
                                                    style={
                                                        'margin-top': '10px', 'margin-right' : '-110px'
                                                    }
                                                ),
                                              ],
                                    className="box4"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='powerFL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"Power FL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    showCurrentValue=True,
                                    units="W",
                                    value=0,
                                    min=-524288,
                                    max=524272,
                                    ),
                                    className="box8"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='powerFR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"Power FR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    showCurrentValue=True,
                                    units="W",
                                    value=0,
                                    min=-524288,
                                    max=524272,
                                    ),
                                    className="box9"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='powerRL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"Power RL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    showCurrentValue=True,
                                    units="W",
                                    value=0,
                                    min=-524288,
                                    max=524272,
                                    ),],
                                    className="box10"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='powerRR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"Power RR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    showCurrentValue=True,
                                    units="W",
                                    value=0,
                                    min=-524288,
                                    max=524272,
                                    ),],
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
                                    children=html.Img(src="../assets/Motor.png", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Drivetrain",
                                    className="box2"
                                ),
                                html.Div(
                                    children=[html.H6('LatchedStatus FL', className='statuswordtit'),
                                              html.H5('A67F', id='LS FL'),
                                              #html.Br(style={'display': 'block', 'margin-bottom': '20px'}),
                                              html.H6('LatchedStatus FR', className='statuswordtit'),
                                              html.H5('A67F', id='LS FR'),
                                              #html.Br(className='miniBr'),
                                              html.H6('LatchedStatus RL', className='statuswordtit'),
                                              html.H5('A67F', id='LS RL'),
                                              #html.Br(className='miniBr'),
                                              html.H6('LatchedStatus RR', className='statuswordtit'),
                                              html.H5('A67F', id='LS RR'),
                                              ],
                                    className="box4"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='tqComFL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"TorqueCommand FL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 100, 'labelInterval': 1},
                                    showCurrentValue=True,
                                    value=1000,
                                    min=0,
                                    max=1000,
                                    ),
                                    className="box8"
                                ),
                                html.Div(
                                    children=daq.Gauge(
                                    id='tqComFR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                    size=160,
                                    label={'label':"TorqueCommand FR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 100, 'labelInterval': 1},
                                    showCurrentValue=True,
                                    value=1000,
                                    min=0,
                                    max=1000,
                                    ),
                                    className="box9"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='tqComRL',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"TorqueCommand RL", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 100, 'labelInterval': 1},
                                    showCurrentValue=True,
                                    value=1000,
                                    min=0,
                                    max=1000,
                                    ),],
                                    className="box10"
                                ),
                                html.Div(
                                    children=[html.Br(),daq.Gauge(
                                    id='tqComRR',
                                    style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'50'}},
                                    size=160,
                                    label={'label':"TorqueCommand RR", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                    labelPosition='bottom',
                                    color="#e30202",
                                    scale={'start': 0, 'interval': 100, 'labelInterval': 1},
                                    showCurrentValue=True,
                                    value=1000,
                                    min=0,
                                    max=1000,
                                    ),
                                    ],
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
                                    children=html.Img(src="../assets/Motor.png", className="pedalbox-logo"),
                                    className="box1"
                                ),
                                html.Div(
                                    children="Drivetrain",
                                    className="box2"
                                ),
                                html.Div(
                                    children=dcc.Graph(
                                        id="current-Graph",
                                        figure={'layout':{"autosize":False}},
                                        style={'width': '100%', 'height':'100%', 'margin':{'l':'0','r':'0','b':'0','t':'0'}},
                                        config={"responsive":True,"displayModeBar": False, "edits":{"titleText":False,"legendText":False, "annotationPosition":False,"colorbarTitleText":False},"displayModeBar":True},

                                    ),
                                    className="box3"
                                )



                            ],
                            className="cornerWrapper"
                        )
                    ],
                    className="box"
                )
            ],
            className="container2"
        ),




@callback(
    [Output("grafico-1", "figure"), Output('totalVoltage', 'value'), Output('cellMinVoltage', 'value'), Output('idCellMinVoltage', 'value'), Output('totalVoltage', 'color'), Output('cellMinVoltage', 'color'), Output('k1', 'color'), Output('k2', 'color'), Output('k3', 'color'), Output("safetyFront", "children"), Output("safetyLine", "children"), Output("carStatus", "children"), Output('sw1', 'children'), Output('sw2', 'children'), Output('sw3', 'children'), Output('sw4', 'children'), Output('SpeedFL','value'), Output('SpeedFR','value'), Output('SpeedRL','value'), Output('SpeedRR','value'), Output('LS FL', 'children'), Output('LS FR', 'children'), Output('LS RL', 'children'), Output('LS RR', 'children'), Output('IMD', 'color'), Output('AMS', 'color'), Output('Plausibility', 'color'), Output('tempFL','value'), Output('tempFR','value'), Output('tempRL','value'), Output('tempRR','value'), Output('powerFL','value'), Output('powerFR','value'), Output('powerRL','value'), Output('powerRR','value'), Output('tqComFL','value'), Output('tqComFR','value'), Output('tqComRL','value'), Output('tqComRR','value'), Output('Speed', 'value'), Output('smAMS', 'children'), Output('errorAMS', 'children')],
    Input('int-component', 'n_intervals'),
)
def acutaliza(N):
    #begining = time.time()
    data = dict(get_data())
    print(data)
    #figura2 = interfaceUpdater.updateFigure2(data.get('0310'))

    totalVoltage, minVoltage, idMinVoltage, voltageColor = interfaceUpdater.updateVoltages(data.get('0311'))
    k1, k2, k3, smAMS, errorAMS = interfaceUpdater.contactorFeedbackAndAMSState(data.get('0310'))

    figura1 = interfaceUpdater.updateFigure1(get_0001())

    safetyFront = interfaceUpdater.safetyFront(data.get('00a2'))
    safetyValue, imd, ams, plausibility, carState = interfaceUpdater.safety(data.get('00f1'))

    sw1, ls1, sw2, ls2, sw3, ls3, sw4, ls4 = interfaceUpdater.motorData(data.get('01cf'), data.get('02cf'), data.get('01ce'), data.get('02ce'))
    speedFL, speedFR, speedRL, speedRR = interfaceUpdater.motorRPM(data.get('024f'), data.get('034f'), data.get('024e'), data.get('034e'))
    tempFL, tempFR, tempRL, tempRR, powerFL, powerFR, powerRL, powerRR = interfaceUpdater.powerAndDCVoltage(data.get('028f'), data.get('038f'), data.get('028e'), data.get('038e'))
    tqComFL, tqComFR, tqComRL, tqComRR = interfaceUpdater.torqueCommands(data.get('020e'), data.get('040e'), data.get('020f'), data.get('040f'))
    speed, yawRateRef = interfaceUpdater.speedAndYawRateRef(data.get('00f2'))
    currentFigure = interfaceUpdater.currents(get_currentFL(), get_currentFR(), get_currentRL(), get_currentRR())
    #end = time.time()
    #print(end-begining)
    return figura1, totalVoltage, minVoltage, idMinVoltage, voltageColor, voltageColor, k1, k2, k3, safetyFront, safetyValue, carState, sw1, sw2, sw3, sw4, speedFL, speedFR, speedRL, speedRR, ls1, ls2, ls3, ls4, imd, ams, plausibility, tempFL, tempFR, tempRL, tempRR, powerFL, powerFR, powerRL, powerRR, tqComFL, tqComFR, tqComRL, tqComRR, speed, smAMS, errorAMS

