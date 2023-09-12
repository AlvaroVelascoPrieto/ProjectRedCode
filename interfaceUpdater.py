import plotly.graph_objects as go

def updateFigure1(data):
    datosAcc = [int(i[10:12],base=16) for i in data]
    datosBrk = [int(i[8:10],base=16) for i in data]
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


def safety(data):
    #0
    #1-Safe start 0 o 1
    #2-Front safety safe2->0, safe_inertia->1, safe_bots->3, fr->7, fl->15, safe_start->31, front_ok->3
    #k3
    #print(data)
    safe=int(data[4:6][0:2],base=16)
    #print(safe)
    if safe==63:
        frontSafetyState='Front ok'
    elif safe==31:
        frontSafetyState='Safe Start'
    elif safe==15:
        frontSafetyState='Safe FL'
    elif safe==7:
        frontSafetyState='Safe FR'
    elif safe==3:
        frontSafetyState='Safe BOTS'
    elif safe==1:
        frontSafetyState='Safe Inertia'
    else:
        frontSafetyState='Safe 2'


    return frontSafetyState


def motorData(data1, data2, data3, data4):
    sw1 = int(data1[2:4]+data1[0:2],base=16)
    sw2 = int(data2[2:4]+data2[0:2], base=16)
    sw3 = int(data3[2:4]+data3[0:2], base=16)
    sw4 = int(data4[2:4]+data4[0:2], base=16)
    return sw1, sw2, sw3, sw4

def motorRPM(data1, data2, data3, data4):
    rpm1 = int(data1[6:8] + data1[4:6] + data1[2:4] + data1[0:2], base=16)*0.0000610352
    rpm2 = int(data2[6:8] + data2[4:6] + data2[2:4] + data2[0:2], base=16)*0.0000610352
    rpm3 = int(data3[6:8] + data3[4:6] + data3[2:4] + data3[0:2], base=16)*0.0000610352
    rpm4 = int(data4[6:8] + data4[4:6] + data4[2:4] + data4[0:2], base=16)*0.0000610352
    return rpm1, rpm2, rpm3, rpm4