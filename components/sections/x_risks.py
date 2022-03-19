from dash import html
import dash_table
import dash_dangerously_set_inner_html
import pandas as pd
from utils.subtitle import get_data_source

df = pd.read_csv("./assets/data/longtermism/x-risks.csv")


def x_risks_section():
    return html.Div(
        [
            html.Div(
                html.H2("Probability of X-Risks by Toby Ord"),
                className="section-title",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="table",
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict("records"),
                                style_cell=dict(textAlign="left"),
                                style_data_conditional=[
                                    {
                                        "if": {
                                            "state": "active"  # 'active' | 'selected'
                                        },
                                        "backgroundColor": "rgba(14, 122, 142, 0.3)",
                                        "border": "1px solid rgb(14, 122, 142)",
                                    }
                                ],
                                editable=False,
                            )
                        ]
                    ),
                    html.Div(
                        [
                            html.Div(
                                dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                                    """
                        <img
                            id="x-risks-img"
                            height="200px"
                        >
                        """
                                ),
                                id="x-risks-img-div",
                            ),
                            html.Div(id="x-risks-output"),
                        ],
                        id="x-risks-results",
                    ),
                ],
                className="x-risks",
            ),
            get_data_source("x-risks"),
        ],
        className="section",
        id="x-risks",
    )
