import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import re
from glob import glob

##################################
###       DEMOGRAPHICS         ###
##################################

def get_demo_table(demo_name):

    path = f"./data/rp_survey_data/{demo_name}.csv"
    demo_table = pd.read_csv(path, sep='\t')
    title = demo_table.columns[0]

    # remove the 'Total' row
    demo_table = demo_table[ ~demo_table[title].isin(['Total', 'Total respondents']) ]
    # demo_table['label'] = demo_table[title] + demo_table['Percent']
    # convert '5%' to 5
    demo_table['Percent'] = demo_table['Percent'].apply(lambda x: float(x[:-1]))



    subs = {
        'Eat meat, but try to reduce the amount  ': 'Reducetarian',
    #     # 'Eat meat': 'Meat',
    #     # 'Vegetarian': 'Veg.',
    #     # 'Pescetarian': 'Pesc.',
        'Other (please specify)': 'Other',

        'Native Hawaiian or Other Pacific Islander': 'Hawaiian or Pacific Islander',
        'American Indian or Alaskan Native': 'Native American or Alaskan', 
    #     'Black or African American': 'Black',
        'Hispanic, Latino or Spanish Origin': 'Hispanic or Latino',

    #     # 'Computer Science': 'CS',
    #     'Math': 'Math',
    #     # 'Economics': 'Econ',
    #     # 'Social Science': 'Soc. Sci.',
    #     # 'Philosophy': 'Phil',
    #     # 'Psychology': 'Science',#'Psych',
    #     # 'Arts & Humanities': 'Arts',
    #     # 'Sciences': 'Other',
    #     # 'Engineering': 'Other',
    #     # 'Physics': 'Other',
    #     # 'Psychology': 'Other',
    #     # 'Medicine': 'Other',
        'Professional or vocational qualification': 'Professional/Vocational qualification',

    #     'Employed, Full-Time': 'Employed (FT)',
    #     'Student, Full-Time': 'Student (FT)',
    #     'Employed, Part-Time': 'Employed (PT)',
        'Not employed, but looking for work': 'Not employed, looking for work',
    #     'Student, Part-Time': 'Student (PT)',
        'Not employed, but not looking for work': 'Not employed, not looking for work',
    #     # 'Homemaker ': 'Other',
    #     # 'Student, Part-Time': 'Student',
    #     # 'Self-Employed': 'Self-Employ',


        'Consequentialism (utilitarian)': 'Utilitarianism',
        'Consequentualism (other than utilitarian)': 'Other Consequentialism',

    #     # '13-17': '13-17'
    #     # 18-24
    #     # 25-34
    #     # 35-44
    #     # 45-54
    #     # 55-64
    #     # 65+
    }
    # max_chars = 20
    demo_table['label'] = demo_table[title].map(subs).fillna(demo_table[title])
    # demo_table['label'] = demo_table['label'].apply(lambda x: x.rjust(max_chars))

    # swap utilitarianism and consequentialism in the moral_belief table
    if title == 'Moral View':
        demo_table = demo_table.loc[[ 1, 0, 2, 3, 4 ], :]

    # # Normalise title
    # title_subs = {
    #     'Age Group': 'Age',
    #     'Employment Type': 'Employment',
    #     'Race/Ethnicity': 'Ethnicity',
    #     'Subject Studied': 'Subject Studied',
    #     'Moral View': 'Moral View',
    #     'Gender': 'Gender',
    #     'Diet ': 'Diet',
    #     'Education': 'Education',
    #     'Career path': 'Career path' 
    # }
    # title = title_subs[title]

    if title=='Gender':
        height = 200
    elif title=='Education':
        height = 250
    else:
        height_per_bar = 20 if len(demo_table) > 10 else 23
        height = height_per_bar * len(demo_table) + 30

    bar_fig = px.bar(
        demo_table,
        y='label',
        x='Percent',
        title=title,
        hover_data={
            # 'title': True,
            'Percent': True,
            # 'label': False
        },
        height=height,
        orientation='h',
        labels={
            'label': title,
            'Percent': 'Percentage',
        },
    )
    bar_fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(title=''),
        yaxis=dict(title=''),
        font=dict(
            # family="Courier New, monospace",
            # size=8,
            # color="RebeccaPurple"
        )
    )
    this_bar = dcc.Graph(
        id=title, #style={'margin': '0%'},
        figure=bar_fig,
        config={
            'displayModeBar': False,
        },
        # style={},
    )

    return this_bar

