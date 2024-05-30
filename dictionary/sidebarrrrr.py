#1 로그아웃을 아랫단에 붙이고 싶음
#2 관리자모드로 실행하면 시험 점수 아래 이어서 나오게 하고 싶음
#3 톱니바퀴 추가해야함
#4 예시로 만든 btn1, ... , btn7을 각 파일로 이어야함
#5 뼈대만 만들어 놨다 생각하면 편함
#6 관리자 쪽 토글메뉴는 일단 보류 해놨음

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from signup import SignupController
import webbrowser
from speak_word import SpeakWord
import random
from part_dict import PartDictController
from part_dict import PartDictModel
from titlebar import TitleView
from login import LoginController
import math
from tkinter.ttk import Progressbar, Label
import partbox as pb
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from examInfoClass import ExamDBModel

root = tk.Tk()
root.geometry('700x550')
root.title('토익 단어장')
root.configure(background="#FFFFFF")

def switch(indicator_lb, parent_frame, page):

    for child in parent_frame.winfo_children():
        if isinstance(child, tk.Label):
            child['bg']='#838383'

    indicator_lb['bg']='black'

    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()

option_fm = tk.Frame(root)

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)

    if (LoginController.is_login):
        toggle_menu_fm = tk.Frame(root, bg='#838383')

        toggle_btn1 = tk.Button(toggle_menu_fm, text='단어장', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn1_indicator_lb, parent_frame=toggle_menu_fm, page=btn1_page))
        toggle_btn1.pack(anchor='center')

        toggle_btn1_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn1_indicator_lb.place(x=110, y=33, width=80, height=2)

        canvas1 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas1.pack()
        canvas1.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn2 = tk.Button(toggle_menu_fm, text='단어 테스트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn2_indicator_lb, parent_frame=toggle_menu_fm, page=btn2_page))
        toggle_btn2.pack(anchor='center')

        toggle_btn2_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn2_indicator_lb.place(x=110, y=73, width=80, height=2)

        canvas2 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas2.pack()
        canvas2.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn3 = tk.Button(toggle_menu_fm, text='오답노트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn3_indicator_lb, parent_frame=toggle_menu_fm, page=btn3_page))
        toggle_btn3.pack(anchor='center')

        toggle_btn3_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn3_indicator_lb.place(x=110, y=113, width=80, height=2)

        canvas3 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas3.pack()
        canvas3.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn4 = tk.Button(toggle_menu_fm, text='토익 시험 날짜', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn4_indicator_lb, parent_frame=toggle_menu_fm, page=btn4_page))
        toggle_btn4.pack(anchor='center')

        toggle_btn4_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn4_indicator_lb.place(x=110, y=153, width=80, height=2)

        canvas4 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas4.pack()
        canvas4.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn5 = tk.Button(toggle_menu_fm, text='고사장 안내 및 시험 점수 조회', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn5_indicator_lb, parent_frame=toggle_menu_fm, page=btn5_page))
        toggle_btn5.pack(anchor='center')

        toggle_btn5_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn5_indicator_lb.place(x=110, y=193, width=80, height=2)

        canvas5 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas5.pack()
        canvas5.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn7 = tk.Button(toggle_menu_fm, text='로그아웃', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn7_indicator_lb, parent_frame=toggle_menu_fm, page=btn7_page))
        toggle_btn7.place(x=100, y=440)

        toggle_btn7_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
        toggle_btn7_indicator_lb.place(x=105, y=480, width=80, height=2)

        canvas7 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas7.pack()
        canvas7.create_line(0, 0, 300, 0, fill='gray')

        # 관리자 전용 기능을 추가합니다. 사용자가 관리자일 경우에만 보입니다.
        if LoginController.is_admin:
            canvas8 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
            canvas8.place(x=0, y=390)
            canvas8.create_line(0, 0, 300, 0, fill='gray')

            toggle_btn8 = tk.Button(toggle_menu_fm, text='관리자 전용 기능', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda:switch(indicator_lb=toggle_btn7_indicator_lb, parent_frame=toggle_menu_fm, page=admin_function))
            toggle_btn8.place(x=100, y=400)

        window_height = 700
        menu_width = 300
        
        window_width = root.winfo_width()

        x_position = window_width - menu_width

        toggle_menu_fm.place(x=x_position, y=50, height=window_height, width=menu_width)

        toggle_btn.config(text='≡', font=('Bold, 40'))
        toggle_btn.config(command=collapse_toggle_menu)
    else:
        messagebox.showwarning("로그인", "로그인하세요")

