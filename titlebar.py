from tkinter import ttk
import tkinter as tk

# ----------------------------- View -----------------------------
class TitleView:

    def __init__(self,window, title_name):
        self.window = window
        self.style = ttk.Style()
        self.title_bar_frame = ttk.Frame(self.window, style='TFrame', height=30)
        self.gear_icon_image = tk.PhotoImage(file="resource/gear_icon.png").subsample(10)
        self.gear_button = tk.Label(self.title_bar_frame, image=self.gear_icon_image, relief="flat", bd=0, bg='#838383') # command 추가하기
        self.text_label = tk.Label(self.title_bar_frame, text=title_name, font=("Helvetica", 15), bg='#838383')
        self.sidebar_image = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)
        self.sidebar_button = tk.Button(self.title_bar_frame, image=self.sidebar_image, relief="flat", bd=0, bg='#838383') # command 추가하기
        self.canvas = tk.Canvas(self.window)
        self.scrollbar = ttk.Scrollbar(window, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)

    # style 객체 설정
    def setting_style(self):
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#838383') # 스타일에 색상을 지정

    # title bar 위치 설정
    def setting_title_bar(self):
        self.title_bar_frame.pack(fill='x')
        self.title_bar_frame.pack(pady=10)
        
    # gear_icon ( 톱니바퀴 ) 설정
    def setting_gear_icon(self):
        self.gear_button.image = self.gear_icon_image
        self.gear_button.pack(side="left", padx=5)

    # 토익단어 글씨 들어가는 label 설정
    def setting_text_label(self):
        self.text_label.pack(side="left", padx=5)
 
    # 사이드바 버튼 설정
    def setting_sidebar(self):
        self.sidebar_button.image = self.sidebar_image
        self.sidebar_button.pack(side="right", padx=5)

    # canvas 위치 설정, 스크롤바 넣기
    def setting_canvas(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((30, 0), window=self.frame, anchor="nw")

    # scrollbar 위치 설정
    def setting_scrollbar(self):
        self.scrollbar.pack(side="right", fill="y")

    # frame 설정
    def setting_frame(self):
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    # 최종적으로 title 만들어주는 함수
    def init_title(self):
        self.setting_style()
        self.setting_title_bar()
        self.setting_gear_icon()
        self.setting_text_label()
        self.setting_sidebar()
        self.setting_canvas()
        self.setting_scrollbar()
        self.setting_frame()


# ----------------------------- Controller -----------------------------
# title바에 존재하는 톱니바퀴, 사이드바 클릭 시 이벤트 처리
class TitleController:

    def __init__(self,gear_button,sidebar_button):
        self.gear_button = gear_button
        self.sidebar_button = sidebar_button

    
    def gear_button_click(self):
        self.gear