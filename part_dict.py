import tkinter as tk
from tkinter import ttk
import random
class PartDictView:

# 각 파트 단어의 db
class PartDictModel:
    def __init__(self):
        self.word_texts = [] # 프레임에 들어가는 텍스트 클래스 ( 단어 )
        self.sentence_texts = [] # 초록색 프레임에 들어가는 텍스트 클래스 ( 예문 )
        self.wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
        self.random_index=list(range(0,10)) # 랜덤 함수에서 사용, 임시로 단어 10개라고 설정했기 때문에 range(0,10)으로 설정함 
        self.learned_word = 0 # 이 파트에서 배운 단어 개수 
        self.learning_rate = 0.0 # 이 파트에서 배운 단어 학습률

# gui 구현
class PartDictView:
    def __init__(self,frame):
        self.white_box = tk.Frame(frame, bg="white",borderwidth=2, relief="ridge")
        self.green_box = tk.Frame(self.white_box, bg="white",borderwidth=0, relief="ridge")
        self.dictionary_box = tk.Text(self.green_box, height=12,bg="lightgreen",borderwidth=0)
        self.favorites_button_image = tk.PhotoImage(file="resource/favorites_icon.png").subsample(15)
        self.favorites_button = tk.Button(self.white_box,image = self.favorites_button_image,
        relief="flat",command=lambda:print("favorties")) # 나중에 오답노트로 저장하는 모듈로 바꿔주기, favorites_button_click(favorites_button,word_index)
        self.sound_button_image = tk.PhotoImage(file="resource/sound_icon.png").subsample(15)
        self.sound_button = tk.Button(self.white_box,image = self.sound_button_image, 
        relief="flat",command=lambda:print("sound")) # 나중에 음성 모듈로 바꿔주기
        self.dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2)
        dic_button = tk.Button(self.white_box,image = self.dic_button_image,relief="flat",
        command=lambda:open_green_box(self.white_box,self.green_box,self.dictionary_box,dic_button,text)) # open_green_box(self.white_box,self.green_box,self.dictionary_box,dic_button,text)
    def white_box_setting(self):
        self.white_box.pack(pady=10,fill="x")

    def green_box_setting(self):
        self.green_box.pack(side="bottom",fill="x")
    
    def dictionary_box_setting(self):
        self.dictionary_box.insert("end", text)
        self.dictionary_box.config(state="disabled")
        sentence_texts.append(self.dictionary_box)

    def setting_favorites_button(self):
        self.favorites_button.image = self.favorites_button_image
        self.favorites_button.pack(anchor = "e")

    def setting_sound_button(self):
        self.sound_button.image = self.sound_button_image
        self.sound_button.pack(anchor="e",pady = 0)

    # 뜻 여는 버튼 생성
    
    dic_button = tk.Button(white_box,image = dic_button_image,relief="flat",command=lambda:open_green_box(white_box,green_box,dictionary_box,dic_button,text))
    dic_button.image = dic_button_image
    dic_button.pack(side="right",anchor="s")

    # 체크 버튼 생성
    check_button_image = tk.PhotoImage(file="resource/check_icon.png").subsample(15)
    check_button = tk.Button(white_box,image = check_button_image, relief="flat",command=lambda:check_button_click(check_button))
    check_button.image = check_button_image
    check_button.place(relx=0.0, rely = 0.0)

    # 스크롤 가능한 텍스트 박스 생성
    text_box = tk.Text(white_box, fg="black", wrap="word", height=4, padx=20, pady=20, borderwidth=0)
    text_box.insert(tk.END, text)
    text_box.config(state="disabled")
    text_box.pack(side="top", fill="both", expand=True)
    word_texts.append(text_box)

