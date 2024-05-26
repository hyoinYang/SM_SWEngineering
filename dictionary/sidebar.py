from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#from word_managing_page import ManagementController
from exam_place_seyeon import EtsPlaceController


# 파일 경로가 모두 resource 로 간소화됐기 때문에 아래 코드는 필요 없을 것 같아 주석처리했습니다. 나중에 처리해야함!!!!!!!!!!
"""
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./resource")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

"""
# ----------------------------- View -----------------------------
class SidebarView:

    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 550,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            -2.0,
            88.0,
            700.0,
            90.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -2.0,
            268.0,
            700.0,
            270.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -2.0,
            448.0,
            700.0,
            450.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -2.0,
            358.0,
            700.0,
            360.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            -2.0,
            178.0,
            700.0,
            180.0,
            fill="#000000",
            outline="")

        button_image_1 = PhotoImage(
            file=("resource/sidebar_button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("단어장"),
            relief="flat"
        )
        button_1.place(
            x=0.0,
            y=0.0,
            width=700.0,
            height=88.0
        )

        button_image_2 = PhotoImage(
            file=("resource/sidebar_button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("단어테스트"),
            relief="flat"
        )
        button_2.place(
            x=0.0,
            y=90.0,
            width=700.0,
            height=88.0
        )

        button_image_3 = PhotoImage(
            file=("resource/sidebar_button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("오답노트"),
            relief="flat"
        )
        button_3.place(
            x=0.0,
            y=180.0,
            width=700.0,
            height=88.0
        )

        button_image_6 = PhotoImage(
            file=("resource/sidebar_button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("토익 시험 날짜"),
            relief="flat"
        )
        button_6.place(
            x=0.0,
            y=270.0,
            width=700.0,
            height=88.0
        )

        button_image_4 = PhotoImage(
            file=("resource/sidebar_button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:EtsPlaceController(self),
            relief="flat"
        )
        button_4.place(
            x=0.0,
            y=360.0,
            width=700.0,
            height=88.0
        )

        button_image_5 = PhotoImage(
            file=("resource/sidebar_button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("시험 점수 조회"),
            relief="flat"
        )
        button_5.place(
            x=0.0,
            y=450.0,
            width=700.0,
            height=100.0
        )

class SidebarController:
    def __init__(self, root):
        self.view = SidebarView(root)


if __name__ == "__main__":
    root = tk.Tk()
    app = SidebarController(root)
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    root.mainloop()