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

app = dash.Dash(
    __name__,
    meta_tags = [
        {
            'og:title': 'Effective Altruism Data',
            "og:url": "https://effectivealtruismdata.com",
            "og:site_name": "Effective Altruism Data",
            "og:image": "https://i.ibb.co/mqbpdXW/eadata.png",
            "og:image:width": "1440",
            "og:image:height": "630",
            "twitter:card": "summary_large_image",
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0',
        }
    ],
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
    app.run_server(host="0.0.0.0", debug=True)
    # app.run_server(debug=False)
