# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html

def header():

    lightbulb_img_url = '/assets/logo.png'
    hamburger_img_url = '/assets/hamburger-menu.svg'

    return html.Div(
        [
            #html.Img(
            #    src = hamburger_img_url,
            #    className='hamburger',
            #),
            html.Div(
                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <img
                        src='/assets/hamburger-menu.svg'
                        onclick='toggleSidebarVisible()'
                        class='hamburger'
                    >
                '''),
            ),
            html.Img(
                src = lightbulb_img_url,
                className='lightbulb',
            ),
            html.H1(
                [
                    html.Span(
                        'EA Data',
                        className = 'data',
                    ),
                ],
                className='main-title short-title',
            ),
            html.H1(
                [
                    html.Span(
                        'Effective ',
                        className = 'effective',
                    ),
                    html.Span(
                        'Altruism ',
                        className = 'altruism',
                    ),
                    html.Span(
                        'Data',
                        className = 'data',
                    ),
                ],
                className = 'main-title long-title',
            ),
        ],
        className='header main-title-and-bulb center',
    )
