#1 로그아웃을 아랫단에 붙이고 싶음
#2 관리자모드로 실행하면 시험 점수 아래 이어서 나오게 하고 싶음
#3 톱니바퀴 추가해야함
#4 예시로 만든 btn1, ... , btn7을 각 파일로 이어야함
#5 뼈대만 만들어 놨다 생각하면 편함
#6 관리자 쪽 토글메뉴는 일단 보류 해놨음

import tkinter as tk
from login import LoginController
import partbox as pb

def switch(indicator_lb, parent_frame, page):
    print("switch")
    for child in parent_frame.winfo_children():
        print("child: ",child)
        if isinstance(child, tk.Label):
            child['bg']='#838383'

    indicator_lb['bg']='black'
    
    for fm in main_fm.winfo_children():
        print("반복문2")
        fm.destroy()
        root.update()

    print("page(root)")
    page(root)

# 사용자가 관리자인지 여부를 저장하는 변수
is_admin = False

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        #toggle_btn.config(text='≡')
        #toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#838383')

    toggle_btn1 = tk.Button(toggle_menu_fm, text='단어장', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn1_indicator_lb, parent_frame=toggle_menu_fm, page=btn1_page(root))) 
    toggle_btn1.pack(anchor='center')

    toggle_btn1_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn1_indicator_lb.place(x=110, y=33, width=80, height=2)

    canvas1 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas1.pack()
    canvas1.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn2 = tk.Button(toggle_menu_fm, text='단어 테스트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn2_indicator_lb, parent_frame=toggle_menu_fm, page=btn2_page()))
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

    toggle_btn5 = tk.Button(toggle_menu_fm, text='토익 고사장 안내', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn5_indicator_lb, parent_frame=toggle_menu_fm, page=btn5_page))
    toggle_btn5.pack(anchor='center')

    toggle_btn5_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn5_indicator_lb.place(x=110, y=193, width=80, height=2)

    canvas5 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas5.pack()
    canvas5.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn6 = tk.Button(toggle_menu_fm, text='시험 점수 조회', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn6_indicator_lb, parent_frame=toggle_menu_fm, page=btn6_page))
    toggle_btn6.pack(anchor='center')

    toggle_btn6_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn6_indicator_lb.place(x=110, y=233, width=80, height=2)

    canvas6 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas6.pack()
    canvas6.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn7 = tk.Button(toggle_menu_fm, text='로그아웃', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda: switch(indicator_lb=toggle_btn7_indicator_lb, parent_frame=toggle_menu_fm, page=btn7_page))
    toggle_btn7.pack(anchor='center')

    toggle_btn7_indicator_lb = tk.Label(toggle_menu_fm, bg='#838383')
    toggle_btn7_indicator_lb.place(x=110, y=273, width=80, height=2)

    canvas7 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas7.pack()
    canvas7.create_line(0, 0, 300, 0, fill='gray')

    # 관리자 전용 기능을 추가합니다. 사용자가 관리자일 경우에만 보입니다.
    if is_admin:
        canvas8 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas8.pack()
        canvas8.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn8 = tk.Button(toggle_menu_fm, text='관리자 전용 기능', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=admin_function)
        toggle_btn8.pack(anchor='center')

    window_height = 700
    menu_width = 300
    
    window_width = root.winfo_width()

    x_position = window_width - menu_width

    toggle_menu_fm.place(x=x_position, y=50, height=window_height, width=menu_width)

    toggle_btn.config(text='≡', font=('Bold, 40'))
    toggle_btn.config(command=collapse_toggle_menu)


def btn1_page(root):
    return lambda test:LoginController(root)

def btn2_page():
    dictionarymaincontroller.init()
    
def btn3_page():
    btn3_fm=tk.Frame(main_fm)

    btn3_lb=tk.Label(btn3_fm, text='btn3', font='Helvetica, 40', fg='black')

    btn3_lb.pack(pady=80)

    btn3_fm.pack(fill=tk.BOTH, expand=True)

def btn4_page():
    btn4_fm=tk.Frame(main_fm)

    btn4_lb=tk.Label(btn4_fm, text='btn4', font='Helvetica, 40', fg='black')

    btn4_lb.pack(pady=80)

    btn4_fm.pack(fill=tk.BOTH, expand=True)

def btn5_page():
    btn5_fm=tk.Frame(main_fm)

    btn5_lb=tk.Label(btn5_fm, text='btn5', font='Helvetica, 40', fg='black')

    btn5_lb.pack(pady=80)

    btn5_fm.pack(fill=tk.BOTH, expand=True)

def btn6_page():
    btn6_fm=tk.Frame(main_fm)

    btn6_lb=tk.Label(btn6_fm, text='btn6', font='Helvetica, 40', fg='black')

    btn6_lb.pack(pady=80)

    btn6_fm.pack(fill=tk.BOTH, expand=True)

def btn7_page():
    btn7_fm=tk.Frame(main_fm)

    btn7_lb=tk.Label(btn7_fm, text='btn7', font='Helvetica, 40', fg='black')

    btn7_lb.pack(pady=80)

    btn7_fm.pack(fill=tk.BOTH, expand=True)


root = tk.Tk()
canvas = tk.Canvas(root)
main_fm = tk.Frame(canvas)

root.geometry('700x550')
root.title('토익 단어장')
root.configure(background="#FFFFFF")
#dictionarymaincontroller = pb.DictionaryMainController(root,pb.partmodel)

head_frame = tk.Frame(root, bg='#838383', 
                      highlightbackground='white', highlightthickness=1)
head_frame.pack(side=tk.TOP, fill=tk.X)

toggle_btn = tk.Button(head_frame, text='≡', bg='#838383', fg='black', font=('Bold, 40'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=toggle_menu)
toggle_btn.pack(side=tk.RIGHT)

title_lb = tk.Label(head_frame, text='MAIN', bg='#838383', fg='black', font=('Helvetica', 15, 'bold'), bd=0)

title_lb.pack(side='left', padx=5)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

main_fm.pack(fill=tk.BOTH, expand=True)

btn1_page(main_fm)
root.mainloop()