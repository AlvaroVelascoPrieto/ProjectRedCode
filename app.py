import dash
import dash_bootstrap_components as dbc
from dash import Output, Input

import figureCreator


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
from pages.logReader import dataDict
app.layout = dash.html.Div([
    dbc.Navbar([

                dash.html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(dash.html.Img(src="assets/fsb_round_logo.png", height="50px")),
                            dbc.Col(dbc.NavbarBrand("Formula Student Bizkaia", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="https://fsbizkaia.com",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.NavItem(dbc.NavLink(dbc.NavItem(dbc.NavLink("TEAM PAGE", href="https://fsbizkaia.com")))),
                dbc.NavItem(dbc.NavLink(dbc.NavItem(dbc.NavLink("SharePoint", href="https://fsbizkaia.sharepoint.com/_layouts/15/sharepoint.aspx"))))
            ],
        color="dark",
        dark=True,

    ),

        dash.page_container

    ],
    className="body"
)

@app.callback(
    [Output("price-chart", "figure"), Output("log-filter", "multi"), Output("corner1-chart", "figure"), Output("corner2-chart", "figure"), Output("corner3-chart", "figure"), Output("corner4-chart", "figure") ],
    [
        Input("comparisons", "on"),
        Input("log-filter", "value"),
        Input("data-filter", "value"),
        Input("time-range", "value"),
        Input("corner-filter", "value"),
    ],
)
def update_charts(on, log, dato, value, datoCorner):
    print("ALO")
    figure_1, multi = figureCreator.createFigure1(dataDict, on, log, dato, value, dash.ctx.triggered_id == 'comparisons')
    corner_1 = figureCreator.createFigure2(dataDict, on, log, datoCorner, value, dash.ctx.triggered_id == 'comparisons', 1)
    corner_2 = figureCreator.createFigure2(dataDict, on, log, datoCorner, value, dash.ctx.triggered_id == 'comparisons', 2)
    corner_3 = figureCreator.createFigure2(dataDict, on, log, datoCorner, value, dash.ctx.triggered_id == 'comparisons', 3)
    corner_4 = figureCreator.createFigure2(dataDict, on, log, datoCorner, value, dash.ctx.triggered_id == 'comparisons', 4)

    return figure_1, multi, corner_1, corner_2, corner_3, corner_4

if __name__ == '__main__':
    app.run_server(debug=True)