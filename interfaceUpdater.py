import plotly.graph_objects as go
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
            "title": {
                "text": 'dato',
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#e30202", "#302f2f", "#000000", "#15ff00", "#0062ff", "#ff00f7"],
        },
    }
    return figure_2


def updateVoltages(data):
    minVoltage = round(float(int(data[0:2], base=16) / 50.0),3)
    totalVoltage = round(minVoltage*144,4)
    idMinVoltage = int(data[1][0:2], base=16)
    if totalVoltage>532.8:
        colorVoltage='green'
    elif totalVoltage>512:
        colorVoltage='orange'
    else:
        colorVoltage='red'
    return totalVoltage, minVoltage, idMinVoltage, colorVoltage


def contactorFeedback(data):
    k1 = 'green' if bin(int(data[2:4][0:2], base=16))[-1] == '1' else 'grey'
    k2 = 'green' if bin(int(data[2:4][0:2], base=16))[-2] == '1' else 'grey'
    k3 = 'green' if bin(int(data[2:4][0:2], base=16))[-3] == '1' else 'grey'
    return k1, k2, k3


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
    plausibility = 'yellow' if str(data[8:10][0:2]) == '01' else 'grey'
    return safety, imd, ams, plausibility

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
    temp1 = int(data1[2:4] + data1[0:2], base=16) * 0.0625
    temp2 = int(data2[2:4] + data2[0:2], base=16) * 0.0625
    temp3 = int(data3[2:4] + data3[0:2], base=16) * 0.0625
    temp4 = int(data4[2:4] + data4[0:2], base=16) * 0.0625
    power1 = int(data1[6:8] + data1[4:6], base=16) * 16
    power2 = int(data2[6:8] + data2[4:6], base=16) * 16
    power3 = int(data3[6:8] + data3[4:6], base=16) * 16
    power4 = int(data4[6:8] + data4[4:6], base=16) * 16
    return temp1, temp2, temp3, temp4, power1, power2, power3, power4