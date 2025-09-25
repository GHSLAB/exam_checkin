import dash
from dash import dcc
from dash import html
from datetime import datetime

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State, MATCH, ALL


from server import app

from views import select_seat, confirm_user


class config:
    title = "考务辅助系统"
    sub_title = "笔试考场签到"
    exam_time = "2025年"
    exam_name = "摸鱼专业技能"
    exam_location = "摸鱼大学"
    org = "摸鱼技术协会"


class room:
    room_num = "101"


def get_current_date_time_period():
    now = datetime.now()
    # 获取月日，格式为"月-日"
    month_day = now.strftime("%m月%d日")
    # 判断上午或下午
    period = "上午" if now.hour < 12 else "下午"
    return f"{month_day}{period}"


def bar():
    return [
        html.Div(
            [
                fac.AntdCenter(
                    fac.AntdText(
                        config.title,
                        style=style(
                            fontSize="28px",
                            fontFamily="微软雅黑",
                            fontWeight="bold",
                            color="#135FAB",
                            letterSpacing="6px",
                        ),
                    ),
                    style=style(height="80px"),
                )
            ],
            style=style(height="80px", width="100%", background="#E6EFFF"),
        ),
        html.Div(
            [
                fac.AntdCenter(
                    fac.AntdText(
                        config.sub_title,
                        style=style(
                            fontSize="20px",
                            fontFamily="微软雅黑",
                            fontWeight="bold",
                            color="#FFFFFF",
                            letterSpacing="4px",
                        ),
                    ),
                    style=style(height="60px"),
                )
            ],
            style=style(height="60px", width="100%", background="#287ACE"),
        ),
        html.Div(
            [
                fac.AntdCenter(
                    fac.AntdText(
                        f"{config.exam_time} {config.exam_name}考试",
                        style=style(
                            fontSize="18px",
                            fontFamily="黑体",
                            fontWeight="bold",
                            color="#FFFFFF",
                            # letterSpacing="2px",
                        ),
                    ),
                    style=style(height="50px"),
                )
            ],
            style=style(
                height="50px",
                width="calc(100% - 40px)",
                background="#E76A34",
                borderRadius=5,
                margin=20,
            ),
        ),
    ]


def footer():
    return [
        html.Div(
            [
                fac.AntdCenter(
                    [
                        fac.AntdText(
                            f"© {config.org}",
                            style=style(
                                fontSize="16px",
                                fontFamily="黑体",
                                # fontWeight="bold",
                                # letterSpacing="2px",
                            ),
                        )
                    ],
                    style=style(height="40px"),
                )
            ],
            style=style(
                position="absolute",
                borderTop="2px solid #287ACE",
                left=0,
                bottom=0,
                backgroundColor="#F4F4F4",
                height="40px",
                width="100vw",
                maxWidth="500px",
            ),
        ),
    ]


def exam_info():
    return (
        fac.AntdFlex(
            [
                fac.AntdCenter(
                    fac.AntdText(
                        f"{config.exam_location} {get_current_date_time_period()}",
                        style=style(
                            fontSize="18px",
                            fontFamily="黑体",
                            fontWeight="bold",
                        ),
                    )
                ),
                fac.AntdCenter(
                    fac.AntdText(
                        f"{room.room_num} 考场",
                        style=style(
                            fontSize="18px",
                            fontFamily="黑体",
                            fontWeight="bold",
                        ),
                    )
                ),
            ],
            vertical=True,
            gap=0,
        ),
    )


# 布局
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        fac.AntdCenter(
            html.Div(
                [
                    *bar(),
                    *exam_info(),
                    html.Div(
                        id="main-content",
                        style=style(padding=20, fontSize=16, width="calc(100% - 40px)"),
                    ),
                    *footer(),
                ],
                style=style(
                    position="relative",
                    height="100vh",
                    width="100vw",
                    maxWidth="500px",
                    background="#FFFFFF",
                    # padding=20,
                ),
            ),
        ),
    ],
    style=style(height="100vh", width="100vw", background="#CDCDCD"),
)


######
# 回调
######

@app.callback(
    Output("main-content", "children"),
    Input("url", "pathname"),
)
def router(pathname):
    if pathname == "/":
        return select_seat.render()

    elif pathname.startswith("/roomid-"):  # 示例：处理/roomid-101这样的路径
        room_id = pathname.split("-")[1]  # 获取考场ID
        return select_seat.render(room_id=room_id)

    return "404", None


if __name__ == "__main__":
    app.run(debug=True)