import plotly.express as px
import plotly.graph_objects as go
from dash import dcc
from dash import html


class Line(dcc.Graph):
    def __init__(
        self,
        df,
        x="x",
        y="y",
        label="label",
        hover="hover",
        title=None,
        x_title="",
        y_title="",
        size=None,
        color=None,
        log_y=False,
        dollars=False,
        xanchor="right",
        yanchor="bottom",
    ):

        fig = go.Figure()

        annotations = []
        for val in df[label].unique():

            val_df = df.loc[df[label] == val]
            val_df = val_df.sort_values(by=[x, y])

            fig.add_trace(
                go.Scatter(
                    x=val_df[x],
                    y=val_df[y],
                    name=val,
                    hovertext=val_df[hover],
                    hovertemplate="%{hovertext}<extra></extra>",
                    mode="lines",
                    line=dict(
                        color="#0c869b",
                    ),
                )
            )

            val_df = val_df.loc[val_df[y].notnull()].reset_index()
            last_row = val_df.iloc[len(val_df) - 1]
            last_hover = last_row[hover]

            fig.add_trace(
                go.Scatter(
                    x=[last_row[x]],
                    y=[last_row[y]],
                    mode="markers",
                    marker=dict(
                        color="#0c869b",
                        size=10,
                    ),
                    hovertext=[last_hover],
                    hovertemplate="%{hovertext}<extra></extra>",
                )
            )

            annotations.append(
                dict(
                    x=last_row[x],
                    y=last_row[y],
                    xanchor=xanchor,
                    yanchor=yanchor,
                    text=f" {val}",
                    font={
                        "size": 13,
                    },
                    showarrow=False,
                )
            )

        if log_y:
            fig.update_layout(
                yaxis_type="log",
            )

        if dollars:
            fig.update_layout(
                yaxis_tickprefix="$",
            )

        top_margin = 40 if title else 0
        fig.update_layout(
            title=title,
            showlegend=False,
            xaxis=dict(
                title=x_title,
            ),
            yaxis=dict(
                title=y_title,
            ),
            annotations=annotations,
            margin=dict(l=0, r=0, t=top_margin, b=0),
            title_x=0.5,
        )

        super().__init__(figure=fig, responsive=True)
