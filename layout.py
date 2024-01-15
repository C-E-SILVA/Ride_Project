from dash import html
import dash_bootstrap_components as dbc
from components import (
                bar_chart, 
                dates_dropdown,
                bourogh_dropdown
            )

 
def create_layout(app,data):
    heading = html.H1(
        'Ride Shares',
        className = 'bg-info text-white p-2 mb-3'
    )
    return dbc.Container([
        dbc.Row([
            dbc.Col(heading)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(
                [
                    bourogh_dropdown.render(app,data), 
                    dates_dropdown.render(app,data)
                ],
                className="dropdown-container"
                ),lg= 6)
            
        ]),
        dbc.Row([
            dbc.Col(html.H3(
        'Rides Quantity - Pickup / Dropoff',
        className = 'bg-primary text-white p-2 mb-3'
        ))
        ]),
        dbc.Row([
            dbc.Col(bar_chart.render_1(app, data), lg=6),
            dbc.Col(bar_chart.render_3(app, data), lg=6),
        ]),

        dbc.Row([
            dbc.Col(bar_chart.render_7(app, data), lg=6),
            dbc.Col(bar_chart.render_8(app, data), lg=6),
        ]),
        dbc.Row([
            dbc.Col(html.H3(
        'Rides Profit - Pickup / Dropoff',
        className = 'bg-primary text-white p-2 mb-3'
        ))
        ]),
        dbc.Row([
            dbc.Col(bar_chart.render_5(app, data), lg=6),
            dbc.Col(bar_chart.render_6(app, data), lg=6),
        ]),
        dbc.Row([
            dbc.Col(bar_chart.render_9(app, data), lg=6),
            dbc.Col(bar_chart.render_10(app, data), lg=6),
        ]),
        dbc.Row([
            dbc.Col(html.H3(
        'Hour of Day Rides Quantity - Pickup / Dropoff',
        className = 'bg-primary text-white p-2 mb-3'
        ))
        ]),
        dbc.Row([
            dbc.Col(bar_chart.render_2(app, data), lg=6),
            dbc.Col(bar_chart.render_4(app, data), lg=6),
        ]),
     ])