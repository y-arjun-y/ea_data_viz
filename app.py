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
import visdcc

metas = [
    {'property': "twitter:card", 'content': "summary_large_image"},
    {'property': 'og:title', 'content': 'Effective Altruism Data'},
    {'property': "og:description", 'content': "Aggregating and visualizing data from EA organisations, including grants, donors, and pledges."},
    {'property': "og:url", 'content': "https://effectivealtruismdata.com"},
    {'property': "og:site_name", 'content': "Effective Altruism Data"},
    {'property': "og:image", 'content':  "https://rawcdn.githack.com/y-arjun-y/ea_data_viz/c4b92d4dd914d4c168d65f3f19538e859ebce949/eadata-twittercard.png",},
    {'property': "og:image:width", 'content': "800"},
    {'property': "og:image:height", 'content': "418"},
    {'name': "viewport", 'content': "width=device-width, initial-scale=1.0"}
]

app = dash.Dash(
    __name__,
    meta_tags=metas
)

app.title = 'Effective Altruism Data'

server = app.server

# refresh_data()

# def serve_layout():
#     return html.Div(
app.layout = html.Div(
        [
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
                    visdcc.Run_js(id='javascript-body'),
                ],
                className = 'body',
                id="sidebar-visdcc",
            )
        ],
    )

@app.callback(
    Output('javascript-body', 'run'),
    [Input('sidebar-visdcc', 'n_clicks')])
def sidebar(x):
    if x: 
        return "document.getElementById('sidebar').setAttribute('onclick', 'mobileSidebar()'); var elements = document.getElementsByClassName('download-subtitle-visdcc'); for (var i = 0; i < elements.length; i++) { elements[i].setAttribute('download', ''); }"
    return ""

@app.callback(
    Output('javascript-header', 'run'),
    [Input('header-sidebar-visdcc', 'n_clicks')])
def sidebar(x):
    if x: 
        return "document.getElementById('sidebar').setAttribute('onclick', 'mobileSidebar()')"
    return ""


# app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=False)
