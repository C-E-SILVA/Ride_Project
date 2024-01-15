from dash import html, dcc, Input, Output


def render(app,data):
    all_date = data["date"].unique()
    dates = [{'label': date, 'value': date} for date in all_date]
    
    @app.callback(
            Output("date_dropdown","value"),
            [
            Input("bourogh_dropdown", "value"),
            Input("date_button", "n_clicks"),
            ]
    )
    def select_all_dates(bourogh, n):
        filtered_data = data.query("borough_pickup_location in @bourogh")
        return sorted(filtered_data["date"].unique())
    return html.Div([
            html.H6("Dates"),
            dcc.Dropdown(
                options = dates,
                placeholder = "Choose your date",
                multi = False,
                id = "date_dropdown",
            ),
            html.Button(
                children=["Select All"],
                id = "date_button",
                n_clicks=0
            )
        ]
    )