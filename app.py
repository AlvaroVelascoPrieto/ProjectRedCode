import dash
import dash_bootstrap_components as dbc


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



if __name__ == '__main__':
    app.run_server(debug=True)