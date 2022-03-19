from dash import html
from utils.subtitle import get_data_source
import json
import dash_dangerously_set_inner_html

content = []
flag = True

with open("assets/data/general_ea/EA-numbers.json") as json_file:
    data = json.load(json_file)
    for i in range(0, 94):
        content.append(data["notes"][i]["fields"])


def insert(source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]


def key_ea_numbers():
    return html.Div(
        [
            html.Div(
                html.H2("Key EA Numbers"),
                className="section-title",
            ),
            html.P(
                "Scroll down to view more flashcards. Click on them to reveal the answer and the source."
            ),
            html.Div(
                children=[
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(i + j + k)
                    for i, j, k in zip(
                        [
                            insert(i, " class='question' ", 2)
                            for list in content
                            for i in list
                        ][0::3],
                        [
                            insert(i, " class='answer' ", 2)
                            for list in content
                            for i in list
                        ][1::3],
                        [
                            insert(i, " class='answer' ", 2)
                            for list in content
                            for i in list
                        ][2::3],
                    )
                ],
                id="card-div",
            ),
            get_data_source("key-ea-numbers"),
        ],
        className="section",
        id="key-ea-numbers",
    )
