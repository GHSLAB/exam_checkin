from feffery_dash_utils.style_utils import style
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash
from dash import html

from server import app


def render():
    return html.Div(
        [
            fac.AntdCenter(
                fac.AntdSpace(
                    [
                        html.A(
                            fac.AntdButton(
                                "返回重选",
                                id="back-btn",
                                style=style(backgroundColor="#EFEFEF"),
                            ),
                            href="/select_seat",
                        ),
                        fac.AntdButton(
                            "下一步",
                            id="next-btn",
                            style=style(backgroundColor="#EFEFEF"),
                        ),
                    ],
                    direction="horizontal",
                ),
            ),
        ]
    )