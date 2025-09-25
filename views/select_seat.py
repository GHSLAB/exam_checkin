from feffery_dash_utils.style_utils import style
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash

from server import app

from views import confirm_user


def render(room_id=101):
    return [
        fac.AntdCenter(
            fac.AntdText(
                f"{room_id} 考场",
                style=style(
                    fontSize="18px",
                    fontFamily="黑体",
                    fontWeight="bold",
                ),
            )
        ),
        fac.AntdText("请选择您的座位号:", style=style(fontSize=16)),
        fac.AntdFlex(
            [
                fac.AntdButton(
                    f"{str(i).zfill(2)}",
                    id={"type": "seat-btn", "index": i},
                    variant="filled",
                    style=style(
                        fontSize=20,
                        height="50px",
                        width="50px",
                        backgroundColor="#F3F3F3",
                    ),
                )
                for i in range(1, 31)
            ],
            wrap=True,
            gap=25,
            style=style(width="100%", padding=10),
        ),
    ]