demo_names = [
        'gender',
        'ethnicity',
        'age_group',
        'education2',
        'subject',
        'career_path',
        'employment',
        'political_belief',
        'diet',
        'moral_view',
]

demo_bars = {
    demo_name: get_demo_table(demo_name)
    for demo_name in demo_names
}

demo_div = html.Div(
    [
        html.Div(
            [
                html.Div(
                    html.H2('Demographics'),
                    className='section-heading',
                ),
                html.Div(
                    demo_bars['gender'],
                    className='demo-column',
                    style={
                        'width': '25%'
                    }
                ),
                html.Div(
                    demo_bars['age_group'],
                    className='demo-column',
                    style={
                        'width': '25%'
                    }
                ),
                html.Div(
                    demo_bars['ethnicity'],
                    className='demo-column',
                    style={
                        'width': '40%'
                    }
                ),
            ],
            style={'overflow': 'auto'}
#            className='big-box'
        ),

        html.Div(
            [
                html.Div(
                    html.H2('Education'),
                    className='section-heading',
                ),
                html.Div(
                    demo_bars['education2'],
                    className='demo-column',
                    style={
                        'width': '30%'
                    }
                ),
                html.Div(
                    demo_bars['subject'],
                    className='demo-column',
                    style={
                        'width': '60%'
                    }
                ),
            ],
            style={'overflow': 'auto'}
#            className='big-box'
        ),

        html.Div(
            [
                html.Div(
                    html.H2('Career'),
                    className='section-heading',
                ),
                html.Div(
                    demo_bars['career_path'],
                    className='demo-column',
                    style={
                        'width': '45%'
                    }
                ),
                html.Div(
                    demo_bars['employment'],
                    className='demo-column',
                    style={
                        'width': '45%'
                    }
                ),
            ],
            style={'overflow': 'auto'}
#            className='big-box'
        ),

        html.Div(
            [
                html.Div(
                    html.H2('Beliefs'),
                    className='section-heading',
                ),
                html.Div(
                    demo_bars['political_belief'],
                    className='demo-column',
                    style={
                        'width': '30%'
                    }
                ),
                html.Div(
                    demo_bars['moral_view'],
                    className='demo-column',
                    style={
                        'width': '30%'
                    }
                ),
                html.Div(
                    demo_bars['diet'],
                    className='demo-column',
                    style={
                        'width': '30%'
                    }
                ),
            ],
            style={'overflow': 'auto'}
#            className='big-box'
        ),





#        html.P(
#            'There are about {} active members of the '.format(6500) + \
#            'Effective Altruism community. Who are they?'
#            # source: https://www.rethinkpriorities.org/blog/2020/6/26/ea-survey-2019-series-how-many-people-are-there-in-the-ea-community
#        ),
#        html.Div(
#            [
#                demo_bars['gender'],
#                demo_bars['age_group'],
#                demo_bars['ethnicity'],
#
#            ],
#            className='demo-column',
#            style = {
#                # 'background-color': 'yellow',
#            }
#        ),
#
#        html.Div(
#            [
#                demo_bars['diet'],
#                demo_bars['employment'],
#            ],
#            className='demo-column',
#            style = {
#                # 'background-color': 'red',
#            }
#        ),
#
#        html.Div(
#            [
#                demo_bars['subject'],
#                demo_bars['education2'],
#            ],
#            className='demo-column',
#            # style = {
#            #     # 'background-color': 'yellow',
#            # }
#        ),
#        html.Div(
#            [
#                demo_bars['moral_view'],
#            ],
#            className='demo-column',
#            # style = {
#            #     # 'background-color': 'yellow',
#            # }
#        ),


    ],
#    className='big-box'
)
