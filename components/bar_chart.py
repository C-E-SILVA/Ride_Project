from dash import html, dcc, Input, Output
import plotly.express as px

def render_1(app, data):

    @app.callback(
            Output("bar_chart", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):

        fieltered_data = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data = fieltered_data.groupby(['business'])[['rides_quantity']].sum()
        fieltered_data.reset_index(inplace=True)
        
        if fieltered_data.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart")
        fig = px.bar(

            fieltered_data,
            x = "business",
            y = "rides_quantity",
            color = "business"
            
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart")

    return html.Div(id = "bar_chart")

def render_2(app, data):

    @app.callback(
            Output("bar_chart2", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_1 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_1 = fieltered_data_1.groupby(['borough_pickup_location','business','date','hour_of_day'])[['rides_quantity']].sum()
        fieltered_data_1.reset_index(inplace=True)
        
        if fieltered_data_1.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart2")
        fig = px.bar(

            fieltered_data_1,
            x = "hour_of_day",
            y = "rides_quantity",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart2")

    return html.Div(id = "bar_chart2")

def render_3(app, data):

    @app.callback(
            Output("bar_chart3", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):

        fieltered_data_3 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_3 = fieltered_data_3.groupby(['date','zone_pickup_location','business'])[['rides_quantity']].sum().sort_values(['rides_quantity'],ascending=False).head(5)
        fieltered_data_3.reset_index(inplace=True)
        
        if fieltered_data_3.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart3")
        fig = px.bar(

            fieltered_data_3,
            x = "zone_pickup_location",
            y = "rides_quantity",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart3")

    return html.Div(id = "bar_chart3")

def render_4(app, data):

    @app.callback(
            Output("bar_chart4", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_4 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_4 = fieltered_data_4.groupby(['date','hour_of_day','business'])[['rides_quantity_dropoff']].sum()
        fieltered_data_4.reset_index(inplace=True)
        
        if fieltered_data_4.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart4")
        fig = px.bar(

            fieltered_data_4,
            x = "hour_of_day",
            y = "rides_quantity_dropoff",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart4")

    return html.Div(id = "bar_chart4")

def render_5(app, data):

    @app.callback(
            Output("bar_chart5", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_5 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_5 = fieltered_data_5.groupby(['date','business'])[['rideshare_profit']].sum()
        fieltered_data_5.reset_index(inplace=True)
        
        if fieltered_data_5.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart5")
        fig = px.bar(

            fieltered_data_5,
            x = "business",
            y = "rideshare_profit",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart5")

    return html.Div(id = "bar_chart5")

def render_6(app, data):

    @app.callback(
            Output("bar_chart6", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_6 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_6 = fieltered_data_6.groupby(['date','business','zone_pickup_location'])[['rideshare_profit']].sum().sort_values(['rideshare_profit'],ascending=False).head(5)
        fieltered_data_6.reset_index(inplace=True)
        
        if fieltered_data_6.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart6")
        fig = px.bar(

            fieltered_data_6,
            x = "zone_pickup_location",
            y = "rideshare_profit",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart6")

    return html.Div(id = "bar_chart6")

def render_7(app, data):

    @app.callback(
            Output("bar_chart_7", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):

        fieltered_data_7 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_7 = fieltered_data_7.groupby(['business'])[['rides_quantity_dropoff']].sum()
        fieltered_data_7.reset_index(inplace=True)
        
        if fieltered_data_7.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart_7")
        fig = px.bar(

            fieltered_data_7,
            x = "business",
            y = "rides_quantity_dropoff",
            color = "business"
            
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart_7")

    return html.Div(id = "bar_chart_7")

def render_8(app, data):

    @app.callback(
            Output("bar_chart_8", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):

        fieltered_data_8 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_8 = fieltered_data_8.groupby(['date','zone_pickup_location','business'])[['rides_quantity_dropoff']].sum().sort_values(['rides_quantity_dropoff'],ascending=False).head(5)
        fieltered_data_8.reset_index(inplace=True)
        
        if fieltered_data_8.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart_8")
        fig = px.bar(

            fieltered_data_8,
            x = "zone_pickup_location",
            y = "rides_quantity_dropoff",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart_8")

    return html.Div(id = "bar_chart_8")

def render_9(app, data):

    @app.callback(
            Output("bar_chart_9", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_9 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_9 = fieltered_data_9.groupby(['date','business'])[['rideshare_profit_dropoff']].sum()
        fieltered_data_9.reset_index(inplace=True)
        
        if fieltered_data_9.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart_9")
        fig = px.bar(

            fieltered_data_9,
            x = "business",
            y = "rideshare_profit_dropoff",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart_9")

    return html.Div(id = "bar_chart_9")

def render_10(app, data):

    @app.callback(
            Output("bar_chart_10", "children"),
            Input("bourogh_dropdown", "value"),
            Input("date_dropdown", "value")
    )
    def update_bar_char(bourogh, dates):
        
        fieltered_data_10 = data.query("borough_pickup_location in @bourogh and date in @dates")

        fieltered_data_10 = fieltered_data_10.groupby(['date','business','zone_pickup_location'])[['rideshare_profit_dropoff']].sum().sort_values(['rideshare_profit_dropoff'],ascending=False).head(5)
        fieltered_data_10.reset_index(inplace=True)
        
        if fieltered_data_10.shape[0]==0:
            return html.Div("No data selected", id = "bar_chart_10")
        fig = px.bar(

            fieltered_data_10,
            x = "zone_pickup_location",
            y = "rideshare_profit_dropoff",
            color = "business"
        )

        return html.Div(dcc.Graph(figure=fig), id = "bar_chart_10")

    return html.Div(id = "bar_chart_10")