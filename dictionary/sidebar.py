
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from testPage import TestView
from showToeicGrade import open_ybm_grade

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_sidebar_window(current_window):
    
    #window = Tk()

    #window.geometry("700x550")
    #window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        current_window,
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
        file=relative_to_assets("button_1.png"))
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
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: TestView(current_window),
        relief="flat"
    )
    button_2.place(
        x=0.0,
        y=90.0,
        width=700.0,
        height=88.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
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
        file=relative_to_assets("button_6.png"))
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
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("고사장 안내"),
        relief="flat"
    )
    button_4.place(
        x=0.0,
        y=360.0,
        width=700.0,
        height=88.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_ybm_grade(current_window),
        relief="flat"
    )
    button_5.place(
        x=0.0,
        y=450.0,
        width=700.0,
        height=100.0
    )

    current_window.mainloop()
    #window.resizable(False, False)
    #window.mainloop()