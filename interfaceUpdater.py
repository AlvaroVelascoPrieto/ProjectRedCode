import dash.html as html
import dash_daq as daq
import plotly.graph_objects as go

statuses = [
    "Event buffer has a new event entry since last upload",
    "Event buffer is full and has missed at least one event",
    "Power module over current detected by hardware",
    "Power module current offset calibration failed",
    "Power module temperature sensor defective",
    "Power module temperature has reached warning level",
    "Power module temperature has reached error level",
    "Power module i*t error",
    "Power module over current detected by software",
    "Power module pattern data inconsistency",
    "Dc link over voltage detected by hardware",
    "Dc link over voltage detected by software",
    "Dc link undervoltage detectedy by software",
    "Fault of the other inverter on the same device",
    "Motor temperature sensor defective",
    "Motor temperature has reached warning level",
    "Motor temperature has reached error level",
    "Motor stator frequency to high",
    "Board supply voltage error",
    "Receive PDO timeout",
    "NMT not in state operational",
    "Task calculation time overrun",
    "Net synchronisation error",
    "Position device signal to low",
    "Position device signal to high",
    "Resolver calibration failed",
    "System error, analog input or motor feedback DMA error",
    "Interlock open due to open cover sheet",
    "Gate driver disabled by APPC",
    "Motor stall error",
    "Ambient temperature has reached warning level",
    "Ambient temperature has reached error level"
]


STATES = {'00' : 'Safe 1',
    '01' : 'Safe 2 Front',
    '02' : 'Safe 2 BOTS',
    '03' : 'Safe 2 FL',
    '04' : 'Safe 2 FR',
    '05' : 'Safe 2 Cockpit',
    '06' : 'Safe 2 Inertia',
    '07' : 'Safe 3 Mainhoop',
    '08' : 'Safe 4 Accu',
    '09' : 'Safe 5 RL',
    '0a' : 'Safe 6 RR',
    '0b' : 'Safe 7 BSPD',
    '0c' : 'Safe 8 Interlocks',
    '0d' : 'Safe End Vload',
    '0e' : 'Safe OK'
}

CARSTATES = {
    '00' : 'Init',
    '01' : 'Standby',
    '02' : 'Precharge',
    '03' : 'Energized',
    '04' : 'Running',
    '05' : 'Error'
}

AMSSTATES = {
    '01' : 'Charge waiting',
    '02' : 'Charge precharge',
    '03' : 'Charge charging',
    '04' : 'Car waiting',
    '05' : 'Car precharge',
    '06' : 'Car RTD',
    '07' : 'Error',
    '08' : 'Critical Error'
}

AMSERRORS = {
    '0' : 'OK',
    '1' : 'VLoad',
    '2' : 'IMD',
    '4' : 'ECU Timeout',
    '8' : 'Current',
    '16' : 'Error contactores',
    '32' : 'Voltaje',
    '64' : 'Temperatura',
    '128' : 'Slaves Timeout'
}

