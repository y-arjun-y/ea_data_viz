# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import html

from components.header import header
from components.sidebar import sidebar
from components.about import about_box
from components.body import body

from utils.get_data.refresh_data import refresh_data
from dash.dependencies import Input, Output, State

import dash_defer_js_import as dji

metas = [
    {"property": "twitter:card", "content": "summary_large_image"},
    {"property": "og:title", "content": "Effective Altruism Data"},
    {
        "property": "og:description",
        "content": "Aggregating and visualizing data from EA organisations, including grants, donors, and pledges.",
    },
    {"property": "og:url", "content": "https://effectivealtruismdata.com"},
    {"property": "og:site_name", "content": "Effective Altruism Data"},
    {
        "property": "og:image",
        "content": "https://rawcdn.githack.com/y-arjun-y/ea_data_viz/c4b92d4dd914d4c168d65f3f19538e859ebce949/eadata-twittercard.png",
    },
    {"property": "og:image:width", "content": "800"},
    {"property": "og:image:height", "content": "418"},
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
]

main_script = dji.Import(src="../assets/main.js")

app = dash.Dash(
    __name__,
    meta_tags=metas,
)

app.title = "Effective Altruism Data"

server = app.server

# refresh_data()

# def serve_layout():
#     return html.Div(
app.layout = html.Div(
    [
        main_script,
        header(),
        html.Div(
            [
                html.Div(
                    [
                        sidebar(),
                    ],
                ),
                about_box(),
                body(),
            ],
            className="body",
        ),
    ],
)

app.clientside_callback(
    """
    function (value) {
            document.getElementById("x-risks-output").innerHTML = "<h3>Try clicking a cell!</h3>"
            if (value["row"] == 0) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/landmark-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 1,000,000</h1><p>is approximately the odds of any one of the next 24 babies born in the U.S. becoming the President.</p>"
            } 
            else if (value["row"] == 1 || value["row"] == 3 || value["row"] == 7) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/clover-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 10,000</h1><p>is approximately the odds of finding a four-leaf clover.</p>"
            } else if (value["row"] == 2) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/baseball-solid.svg";
                document.getElementById("x-risks-img").setAttribute("class", "baseball");
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 1,000,000,000</h1><p>is approximately the odds of catching two foul-balls in a baseball game in a row.</p>"
            } else if (value["row"] == 4 || value["row"] == 5 || value["row"] == 6) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/cake-candles-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 1,000</h1><p>is approximately the odds of being born on February 29th.</p>"
            } else if (value["row"] == 8 || value["row"] == 10) {
            document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/dice-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 30</h1><p>is approximately the odds of getting snake-eyes (rolling two ones) on two die.</p>"
            } else if (value["row"] == 9) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/phone-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 10</h1><p>is the odds of guessing the first digit of a phone number correctly.</p>"
            } else if (value["row"] == 11) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/mask-face-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 50</h1><p>is approximately the odds of guessing a person had COVID-19 in England in Oct 2021.</p>"
            } else if (value["row"] == 12 || value["row"] == 13) {
                document.getElementById("x-risks-img").src = "/assets/images/x-risks-imgs/dice-solid.svg";
                document.getElementById("x-risks-output").innerHTML = "<h1>1 in 6</h1><p>is the odds of getting 1 on a dice roll.</p>"
            }
        }
    """,
    Output("x-risks-output", "children"),
    [Input("table", "active_cell")],
)

# app.layout = serve_layout

if __name__ == "__main__":
    app.run_server(debug=False)
