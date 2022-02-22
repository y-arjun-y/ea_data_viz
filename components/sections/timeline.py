# from dash import html
# import dash_core_components as dcc
# import pandas as pd
# import plotly.express as px
# from utils.subtitle import get_data_source

# df = pd.DataFrame([
#     dict(Start='2009', Finish='2010'),
#     dict(Start='2011', Finish='2012'),
#     dict(Start='2013', Finish='2035')
# ])

# fig = px.timeline(df, x_start="Start", x_end="Finish")
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

# def timeline_section():
#     return html.Div([
#         html.Div(
#             html.H2('Timeline of Humanity'),
#             className='section-title',
#         ),
#         html.Div(
#             id="timeline-d3"
#         ),
#         dcc.Graph(figure=fig),
#         get_data_source('timeline')
#     ], 
#         className = 'section',
#         id="timeline"
#     )
