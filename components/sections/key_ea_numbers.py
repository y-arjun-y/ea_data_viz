from dash import html
import pandas as pd
from utils.subtitle import get_instructions
from utils.subtitle import get_data_source

def key_ea_numbers():
    return html.Div(
        [
            html.Div(
                html.H2('Key EA Numbers'),
                className='section-title',
            ),
            get_data_source("key-ea-numbers")
        ],
        className='section',
        id='key-ea-numbers',
    )