def updateFigure1(data):
    datosAcc = [int(i[10:12],base=16) for i in data]
    datosBrk = [int(i[6:8],base=16) for i in data]
    datosX = [i for i in range(len(datosAcc))]
    figure_1 = go.Figure(

        data = [go.Scatter(
            x = datosX,
            y = datosAcc,
            mode = 'lines',
            name='Acc',
            marker = dict(color = 'green')
        ),
            go.Scatter(
                x=datosX,
                y=datosBrk,
                mode='lines',
                name='Brk',
                marker=dict(color='red')
            ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (0, 250)}
    return figure_1

def updatePedaleraMulti(data):
    datosAcc1 = [int(i[10:12],base=16) for i in data]
    datosAcc2 = [int(i[12:14],base=16) for i in data]
    datosAcc3 = [int(i[14:16],base=16) for i in data]
    datosBrk = [int(i[6:8],base=16) for i in data]
    datosX = [i for i in range(len(datosAcc1))]
    figure_1 = go.Figure(

        data = [go.Scatter(
            x = datosX,
            y = datosAcc1,
            mode = 'lines',
            name='Acc1',
            marker = dict(color = 'green')
        ),
            go.Scatter(
                x=datosX,
                y=datosBrk,
                mode='lines',
                name='Brk',
                marker=dict(color='red')
            ),
            go.Scatter(
                x=datosX,
                y=datosAcc2,
                mode='lines',
                name='Acc2',
                marker=dict(color='blue')
            ),
            go.Scatter(
                x=datosX,
                y=datosAcc3,
                mode='lines',
                name='Acc3',
                marker=dict(color='purple')
            ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (0, 250)}
    return figure_1




def updateFigure2(data):
    datosY = []
    datosY.append(int(data[0:2], base=16))
    datosY.append(int(data[3:5], base=16))
    datosX = [i for i in range(len(datosY))]

    figure_2 = {
        "data": [
            {
                "x": datosX,
                "y": datosY,
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "xaxis": {"fixedrange": True},
            "yaxis": {"range":(0,200)},
            "colorway": ["#e30202", "#302f2f", "#000000", "#15ff00", "#0062ff", "#ff00f7"],
        },
    }
    return figure_2


def updateVoltages(data):
    minVoltage = round(float(int(data[0:2], base=16) / 51.0),3)
    totalVoltage = round(minVoltage*144,4)
    idMinVoltage = int(data[2:4][0:2], base=16)
    maxVoltage = round(float(int(data[4:6], base=16) / 51.0), 3)
    idMaxVoltage = int(data[6:8][0:2], base=16)
    if totalVoltage>532.8:
        colorVoltage='green'
    elif totalVoltage>512:
        colorVoltage='orange'
    else:
        colorVoltage='red'
    return totalVoltage, minVoltage, idMinVoltage, colorVoltage, maxVoltage, idMaxVoltage


def contactorFeedbackAndAMSState(data):
    k1 = 'green' if bin(int(data[2:4][0:2], base=16))[-1] == '1' else 'grey'
    k2 = 'green' if bin(int(data[2:4][0:2], base=16))[-2] == '1' else 'grey'
    k3 = 'green' if bin(int(data[2:4][0:2], base=16))[-3] == '1' else 'grey'
    smAMS = str(data[0:2][0:2])
    smAMS = AMSSTATES.get(smAMS)
    errorAMS = str(int(data[4:6][0:2], base=16))
    errorAMS = AMSERRORS.get(errorAMS)
    return k1, k2, k3, smAMS, errorAMS


def safetyFront(data):
    #0
    #1-Safe start 0 o 1
    #2-Front safety safe2->0, safe_inertia->1, safe_bots->3, fr->7, fl->15, safe_start->31, front_ok->3
    #2-Front safety safe2->0, safe2_inertia->1, safe_bots->3, fr->7, fl
    #2-OK->63,Inertia->60,seta_cockpit->62,BOTS->56,
    #k3
    #print(data)
    safe=int(data[4:6][0:2],base=16)
    #print(safe)
    if safe==63:
        frontSafetyState='Front ok'
    elif safe==62:
        frontSafetyState='Seta cockpit'
    elif safe==60:
        frontSafetyState='Safe Inertia'
    elif safe==56:
        frontSafetyState='Safe BOTS'
    elif safe==48:
        frontSafetyState='Safe FR'
    elif safe==32:
        frontSafetyState='Safe FL'
    else:
        frontSafetyState='Safe 2'


    return frontSafetyState

def safety(data):
    state = str(data[12:14][0:2])
    safety = STATES.get(state)
    imd = 'red' if str(data[8:10][0:2])=='01' else 'grey'
    ams = 'red' if str(data[10:12][0:2]) == '01' else 'grey'
    plausibility = 'yellow' if str(data[14:16][0:2]) == '01' else 'grey'
    carState=str(data[0:2][0:2])
    try:
        carState = CARSTATES.get(carState)
    except KeyError:
        carState = "TETAS"

    return safety, imd, ams, plausibility, carState

def motorData(data1, data2, data3, data4):
    sw1 = int(data1[2:4]+data1[0:2],base=16)
    ls1 = int(data1[10:12]+data1[8:10]+data1[6:8]+data1[4:6],base=16)
    sw2 = int(data2[2:4]+data2[0:2], base=16)
    ls2 = int(data2[10:12] + data2[8:10] + data2[6:8] + data2[4:6], base=16)
    sw3 = int(data3[2:4]+data3[0:2], base=16)
    ls3 = int(data3[10:12] + data3[8:10] + data3[6:8] + data3[4:6], base=16)
    sw4 = int(data4[2:4]+data4[0:2], base=16)
    ls4 = int(data4[10:12] + data4[8:10] + data4[6:8] + data4[4:6], base=16)
    return sw1, ls1, sw2, ls2, sw3, ls3, sw4, ls4

def motorRPM(data1, data2, data3, data4):
    rpm1 = int(data1[6:8] + data1[4:6] + data1[2:4] + data1[0:2], base=16)*0.0000610352
    rpm2 = int(data2[6:8] + data2[4:6] + data2[2:4] + data2[0:2], base=16)*0.0000610352
    rpm3 = int(data3[6:8] + data3[4:6] + data3[2:4] + data3[0:2], base=16)*0.0000610352
    rpm4 = int(data4[6:8] + data4[4:6] + data4[2:4] + data4[0:2], base=16)*0.0000610352
    return rpm1, rpm2, rpm3, rpm4


def powerAndDCVoltage(data1, data2, data3, data4):
    #Aviso 60
    #Max 100
    temp1 = int(data1[2:4] + data1[0:2], base=16) * 0.0625
    temp2 = int(data2[2:4] + data2[0:2], base=16) * 0.0625
    temp3 = int(data3[2:4] + data3[0:2], base=16) * 0.0625
    temp4 = int(data4[2:4] + data4[0:2], base=16) * 0.0625
    power1 = int(data1[6:8] + data1[4:6], base=16) * 16
    power2 = int(data2[6:8] + data2[4:6], base=16) * 16
    power3 = int(data3[6:8] + data3[4:6], base=16) * 16
    power4 = int(data4[6:8] + data4[4:6], base=16) * 16
    return temp1, temp2, temp3, temp4, power1, power2, power3, power4


def speedAndYawRateRef(data):
    speed = round(int(data[8:10], base=16)*3.6/10, 4)
    yawRateRef = int(data[10:12], base=16)
    return speed, yawRateRef


def torqueCommands(data1, data2, data3, data4):
    tqCom1 = int(data1[14:16] + data1[12:14], base=16)
    tqCom2 = int(data2[2:4] + data2[0:2], base=16)
    tqCom3 = int(data3[14:16] + data3[12:14], base=16)
    tqCom4 = int(data4[2:4] + data4[0:2], base=16)
    return tqCom1, tqCom2, tqCom3, tqCom4


def currents(data1, data2, data3, data4):
    current1 = [int(i[12:14] + i[14:16], base=16) for i in data1]
    current2 = [int(i[12:14] + i[14:16], base=16) for i in data2]
    current3 = [int(i[12:14] + i[14:16], base=16) for i in data3]
    current4 = [int(i[12:14] + i[14:16], base=16) for i in data4]
    datosX = [i for i in range(len(current1))]
    figure_1 = go.Figure(
        data=[go.Scatter(
            x=datosX,
            y=current1,
            mode='lines',
            name='Current FL',
            marker=dict(color='green')
        ),
            go.Scatter(
                x=datosX,
                y=current2,
                mode='lines',
                name='Current FR',
                marker=dict(color='red')
            ),
            go.Scatter(
                x=datosX,
                y=current3,
                mode='lines',
                name='Current RL',
                marker=dict(color='grey')
            ),
            go.Scatter(
                x=datosX,
                y=current4,
                mode='lines',
                name='Current RR',
                marker=dict(color='blue')
            ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (-200, 200)}
    return figure_1


def updateYawRate(data1, data2):
    yawRate = [int(i[10:12] + i[8:10], base=16)/1000 for i in data1]
    yawRateRef = [int(i[10:12], base=16) for i in data2]
    datosX = [i for i in range(len(yawRate))]
    figure_1 = go.Figure(
        data=[go.Scatter(
            x=datosX,
            y=yawRate,
            mode='lines',
            name='Yaw Rate',
            marker=dict(color='red')
        ),
            go.Scatter(
                x=datosX,
                y=yawRateRef,
                mode='lines',
                name='Yaw Rate Ref',
                marker=dict(color='grey')
        ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (-3, 3)}
    return figure_1

def updateSteeringWheel(data1):
    steeringWheel = round((int(data1[2:4], base=16) - 120) * 0.2083, 5)
    return steeringWheel


def dashData(data):
    power = int(data[8:10], base=16)
    tvValue = int(data[6:8], base=16)
    return power, tvValue


def tvRunning(data):
    tvRunning = 'green' if bin(int(data[14:16][0:2], base=16))[-1] == '1' else 'grey'
    return tvRunning


def updateStatuswordTranslation(data1,data2,data3,data4):
    ls1 = bin(int(data1[10:12] + data1[8:10] + data1[6:8] + data1[4:6], base=16)).removeprefix("b").zfill(32)
    ls2 = bin(int(data2[10:12] + data2[8:10] + data2[6:8] + data2[4:6], base=16)).split()[0].zfill(32)
    ls3 = bin(int(data3[10:12] + data3[8:10] + data3[6:8] + data3[4:6], base=16)).split()[0].zfill(32)
    ls4 = bin(int(data4[10:12] + data4[8:10] + data4[6:8] + data4[4:6], base=16)).split()[0].zfill(32)
    print("REVISAME")
    #print(len(ls1))
    children =html.Div(children=[
                html.Div(children=[daq.Indicator(
                            id="motor1",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls1[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor1"),
                html.Div(children=[daq.Indicator(
                            id="motor2",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls2[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor2"),
                html.Div(children=[daq.Indicator(
                            id="motor3",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls3[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor3"),
                html.Div(children=[daq.Indicator(
                            id="motor4",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls4[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ])])


import dash.html as html
import dash_daq as daq
import plotly.graph_objects as go

statuses = [
    "Event buffer has a new event entry since last upload",
    "Event buffer is full and has missed at least one event",
    "Power module over current detected by hardware",
    "Power module current offset calibration failed",
    "Power module temperature sensor defective",
    "Power module temperature has reached warning level",
    "Power module temperature has reached error level",
    "Power module i*t error",
    "Power module over current detected by software",
    "Power module pattern data inconsistency",
    "Dc link over voltage detected by hardware",
    "Dc link over voltage detected by software",
    "Dc link undervoltage detectedy by software",
    "Fault of the other inverter on the same device",
    "Motor temperature sensor defective",
    "Motor temperature has reached warning level",
    "Motor temperature has reached error level",
    "Motor stator frequency to high",
    "Board supply voltage error",
    "Receive PDO timeout",
    "NMT not in state operational",
    "Task calculation time overrun",
    "Net synchronisation error",
    "Position device signal to low",
    "Position device signal to high",
    "Resolver calibration failed",
    "System error, analog input or motor feedback DMA error",
    "Interlock open due to open cover sheet",
    "Gate driver disabled by APPC",
    "Motor stall error",
    "Ambient temperature has reached warning level",
    "Ambient temperature has reached error level"
]


STATES = {'00' : 'Safe 1',
    '01' : 'Safe 2 Front',
    '02' : 'Safe 2 BOTS',
    '03' : 'Safe 2 FL',
    '04' : 'Safe 2 FR',
    '05' : 'Safe 2 Cockpit',
    '06' : 'Safe 2 Inertia',
    '07' : 'Safe 3 Mainhoop',
    '08' : 'Safe 4 Accu',
    '09' : 'Safe 5 RL',
    '0a' : 'Safe 6 RR',
    '0b' : 'Safe 7 BSPD',
    '0c' : 'Safe 8 Interlocks',
    '0d' : 'Safe End Vload',
    '0e' : 'Safe OK'
}

CARSTATES = {
    '00' : 'Init',
    '01' : 'Standby',
    '02' : 'Precharge',
    '03' : 'Energized',
    '04' : 'Running',
    '05' : 'Error'
}

AMSSTATES = {
    '01' : 'Charge waiting',
    '02' : 'Charge precharge',
    '03' : 'Charge charging',
    '04' : 'Car waiting',
    '05' : 'Car precharge',
    '06' : 'Car RTD',
    '07' : 'Error',
    '08' : 'Critical Error'
}

AMSERRORS = {
    '0' : 'OK',
    '1' : 'VLoad',
    '2' : 'IMD',
    '4' : 'ECU Timeout',
    '8' : 'Current',
    '16' : 'Error contactores',
    '32' : 'Voltaje',
    '64' : 'Temperatura',
    '128' : 'Slaves Timeout'
}

def updateFigure1(data):
    datosAcc = [int(i[10:12],base=16) for i in data]
    datosBrk = [int(i[6:8],base=16) for i in data]
    datosX = [i for i in range(len(datosAcc))]
    figure_1 = go.Figure(

        data = [go.Scatter(
            x = datosX,
            y = datosAcc,
            mode = 'lines',
            name='Acc',
            marker = dict(color = 'green')
        ),
            go.Scatter(
                x=datosX,
                y=datosBrk,
                mode='lines',
                name='Brk',
                marker=dict(color='red')
            ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (0, 250)}
    return figure_1






def updateFigure2(data):
    datosY = []
    datosY.append(int(data[0:2], base=16))
    datosY.append(int(data[3:5], base=16))
    datosX = [i for i in range(len(datosY))]

    figure_2 = {
        "data": [
            {
                "x": datosX,
                "y": datosY,
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "xaxis": {"fixedrange": True},
            "yaxis": {"range":(0,200)},
            "colorway": ["#e30202", "#302f2f", "#000000", "#15ff00", "#0062ff", "#ff00f7"],
        },
    }
    return figure_2


def updateVoltages(data):
    minVoltage = round(float(int(data[0:2], base=16) / 51.0),3)
    totalVoltage = round(minVoltage*144,4)
    idMinVoltage = int(data[2:4][0:2], base=16)
    maxVoltage = round(float(int(data[4:6], base=16) / 51.0), 3)
    idMaxVoltage = int(data[6:8][0:2], base=16)
    if totalVoltage>532.8:
        colorVoltage='green'
    elif totalVoltage>512:
        colorVoltage='orange'
    else:
        colorVoltage='red'
    return totalVoltage, minVoltage, idMinVoltage, colorVoltage, maxVoltage, idMaxVoltage


def contactorFeedbackAndAMSState(data):
    k1 = 'green' if bin(int(data[2:4][0:2], base=16))[-1] == '1' else 'grey'
    k2 = 'green' if bin(int(data[2:4][0:2], base=16))[-2] == '1' else 'grey'
    k3 = 'green' if bin(int(data[2:4][0:2], base=16))[-3] == '1' else 'grey'
    smAMS = str(data[0:2][0:2])
    smAMS = AMSSTATES.get(smAMS)
    errorAMS = str(int(data[4:6][0:2], base=16))
    errorAMS = AMSERRORS.get(errorAMS)
    return k1, k2, k3, smAMS, errorAMS


def safetyFront(data):
    #0
    #1-Safe start 0 o 1
    #2-Front safety safe2->0, safe_inertia->1, safe_bots->3, fr->7, fl->15, safe_start->31, front_ok->3
    #2-Front safety safe2->0, safe2_inertia->1, safe_bots->3, fr->7, fl
    #2-OK->63,Inertia->60,seta_cockpit->62,BOTS->56,
    #k3
    #print(data)
    safe=int(data[4:6][0:2],base=16)
    #print(safe)
    if safe==63:
        frontSafetyState='Front ok'
    elif safe==62:
        frontSafetyState='Seta cockpit'
    elif safe==60:
        frontSafetyState='Safe Inertia'
    elif safe==56:
        frontSafetyState='Safe BOTS'
    elif safe==48:
        frontSafetyState='Safe FR'
    elif safe==32:
        frontSafetyState='Safe FL'
    else:
        frontSafetyState='Safe 2'


    return frontSafetyState

def safety(data):
    state = str(data[12:14][0:2])
    safety = STATES.get(state)
    imd = 'red' if str(data[8:10][0:2])=='01' else 'grey'
    ams = 'red' if str(data[10:12][0:2]) == '01' else 'grey'
    plausibility = 'yellow' if str(data[14:16][0:2]) == '01' else 'grey'
    carState=str(data[0:2][0:2])
    try:
        carState = CARSTATES.get(carState)
    except KeyError:
        carState = "TETAS"

    return safety, imd, ams, plausibility, carState

def motorData(data1, data2, data3, data4):
    sw1 = int(data1[2:4]+data1[0:2],base=16)
    ls1 = int(data1[10:12]+data1[8:10]+data1[6:8]+data1[4:6],base=16)
    sw2 = int(data2[2:4]+data2[0:2], base=16)
    ls2 = int(data2[10:12] + data2[8:10] + data2[6:8] + data2[4:6], base=16)
    sw3 = int(data3[2:4]+data3[0:2], base=16)
    ls3 = int(data3[10:12] + data3[8:10] + data3[6:8] + data3[4:6], base=16)
    sw4 = int(data4[2:4]+data4[0:2], base=16)
    ls4 = int(data4[10:12] + data4[8:10] + data4[6:8] + data4[4:6], base=16)
    return sw1, ls1, sw2, ls2, sw3, ls3, sw4, ls4

def motorRPM(data1, data2, data3, data4):
    rpm1 = int(data1[6:8] + data1[4:6] + data1[2:4] + data1[0:2], base=16)*0.0000610352
    rpm2 = int(data2[6:8] + data2[4:6] + data2[2:4] + data2[0:2], base=16)*0.0000610352
    rpm3 = int(data3[6:8] + data3[4:6] + data3[2:4] + data3[0:2], base=16)*0.0000610352
    rpm4 = int(data4[6:8] + data4[4:6] + data4[2:4] + data4[0:2], base=16)*0.0000610352
    return rpm1, rpm2, rpm3, rpm4


def powerAndDCVoltage(data1, data2, data3, data4):
    #Aviso 60
    #Max 100
    temp1 = int(data1[2:4] + data1[0:2], base=16) * 0.0625
    temp2 = int(data2[2:4] + data2[0:2], base=16) * 0.0625
    temp3 = int(data3[2:4] + data3[0:2], base=16) * 0.0625
    temp4 = int(data4[2:4] + data4[0:2], base=16) * 0.0625
    power1 = int(data1[6:8] + data1[4:6], base=16) * 16
    power2 = int(data2[6:8] + data2[4:6], base=16) * 16
    power3 = int(data3[6:8] + data3[4:6], base=16) * 16
    power4 = int(data4[6:8] + data4[4:6], base=16) * 16
    return temp1, temp2, temp3, temp4, power1, power2, power3, power4


def speedAndYawRateRef(data):
    speed = round(int(data[8:10], base=16)*3.6/10, 4)
    yawRateRef = int(data[10:12], base=16)
    return speed, yawRateRef


def torqueCommands(data1, data2, data3, data4):
    tqCom1 = int(data1[14:16] + data1[12:14], base=16)
    tqCom2 = int(data2[2:4] + data2[0:2], base=16)
    tqCom3 = int(data3[14:16] + data3[12:14], base=16)
    tqCom4 = int(data4[2:4] + data4[0:2], base=16)
    return tqCom1, tqCom2, tqCom3, tqCom4


def currents(data1, data2, data3, data4):
    current1 = [int(i[12:14] + i[14:16], base=16) for i in data1]
    current2 = [int(i[12:14] + i[14:16], base=16) for i in data2]
    current3 = [int(i[12:14] + i[14:16], base=16) for i in data3]
    current4 = [int(i[12:14] + i[14:16], base=16) for i in data4]
    datosX = [i for i in range(len(current1))]
    figure_1 = go.Figure(
        data=[go.Scatter(
            x=datosX,
            y=current1,
            mode='lines',
            name='Current FL',
            marker=dict(color='green')
        ),
            go.Scatter(
                x=datosX,
                y=current2,
                mode='lines',
                name='Current FR',
                marker=dict(color='red')
            ),
            go.Scatter(
                x=datosX,
                y=current3,
                mode='lines',
                name='Current RL',
                marker=dict(color='grey')
            ),
            go.Scatter(
                x=datosX,
                y=current4,
                mode='lines',
                name='Current RR',
                marker=dict(color='blue')
            ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (-200, 200)}
    return figure_1


def updateYawRate(data1, data2):
    yawRate = [int(i[10:12] + i[8:10], base=16)/1000 for i in data1]
    yawRateRef = [int(i[10:12], base=16) for i in data2]
    datosX = [i for i in range(len(yawRate))]
    figure_1 = go.Figure(
        data=[go.Scatter(
            x=datosX,
            y=yawRate,
            mode='lines',
            name='Yaw Rate',
            marker=dict(color='red')
        ),
            go.Scatter(
                x=datosX,
                y=yawRateRef,
                mode='lines',
                name='Yaw Rate Ref',
                marker=dict(color='grey')
        ),
        ]
    )
    figure_1['layout']['yaxis'] = {'range': (-3, 3)}
    return figure_1

def updateSteeringWheel(data1):
    steeringWheel = round((int(data1[2:4], base=16) - 120) * 0.2083, 5)
    return steeringWheel


def dashData(data):
    power = int(data[8:10], base=16)
    tvValue = int(data[6:8], base=16)
    return power, tvValue


def tvRunning(data):
    tvRunning = 'green' if bin(int(data[14:16][0:2], base=16))[-1] == '1' else 'grey'
    return tvRunning


def updateStatuswordTranslation(data1,data2,data3,data4):
    ls1 = bin(int(data1[10:12] + data1[8:10] + data1[6:8] + data1[4:6], base=16)).removeprefix("b").zfill(32)
    ls2 = bin(int(data2[10:12] + data2[8:10] + data2[6:8] + data2[4:6], base=16)).split()[0].zfill(32)
    ls3 = bin(int(data3[10:12] + data3[8:10] + data3[6:8] + data3[4:6], base=16)).split()[0].zfill(32)
    ls4 = bin(int(data4[10:12] + data4[8:10] + data4[6:8] + data4[4:6], base=16)).split()[0].zfill(32)
    print("REVISAME")
    #print(len(ls1))
    children =html.Div(children=[
                html.Div(children=[daq.Indicator(
                            id="motor1",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls1[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor1"),
                html.Div(children=[daq.Indicator(
                            id="motor2",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls2[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor2"),
                html.Div(children=[daq.Indicator(
                            id="motor3",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls3[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ], className="motor3"),
                html.Div(children=[daq.Indicator(
                            id="motor4",
                            label=statuses[i],
                            labelPosition="right",
                            color="grey" if ls4[-1-i]=='0' else 'green',
                            value=False,
                            style={'float' : 'left'}
                            )for i in range(len(statuses))
                ])])


    return children