head_frame = tk.Frame(root, bg='#838383', 
                      highlightbackground='white', highlightthickness=1)
head_frame.pack(side=tk.TOP, fill=tk.X)

toggle_btn = tk.Button(head_frame, text='≡', bg='#838383', fg='black', font=('Bold, 40'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=toggle_menu)
toggle_btn.pack(side=tk.RIGHT)

def gear_btn_click():
    if LoginController.is_admin:
        messagebox.showinfo("정보", "관리자 입니다.")
    else:
        messagebox.showerror("정보", "사용자 입니다.")

gear_btn=tk.Button(head_frame, text='⚙', bg='#838383', fg='black', font=('Bold, 30'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=gear_btn_click)
gear_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame, text='MAIN', bg='#838383', fg='black', font=('Helvetica', 15, 'bold'), bd=0)

title_lb.pack(side='left', padx=5)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

def btn1_page(): # 단어장 조회
    btn4_fm = tk.Frame(main_fm)
    btn4_fm.pack(fill=tk.BOTH, expand=True)
    dictionarymaincontroller = pb.DictionaryMainController(btn4_fm,main_fm,pb.partmodel,speakword)
    dictionarymaincontroller.init()


def btn2_page(): # 단어 테스트 조회
    import testPage as tp

    btn3_fm=tk.Frame(main_fm)
    btn3_fm.pack(fill=tk.BOTH, expand=True)
    testPageController = tp.TestController(btn3_fm)

def btn3_page(): # 오답노트 조회
    from answer_note import AnswerNoteController

    btn2_fm = tk.Frame(main_fm)
    btn2_fm.pack(fill=tk.BOTH,expand=True)
    answernotecontroller = AnswerNoteController(btn2_fm,pb.partmodel,speakword)
    answernotecontroller.part_event()


def btn4_page(): # 토익 날짜 조회
    from exam_schedule_seyeon import TOEICScheduleController
    btn4_fm = tk.Frame(main_fm)
    btn4_fm.pack(fill=tk.BOTH, expand=True)
    controller = TOEICScheduleController(btn4_fm)


def btn5_page(): # 토익 고사장 조회
    import exam_place_seyeon as place

    btn5_fm = tk.Frame(main_fm)
    controller = place.EtsPlaceController(btn5_fm)
    btn5_fm.pack(fill=tk.BOTH, expand=True)

def btn7_page(): # "로그아웃" 버튼
    LoginController.is_login=False
    LoginController.is_admin=False
    btn1_fm=tk.Frame(main_fm)
    btn1_fm.pack(fill=tk.BOTH, expand=True)
    controller = LoginController(btn1_fm)


# 수정 필요
def admin_function(): # "관리자 전용 기능" 버튼
    import word_management as management

    admin_fm = tk.Frame(main_fm)
    admin_fm.pack(fill=tk.BOTH, expand=True)
    adminmaincontroller = management.ManagementController(admin_fm)
    return adminmaincontroller

speakword = SpeakWord()
main_fm = tk.Canvas(root)

main_fm.pack(fill=tk.BOTH, expand=True)

# 처음 시작할 때: 로그인 창 띄우기
btn1_fm=tk.Frame(main_fm)
btn1_fm.pack(fill=tk.BOTH, expand=True)
controller = LoginController(btn1_fm)
#btn1_page()

root.mainloop()