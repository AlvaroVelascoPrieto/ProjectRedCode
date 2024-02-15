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
                                children=html.Img(src="../assets/Balcon_ACCU.png", className="pedalbox-logo"),
                                className="grid1-1"
                            ),
                            html.Div(
                                children="ACCUMULATOR STATE",
                                className="grid25-1",
                                style={'text-align':'center'}
                            ),
                            html.Div(
                                children=[html.H5('AMS State Machine',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='smAMS3',
                                        style={'font-size':'26px'}
                                        ),
                                ],className="grid1-22"
                            ),
                            html.Div(                                        
                                children=[html.H5('AMS Error',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='errorAMS3',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-33"
                            ),
                            html.Div(
                                children=[html.H5('AMS Mode',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='modeAMS3',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-44"
                            ), 
                            html.Div(
                                children=[html.H5('Timed Out Slave',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='timedOutSlave3',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-55"
                            ), 
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMinVoltage3',
                                        label={'label':"Cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='3.64',
                                        color="black"
                                    ),
                                className="grid2-22"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMaxVoltage3',
                                        label={'label':"Cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"

                                    ),
                                className="grid2-33"
                                ),
                            html.Div(
                                children=daq.Indicator(
                                            id='imd3',
                                            label={'label':"IMD", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="grid2-44"
                            ),
                                html.Div(
                                children=daq.Indicator(
                                            id='k13',
                                            label={'label':"K1", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="grid2-55"
                                ), 
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinVoltage3',
                                            label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxVoltage3',
                                            label={'label':"ID cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-33"
                                ),
                                html.Div(
                                    children=daq.Indicator(
                                                id='k23',
                                                label={'label':"K2+", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                                color="green",
                                                size=45,
                                                value=True
                                            ),
                                    className="grid3-55"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinVoltage3',
                                            label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxVoltage3',
                                            label={'label':"ID cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-33"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='cellMinTemp3',
                                            label={'label':"Cell Min Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid4-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='cellMaxTemp3',
                                            label={'label':"Cell Max Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid4-33"
                                ),
                                html.Div(
                                children=daq.Indicator(
                                            id='ams3',
                                            label={'label':"AMS", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="grid4-44"
                                ),
                                html.Div(
                                    children=daq.Indicator(
                                                id='k33',
                                                label={'label':"K3-", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                                color="green",
                                                size=45,
                                                value=True
                                            ),
                                    className="grid4-55"
                                ), 
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinTemp3',
                                            label={'label':"ID Cell Min Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxTemp3',
                                            label={'label':"ID Cell Max Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-33"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='totalVoltage3',
                                            label={'label':"Estimated Voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-44"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='current3',
                                            label={'label':"Output Current", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-55"
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
                                    children=html.Img(src="../assets/Motor.png", className="pedalbox-logo"),
                                    className="grid1-1"
                                ),
                                html.Div(
                                    children="INVERTERS & MOTORS",
                                    className="grid25-1",
                                    style={'text-align':'center'}
                                ),
                                html.Div(
                                children=[html.H5('AMS State Machine',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='smAMS4',
                                        style={'font-size':'26px'}
                                        ),
                                ],className="grid1-22"
                            ),
                            html.Div(                                        
                                children=[html.H5('AMS Error',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='errorAMS4',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-33"
                            ),
                            html.Div(
                                children=[html.H5('AMS Mode',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='modeAMS4',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-44"
                            ), 
                            html.Div(
                                children=[html.H5('Timed Out Slave',
                                        style={'font-weight': 'bold','font-size':'16px'}
                                        ),
                                        html.H5('Waiting for data',
                                        id='timedOutSlave4',
                                        style={'font-size':'26px'}
                                        ),
                                ],
                                className="grid1-55"
                            ), 
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMinVoltage4',
                                        label={'label':"Cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='3.64',
                                        color="black"
                                    ),
                                className="grid2-22"
                            ),
                            html.Div(
                                children=daq.LEDDisplay(
                                        id='cellMaxVoltage4',
                                        label={'label':"Cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                        labelPosition='top',
                                        value='0',
                                        color="black"

                                    ),
                                className="grid2-33"
                                ),
                            html.Div(
                                children=daq.Indicator(
                                            id='imd4',
                                            label={'label':"IMD", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="grid2-44"
                            ),
                                html.Div(
                                children=daq.Indicator(
                                            id='k14',
                                            label={'label':"K1", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="green",
                                            size=45,
                                            value=True
                                        ),
                                className="grid2-55"
                                ), 
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinVoltage4',
                                            label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxVoltage4',
                                            label={'label':"ID cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-33"
                                ),
                                html.Div(
                                    children=daq.Indicator(
                                                id='k24',
                                                label={'label':"K2+", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                                color="green",
                                                size=45,
                                                value=True
                                            ),
                                    className="grid3-55"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinVoltage4',
                                            label={'label':"ID cell min voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxVoltage4',
                                            label={'label':"ID cell max voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid3-33"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='cellMinTemp4',
                                            label={'label':"Cell Min Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid4-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='cellMaxTemp4',
                                            label={'label':"Cell Max Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid4-33"
                                ),
                                html.Div(
                                children=daq.Indicator(
                                            id='ams4',
                                            label={'label':"AMS", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                            color="red",
                                            size=45,
                                            value=True
                                        ),
                                className="grid4-44"
                                ),
                                html.Div(
                                    children=daq.Indicator(
                                                id='k34',
                                                label={'label':"K3-", 'style':{'font-weight': 'bold','font-size':'20px'}},
                                                color="green",
                                                size=45,
                                                value=True
                                            ),
                                    className="grid4-55"
                                ), 
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMinTemp4',
                                            label={'label':"ID Cell Min Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-22"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='idCellMaxTemp4',
                                            label={'label':"ID Cell Max Temp", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-33"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='totalVoltage4',
                                            label={'label':"Estimated Voltage", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-44"
                                ),
                                html.Div(
                                    children=daq.LEDDisplay(
                                            id='current4',
                                            label={'label':"Output Current", 'style':{'font-weight': 'bold','font-size':'16px'}},
                                            labelPosition='top',
                                            value='0',
                                            color="black"
                                        ),
                                    className="grid5-55"
                                ),
                            ],
                            className="cornerWrapperMulti"
                        ),
                    ],
                    className="box"
                ),
        ],
    className='container4'
    )

@callback(
    [Output('smAMS3', 'children'), Output('errorAMS3', 'children'), Output('modeAMS3', 'children'), Output('timedOutSlave3', 'children'), Output('cellMinVoltage3', 'value'), Output('cellMaxVoltage3', 'value'), Output('idCellMaxVoltage3', 'value'), Output('idCellMinVoltage3', 'value'), Output('cellMinTemp3', 'value'), Output('cellMaxTemp3', 'value'), Output('idCellMinTemp3', 'value'), Output('idCellMaxTemp3', 'value'), Output('totalVoltage3', 'value'), Output('current3', 'value'), Output('k13', 'color'), Output('k23', 'color'), Output('k33', 'color'), Output('cellMinVoltage3', 'color'), Output('cellMaxTemp3', 'color'), Output('imd3', 'color'), Output('ams3', 'color'), ],
    Input('int-component-el', 'n_intervals'),
)
def acutaliza(N):
    #begining = time.time()
    data = get_data()
    vel = random.randint(0,10)
    pedalera = interfaceUpdater.updatePedaleraMulti(get_0001())
    #end = time.time()
    #print(end-begining)

    ###MASTER###
    totalVoltage, minVoltage, idMinVoltage, voltageColor, maxVoltage, idMaxVoltage, minTemp, idMinTemp, maxTemp, idMaxTemp, colorTemp = interfaceUpdater.updateVoltages(data.get('0311'))
    k1, k2, k3, smAMS, errorAMS, imd, amsMode, timedOutSlvave, current, amsLed = interfaceUpdater.contactorFeedbackAndAMSState(data.get('0310'))
    return smAMS, errorAMS, amsMode, timedOutSlvave, minVoltage, maxVoltage, idMaxVoltage, idMinVoltage, minTemp, maxTemp, idMinTemp, idMaxTemp, totalVoltage, current, k1, k2, k3, voltageColor, colorTemp, imd, amsLed
