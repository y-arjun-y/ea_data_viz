# -*- coding: utf-8 -*-

from dash import html
import dash_dangerously_set_inner_html


def header():

    lightbulb_img_url = "/assets/images/ea-data/logo.png"
    # hamburger_img_url = "/assets/images/ui-images/hamburger-menu.svg"

    return html.Div(
        [
            # html.Img(
            #    src = hamburger_img_url,
            #    className='hamburger',
            # ),
            html.Div(
                dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                    """
                    <img
                        src='/assets/images/ui-images/hamburger-menu-2.svg'
                        onclick='toggleSidebarVisible()'
                        class='clickable-icon icon'
                        title='Show or hide contents'
                    >
                """
                ),
                className="icon",
            ),
            html.Img(
                src=lightbulb_img_url,
                className="icon",
            ),
            html.H1(
                [
                    html.Span(
                        "EA Data",
                        className="data",
                    ),
                ],
                className="main-title short-title",
            ),
            html.H1(
                [
                    html.Span(
                        "Effective ",
                        className="effective",
                    ),
                    html.Span(
                        "Altruism ",
                        className="altruism",
                    ),
                    html.Span(
                        "Data",
                        className="data",
                    ),
                ],
                className="main-title long-title",
            ),
            html.Div(
                [
                    html.Div(
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                            """
                            <img
                                src="/assets/images/ui-images/sun.svg"
                                onclick='toggleDarkMode()'
                                class='clickable-icon icon'
                                title="Change appearance"
                                id='darkmode-button'
                            >
                        """
                        ),
                        className="icon",
                    ),
                    html.Div(
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                            """
                            <img
                                src='/assets/images/ui-images/question-mark.svg'
                                onclick='toggleAboutVisibility()'
                                class='clickable-icon icon'
                                title='About'
                            >
                        """
                        ),
                        className="icon",
                    ),
                ],
                className="right-icons",
            ),
        ],
        className="header center",
    )
