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

title_lb = tk.Label(head_frame, text='MAIN', bg='#838383', fg='black', font=('Helvetica', 15, 'bold'), bd=0)

title_lb.pack(side='left', padx=5)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

def btn1_page():
    """class PartView:
        def __init__(self, window, frame, part_dict_model, speak_word_model, dictionary_db):
            self.window = window
            self.frame = frame
            self.part_dict_model = part_dict_model
            part_controller = PartDictController(self.frame, part_dict_model, speak_word_model)
            self.white_box = tk.Frame(self.frame, bg="lightgray", borderwidth=0, relief="ridge", width=600, height=140)
            self.part_button = tk.Button(self.white_box, relief="flat", text=f"PART {part_dict_model.part_index+1}", width=11, height=2, font="Helvetica",
                                          command=lambda: part_controller.part_event())
            self.learned_word = dictionary_db.learned_word_list[part_dict_model.part_index]
            self.progress_label = Label(self.white_box, text=f"학습률: {self.learned_word} / 30 [ {self.learned_word//30*100}% ]", background="white", font="Helvetica")
            self.progress_bar = Progressbar(self.white_box, orient="horizontal", mode="determinate", length=300)

        def setting_white_box(self):
            self.white_box.pack_propagate(False)
            self.white_box.pack(pady=10, fill="x")

        def setting_part_button(self):
            self.part_button.pack(side="top", anchor="nw", padx=10, pady=10)

        def setting_learned_word(self):
            self.progress_label.place(relx=0.55, rely=0.73)

        def setting_progress_bar(self):
            self.progress_bar['value'] = self.learned_word // 120 * 100
            self.progress_bar.pack(side="bottom", anchor="sw", padx=10, pady=15)

        def init_part(self):
            self.setting_white_box()
            self.setting_part_button()
            self.setting_learned_word()
            self.setting_progress_bar()

    class DictionaryModel:
        def __init__(self, dictionary, sentence, learned_word_list, wrong_word_texts, learned_word_texts):
            self.learned_word_list = learned_word_list
            self.dictionary = dictionary
            self.word_cnt = len(self.dictionary)
            self.sentence = sentence
            self.wrong_word_texts = wrong_word_texts
            self.learned_word_texts = learned_word_texts

    class DictionaryMainController:
        def __init__(self, root, partmodel):
            self.root = root
            self.canvas = tk.Canvas(self.root)
            self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
            self.frame = tk.Frame(self.canvas)
            self.dictionary_db = partmodel
            self.speak_word_model = SpeakWord()

        def setting_size(self):
            my_windows_width = self.root.winfo_screenwidth()
            my_windows_height = self.root.winfo_screenheight()
            app_width = 700
            app_height = 550
            center_width = (my_windows_width/2)-(app_width/2)
            center_height = (my_windows_height/2)-(app_height/2)
            self.root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")

        def setting_canvas(self):
            self.canvas.pack(side="left", fill="both", expand=True)
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.canvas.create_window((30, 0), window=self.frame, anchor="nw")

        def setting_scrollbar(self):
            self.scrollbar.pack(side="right", fill="y")

        def setting_frame(self):
            self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        def init(self):
            self.setting_size()
            self.setting_canvas()
            self.setting_frame()
            self.setting_scrollbar()

            for part_index in range(0, math.ceil(self.dictionary_db.word_cnt / 30)):
                if part_index == int(self.dictionary_db.word_cnt / 30):
                    part_dict_model = PartDictModel(part_index, self.dictionary_db, self.dictionary_db.word_cnt % 30)
                else:
                    part_dict_model = PartDictModel(part_index, self.dictionary_db, 30)

                partbox = PartView(self.root, self.frame, part_dict_model, self.speak_word_model, self.dictionary_db)
                partbox.init_part()
            self.root.mainloop()

    dictionary = ["apple", "banana", "chief", "depend", "eagle", "fantastic", "golf", "high", "identify", "joke",
                  "sophisticated", "quality", "complete", "information", "consecutive", "deliberation", "formerly",
                  "enhance", "decrease", "estimate", "impressive", "reduce", "beware", "innate", "restor", "necessary",
                  "health", "renovate", "arise", "certain", "policy", "circumscribe", "prohibit", "prohibition", "budget",
                  "preserve", "calcuate", "assent", "exhibit", "safety", "refuse", "expend", "require", "contribute",
                  "competent", "insurance", "frquently", "mandatory", "retire", "abuse", "instruct", "amend", "garner",
                  "monetary", "financial"]
    word_cnt = len(dictionary)
    learned_word_list = [0 for i in range(0, math.ceil(word_cnt / 30))]
    sentence = dictionary
    wrong_word_texts = []
    learned_word_texts = []

    partmodel = DictionaryModel(dictionary, sentence, learned_word_list, wrong_word_texts, learned_word_texts)

    class PartDictModel:
        def __init__(self, part_index, dictionary_db, cnt):
            self.part_index = part_index
            self.dictionary_db = dictionary_db
            self.word_count = cnt
            self.word_texts = []
            self.sentence_texts = []
            self.word = dictionary_db.dictionary[part_index * 30:part_index * 30 + cnt]
            self.sentence = dictionary_db.sentence[part_index * 30:part_index * 30 + cnt]
            self.random_index = list(range(0, len(self.word)))

    class PartDictView:
        def __init__(self, i, frame, model, controller):
            self.i = i
            self.model = model
            self.controller = controller

            self.white_box = tk.Frame(frame, bg="white", borderwidth=2, relief="ridge")
            self.green_box = tk.Frame(self.white_box, bg="white", borderwidth=0, relief="ridge")
            self.dictionary_box = tk.Text(self.green_box, height=12, bg="lightgreen", borderwidth=0)

            self.random_button = tk.Button(frame, bg="white", text="랜덤", font=("Helvetica", 15),
                                            command=lambda: self.controller.random_button_click(self.model.word, self.model.sentence))

        def setting_white_box(self):
            self.white_box.pack(pady=10, fill="x")

        def setting_green_box(self):
            self.green_box.pack(side="bottom",fill="x")
        
        def setting_dictionary_box(self):
            self.dictionary_box.insert("end", self.model.sentence[self.i])
            self.dictionary_box.config(state="disabled")
            self.model.sentence_texts.append(self.dictionary_box)

        def setting_random_button(self):
            self.random_button.pack(side="top", anchor="center")

        def init_part_dict(self):
            self.setting_white_box()
            self.setting_green_box()
            self.setting_dictionary_box()
            self.setting_random_button()

    class PartDictController:
        def __init__(self, root, model, speak_model):
            self.root = root
            self.model = model
            self.speak_model = speak_model

        def part_event(self):
            for widget in self.root.winfo_children():
                widget.destroy()
            
            for i in range(len(self.model.word)):
                partdict = PartDictView(i, self.root, self.model, self)
                if i == 0:
                    partdict.setting_random_button()
                partdict.init_part_dict()

        def random_button_click(self, word, sentence):
            random.shuffle(self.model.random_index)
            for new_text, new_sentence, i in zip(self.model.word_texts, self.model.sentence_texts, self.model.random_index):
                new_text.config(state=tk.NORMAL)
                new_sentence.config(state=tk.NORMAL)
                new_text.delete("1.0", tk.END)
                new_sentence.delete("1.0", tk.END)
                new_text.insert(tk.END, word[self.model.random_index[i]])
                new_sentence.insert(tk.END, sentence[self.model.random_index[i]])

    # ----------------------------- Model -----------------------------
    class LoginModel:
        def validate_login(self, username, password):
            if username == "admin" and password == "12345":
                messagebox.showinfo("로그인", "%s님 환영합니다" % username)
                return True
            else:
                messagebox.showinfo("로그인", "누구세요?")
                return False
        
        def validate_signup(self, root):
            messagebox.showinfo("회원가입", "회원가입 창으로 이동합니다")

            for widget in root.winfo_children():
                widget.destroy()

            SignupController(root)


    # ----------------------------- View -----------------------------
    class LoginView:
        def __init__(self, root):
            self.root = root
            self.setup_ui()

        def setup_ui(self):
            #title = TitleView(self.root, "로그인")
            #title.init_title()

            # 사용자 이름 라벨 및 텍스트 상자
            username_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
            username_frame.pack(pady = 10)

            username_icon = tk.PhotoImage(file="resource/username_entry.png").subsample(10)
            self.username_label = tk.Label(username_frame, image=username_icon, relief="solid", bd=0, cursor="hand2")
            self.username_label.image = username_icon
            self.username_label.pack(side="left", padx=5)
            
            self.username_entry = tk.Entry(username_frame, relief="flat", bg="#F0F0F0")
            self.username_entry.pack(side="left", padx=5)
            self.username_entry.insert(0, "Username")

            # 비밀번호 라벨 및 텍스트 상자
            password_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
            password_frame.pack(pady=10)

            password_icon = tk.PhotoImage(file="resource/password_entry.png").subsample(37)
            self.password_label = tk.Label(password_frame, image=password_icon, relief="flat", bd=0)
            self.password_label.image = password_icon
            self.password_label.pack(side="left", padx=5)
            self.password_entry = tk.Entry(password_frame, relief="flat", bg="#F0F0F0")
            self.password_entry.pack(side="left", padx=5)
            self.password_entry.insert(0, "password")

            # 로그인 버튼
            login_icon = tk.PhotoImage(file="resource/login_btn.png").subsample(2)
            login_button = tk.Button(self.root, image=login_icon, relief="flat", bd=0, command=lambda:LoginModel.validate_login(self, "testid", "testpass"), cursor="hand2")
            login_button.image = login_icon
    
            login_button.pack(pady=20)

            # 회원가입 버튼
            signup_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
            signup_button = tk.Button(self.root, image=signup_icon, relief="flat", bd=0, command=lambda:LoginModel.validate_signup(self, self.root), cursor="hand2")
            signup_button.image = signup_icon

            signup_button.pack(pady=10)

        def get_username(self):
            return self.username_entry.get()

        def get_password(self):
            return self.password_entry.get()

        def show_login_success_message(self, username):
            messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))

        def show_login_failure_message(self):
            messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

    # ----------------------------- Controller -----------------------------
    class LoginController:
        def __init__(self, root):
            self.model = LoginModel()
            self.view = LoginView(root)
            #self.bind_events()

        def validate_login(self):
            username = self.view.get_username()
            password = self.view.get_password()
            if self.model.validate_login(username, password):
                self.view.show_login_success_message(username)
            else:
                self.view.show_login_failure_message()
        
        def handle_btn1_click(root):
            pass



    btn1_fm=tk.Frame(main_fm)
    btn1_fm.pack(fill=tk.BOTH, expand=True)
    controller = LoginController(btn1_fm)
"""


