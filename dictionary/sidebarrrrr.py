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

# 사용자가 관리자인지 여부를 저장하는 변수
is_admin = True

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)

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

    toggle_btn6 = tk.Button(toggle_menu_fm, text='-', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn6_indicator_lb, parent_frame=toggle_menu_fm, page=btn6_page))
    toggle_btn6.pack(anchor='center')

    toggle_btn6_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn6_indicator_lb.place(x=110, y=233, width=80, height=2)

    canvas6 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas6.place(x=0, y=440)
    canvas6.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn7 = tk.Button(toggle_menu_fm, text='로그아웃', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn7_indicator_lb, parent_frame=toggle_menu_fm, page=btn7_page(root)))
    toggle_btn7.place(x=100, y=440)

    toggle_btn7_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn7_indicator_lb.place(x=105, y=480, width=80, height=2)

    canvas7 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas7.pack()
    canvas7.create_line(0, 0, 300, 0, fill='gray')

    # 관리자 전용 기능을 추가합니다. 사용자가 관리자일 경우에만 보입니다.
    if is_admin:
        canvas8 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas8.place(x=0, y=390)
        canvas8.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn8 = tk.Button(toggle_menu_fm, text='관리자 전용 기능', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda:admin_function(root))
        toggle_btn8.place(x=100, y=400)

    window_height = 700
    menu_width = 300
    
    window_width = root.winfo_width()

    x_position = window_width - menu_width

    toggle_menu_fm.place(x=x_position, y=50, height=window_height, width=menu_width)

    toggle_btn.config(text='≡', font=('Bold, 40'))
    toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg='#838383', 
                      highlightbackground='white', highlightthickness=1)
head_frame.pack(side=tk.TOP, fill=tk.X)

toggle_btn = tk.Button(head_frame, text='≡', bg='#838383', fg='black', font=('Bold, 40'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=toggle_menu)
toggle_btn.pack(side=tk.RIGHT)

def gear_btn_click():
    if is_admin:
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

def btn1_page():
    from part_dict import PartDictController
    from part_dict import PartDictModel
    import partbox as pb

    btn4_fm = tk.Frame(main_fm)
    btn4_fm.pack(fill=tk.BOTH, expand=True)
    dictionarymaincontroller = pb.DictionaryMainController(btn4_fm,pb.partmodel,speakword)
    dictionarymaincontroller.init()


def btn2_page():
    import testPage as tp

    btn3_fm=tk.Frame(main_fm)
    btn3_fm.pack(fill=tk.BOTH, expand=True)
    testPageController = tp.TestController(btn3_fm)

def btn3_page():
    pass

##########################################################################
def btn4_page():
    import exam_schedule_seyeon as schedule
    class ExamModel:
        def __init__(self):
            self.ExamDBModel = ExamDBModel()
            self.exam_info =  self.ExamDBModel.get_exam_info()

        def get_exam_info(self):
            return self.exam_info

    class ExamView:
        import exam_schedule_seyeon as schedule
        def __init__(self, frame):
            self.frame = frame
            self.frame.configure(background="#FFFFFF")

            style = ttk.Style()
            style.theme_use('clam')

            self.tree = ttk.Treeview(frame, columns=("일정", "접수기간", "성적발표"), show="headings")
            self.tree.heading("일정", text="일정")
            self.tree.heading("접수기간", text="접수기간")
            self.tree.heading("성적발표", text="성적발표")

            self.tree.pack(pady=20)

            self.tree.style = ttk.Style()
            self.tree.style.configure("Treeview.Item", background="#FFFFFF")
            self.tree.style.configure("Treeview.Heading", background="#FFFFFF", foreground="#000000", font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
            self.tree.style.configure("Treeview.Separator")

            self.tree.column("일정", width=200, anchor="center")
            self.tree.column("접수기간", width=200, anchor="center")
            self.tree.column("성적발표", width=200, anchor="center")

            self.tree.style.configure("Treeview.Separator", background="#FFFFFF", foreground="#FFFFFF", thickness=0)
            style.configure("Custom.Treeview", rowheight=30)
            self.tree.configure(style="Custom.Treeview")

        def update_treeview(self, exam_info):
            self.tree.delete(*self.tree.get_children())  # 기존 내용 삭제
            self.tree.insert("", tk.END, values=("", ""))
            for info in exam_info:
                self.tree.insert("", tk.END, values=list(info.values()))
                self.tree.insert("", tk.END, values=("─" * 100, "─" * 100, "─" * 100))

    class ExamController:
        def __init__(self, root):
            self.model = ExamModel()
            self.view = ExamView(root)
            self.load_exam_info()

        def load_exam_info(self):
            exam_info = self.model.get_exam_info()
            self.view.update_treeview(exam_info)

    btn4_fm = tk.Frame(main_fm)
    btn4_fm.pack(fill=tk.BOTH, expand=True)
    controller = ExamController(btn4_fm)
##########################################################################

def btn5_page():
    import exam_place_seyeon as place

    btn5_fm = tk.Frame(main_fm)
    controller = place.EtsPlaceController(btn5_fm)
    btn5_fm.pack(fill=tk.BOTH, expand=True)


def btn6_page(): # "관리자 전용 기능" 버튼
    btn6_fm=tk.Frame(main_fm)

    btn6_lb=tk.Label(btn6_fm, text='btn6', font='Helvetica, 40', fg='black')

    btn6_lb.pack(pady=80)

    btn6_fm.pack(fill=tk.BOTH, expand=True)

def btn7_page(): # "로그 아웃" 버튼
    import login as logout

    btn1_fm=tk.Frame(main_fm)
    btn1_fm.pack(fill=tk.BOTH, expand=True)
    controller = logout.LoginController(btn1_fm)

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

btn1_page()

root.mainloop()