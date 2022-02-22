# from dash import html
# import dash_core_components as dcc
# from dash.dependencies import Input, Output

# def population_section():
#     return html.Div(
#          [
#              html.Div(
#                  html.H2('Population'),
#                  className='section-title',
#              ),
#              html.H3('Select a year/decade'),
#              dcc.Dropdown(
#                  id='demo-dropdown',
#                  options=[
#                      {'label': '2022', 'value': '2022'},
#                      {'label': '2021', 'value': '2022'},
#                      {'label': '2020', 'value': '2022'},
#                      {'label': '2019', 'value': '2022'},
#                      {'label': '2018', 'value': '2022'},
#                      {'label': '2017', 'value': '2022'},
#                      {'label': '2016', 'value': '2022'},
#                      {'label': '2015', 'value': '2022'},
#                      {'label': '2014', 'value': '2022'},
#                      {'label': '2013', 'value': '2022'},
#                      {'label': '2012', 'value': '2022'},
#                      {'label': '2011', 'value': '2022'},
#                      {'label': '2010', 'value': '2022'},
#                      {'label': '2009', 'value': '2022'},
#                      {'label': '2008', 'value': '2022'},
#                      {'label': '2007', 'value': '2022'},
#                      {'label': '2006', 'value': '2022'},
#                      {'label': '2005', 'value': '2022'},
#                      {'label': '2004', 'value': '2022'},
#                      {'label': '2003', 'value': '2022'},
#                      {'label': '2002', 'value': '2022'},
#                      {'label': '2001', 'value': '2022'},
#                      {'label': '2000', 'value': '2022'},
#                      {'label': '1990\'s', 'value': '1990'},
#                      {'label': '1980\'s', 'value': '1980'},
#                      {'label': '1970\'s', 'value': '1970'},
#                      {'label': '1960\'s', 'value': '1960'},
#                      {'label': '1950\'s', 'value': '1950'},
#                  ],
#                  value='2022'
#              ),
#              html.Div(id='dd-output-container'),
#              html.Div(
#                  html.Div([
#                      html.Div([
#                          html.H2(
#                              "Humans currently alive in 2022",
#                          ),
#                          html.H2(
#                              "7.9 billion"
#                          ),
#                      ], 
#                      className="factoid-div"),
#                      html.Div([
#                          html.H2(
#                              "Projected human population in 2100",
#                          ),
#                          html.H2(
#                              "~11.2 billion"
#                          ),
#                      ], 
#                      className="factoid-div"),
#                      html.Div([
#                          html.H2(
#                              "All humans ever born as of 2022",
#                          ),
#                          html.H2(
#                              "~116 billion"
#                          ),
#                      ], 
#                      className="factoid-div")
#                  ], id="factoid-div")
#              )
#          ],
#          className = 'section',
#          id="population"
#      )