def btn2_page():
    btn4_fm = tk.Frame(main_fm)
    btn4_fm.pack(fill=tk.BOTH, expand=True)
    dictionarymaincontroller = pb.DictionaryMainController(btn4_fm,pb.partmodel)
    dictionarymaincontroller.init()

def btn3_page():
    btn3_fm=tk.Frame(main_fm)

    btn3_lb=tk.Label(btn3_fm, text='btn3', font='Helvetica, 40', fg='black')

    btn3_lb.pack(pady=80)

    btn3_fm.pack(fill=tk.BOTH, expand=True)

def btn4_page():
    class ExamModel:
        def __init__(self):
            self.ExamDBModel = ExamDBModel()
            self.exam_info =  self.ExamDBModel.get_exam_info()

        def get_exam_info(self):
            return self.exam_info

    class ExamView:
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


def btn5_page():
    btn5_fm = tk.Frame(main_fm)

    # ----------------------------- Model -----------------------------
    class EtsPlaceModel:
        
        ets_icon_path = "resource/ets.png"
        member_login_icon_path = "resource/member_login_icon.png"
        non_member_login_icon_path = "resource/non_member_login_icon.png"

        def __init__(self):
            self.urls = {
                "exam_place": "https://m.exam.toeic.co.kr/receipt/centerMap.php",
                "member_login": "https://www.ybmnet.co.kr/common/login.asp?url=%2Fcommon%2FcertifyResponse.php%3FreturnUrl%3D%2Freceipt%2FconfirmList.php&what=m.exam.toeic.co.kr",
                "non_member_login": "https://certify.ybmnet.co.kr/common/certiModuleExam/certify_step1.asp?returnUrl=https%3A%2F%2Fm.exam.toeic.co.kr%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php&loginWhat=m.exam.toeic.co.kr&loginUrl=%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php"
            }

    # ----------------------------- View -----------------------------
    class EtsPlaceView:
        def __init__(self, root):
            self.root = root
            self.setup_gui()
        
        def setup_gui(self):
            self.ets_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.ets_icon_path))
            self.member_login_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.member_login_icon_path))
            self.non_member_login_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.non_member_login_icon_path))

            self.ets_button = tk.Button(self.root, image=self.ets_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
            self.ets_button.pack(pady=(20, 0))

            self.ets_label = tk.Label(self.root, text="[ 고사장 조회 ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
            self.ets_label.pack(pady=(0, 30))

            self.member_login_button = tk.Button(self.root, image=self.member_login_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
            self.member_login_button.pack()

            self.member_login_label = tk.Label(self.root, text="[ 회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
            self.member_login_label.pack(pady=(0, 30))

            self.non_member_login_button = tk.Button(self.root, image=self.non_member_login_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
            self.non_member_login_button.pack()

            self.non_member_login_label = tk.Label(self.root, text="[ 비회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
            self.non_member_login_label.pack()

    # ----------------------------- Controller -----------------------------
    class EtsPlaceController:
        def __init__(self, root):
            self.model = EtsPlaceModel()
            self.view = EtsPlaceView(root)
            self.bind_events()
        
        def bind_events(self):
            self.view.ets_button.config(command=self.open_link)
            self.view.member_login_button.config(command=self.open_member_login_link)
            self.view.non_member_login_button.config(command=self.open_non_member_login_link)
        
        def open_link(self):
            webbrowser.open(self.model.urls["exam_place"])
        
        def open_member_login_link(self):
            webbrowser.open(self.model.urls["member_login"])
        
        def open_non_member_login_link(self):
            webbrowser.open(self.model.urls["non_member_login"])

    # Create an instance of the controller to link the model and the view
    controller = EtsPlaceController(btn5_fm)


    btn5_fm.pack(fill=tk.BOTH, expand=True)


def btn6_page():
    btn6_fm=tk.Frame(main_fm)

    btn6_lb=tk.Label(btn6_fm, text='btn6', font='Helvetica, 40', fg='black')

    btn6_lb.pack(pady=80)

    btn6_fm.pack(fill=tk.BOTH, expand=True)

# 수정 필요
def btn7_page():
    from login import LoginController
    return lambda test:LoginController(root)

# 수정 필요
def admin_function(root):
    from word_management import ManagementController
    ManagementController(root)

main_fm = tk.Canvas(root)

main_fm.pack(fill=tk.BOTH, expand=True)

btn1_page()

root.mainloop()