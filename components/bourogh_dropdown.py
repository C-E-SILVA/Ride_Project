from dash import html, dcc, Input, Output


def render(app,data):
    all_bouroghs = data['borough_pickup_location'].unique()
    bouroghs_list = [{"label":bourogh, "value":bourogh} for bourogh in all_bouroghs]

    @app.callback(
        Output("bourogh_dropdown", "value"),
        [
            Input("bourogh_button","n_clicks")
        ]
    )
    def select_all_bouroghs(bourogh, n):
        filtered_data = data.query("borough_pickup_location in @ybourogh")
        return sorted(filtered_data['borough_pickup_location'].unique())
    return html.Div(
        [
            html.H6("Bourogh"),
            dcc.Dropdown(
                options = bouroghs_list,
                multi=False,
                id = "bourogh_dropdown"
            ),
            html.Button(
                children=["Select All"],
                n_clicks=0,
                id = "bourogh_button"
            )
        ]
    )