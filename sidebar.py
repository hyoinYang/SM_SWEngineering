import tkinter as tk

root = tk.Tk()
root.geometry('700x550')
root.title('a')
root.configure(background="#FFFFFF")


def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)
 
    toggle_menu_fm=tk.Frame(root, bg='#838383')

    toggle_btn1 = tk.Button(toggle_menu_fm, text='단어장', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn1.pack(anchor='center')

    canvas1 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas1.pack()
    canvas1.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn2 = tk.Button(toggle_menu_fm, text='단어 테스트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn2.pack(anchor='center')

    canvas2 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas2.pack()
    canvas2.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn3 = tk.Button(toggle_menu_fm, text='오답노트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn3.pack(anchor='center')

    canvas3 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas3.pack()
    canvas3.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn4 = tk.Button(toggle_menu_fm, text='토익 시험 날짜', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn4.pack(anchor='center')

    canvas4 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas4.pack()
    canvas4.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn5 = tk.Button(toggle_menu_fm, text='토익 고사장 안내', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn5.pack(anchor='center')

    canvas5 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas5.pack()
    canvas5.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn6 = tk.Button(toggle_menu_fm, text='시험 점수 조회', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn6.pack(anchor='center')

    canvas6 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas6.pack()
    canvas6.create_line(0, 0, 300, 0, fill='gray')

    #여기 공백이 들어가거나 canvas7, toggle_btn7의 위치 기준점을 아래서부터 잡아야함 (쉽지않네...) pack 내부 side를 수정하는건 맞는거 같은데 bottom으로 작성하니 아예 화면 밖으로 나가는듯함.

    canvas7 = tk.Canvas(toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
    canvas7.pack()
    canvas7.create_line(0, 0, 300, 0, fill='gray')

    toggle_btn7 = tk.Button(toggle_menu_fm, text='로그아웃', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
    toggle_btn7.pack(anchor='center')



    window_height= 700
    menu_width = 300
    
    window_width = root.winfo_width()

    x_position = window_width - menu_width

    toggle_menu_fm.place(x=x_position, y=50, height=window_height, width=menu_width)

    toggle_btn.config(text='≡', font=('Bold, 40'))
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(root, bg='#838383', 
                      highlightbackground='white', highlightthickness=1)
head_frame.pack(side=tk.TOP, fill=tk.X)

toggle_btn= tk.Button(head_frame, text='≡', bg='#838383', fg='black', font=('Bold, 40'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=toggle_menu)
toggle_btn.pack(side=tk.RIGHT)

title_lb=tk.Label(head_frame, text='토익 시험 일정', bg='#838383', fg='black', font=('Helvetica', 15, 'bold'), bd=0)

title_lb.pack(side='left',padx=5)


head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


root.mainloop()
