from dash import html
import pandas as pd
from utils.plots.bar import Bar
from utils.subtitle import get_instructions
from utils.subtitle import get_data_source

tlycs_data_csv = pd.read_csv("./assets/data/openphil_grants.csv"),

def tlycs_cost():
    return html.Div(
        [
            html.Div(
                html.H2('The Life You Can Save Most Effective Charities - Cost per life/treatment'),
                className='section-title',
            ),
            get_data_source('tlycs-cost'),
            # html.Div(
            #     Bar(tlycs_data_csv)
            # )
        ],
        className = 'section',
        id='tlycs-cost',
    )
