import tkinter as tk
from tkinter import ttk
import random


# 각 파트 단어의 db
class PartDictModel:
    def __init__(self):
        self.wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
        self.random_index=list(range(0,10)) # 랜덤 함수에서 사용, 임시로 단어 10개라고 설정했기 때문에 range(0,10)으로 설정함 
        self.learned_word = 0 # 이 파트에서 배운 단어 개수 
        self.learning_rate = 0.0 # 이 파트에서 배운 단어 학습률

# gui 구현
class PartDictView:
    def __init__(self,frame,word,sentence):
        self.white_box = tk.Frame(frame, bg="white",borderwidth=2, relief="ridge") # 단어가 적혀있는 box
        self.green_box = tk.Frame(self.white_box, bg="white",borderwidth=0, relief="ridge") # 단어 뜻, 예문이 적혀있는 box
        self.dictionary_box = tk.Text(self.green_box, height=12,bg="lightgreen",borderwidth=0) # 단어 뜻, 예문
        self.favorites_button_image = tk.PhotoImage(file="resource/favorites_icon.png").subsample(15) # whitebox에 생성될 즐겨찾기 버튼
        self.favorites_button = tk.Button(self.white_box,image = self.favorites_button_image,
        relief="flat",command=lambda:print("favorties")) # 나중에 오답노트로 저장하는 모듈로 바꿔주기, favorites_button_click(favorites_button,word_index)
        self.sound_button_image = tk.PhotoImage(file="resource/sound_icon.png").subsample(15) # whitebox에 생성될 단어 발음 듣기 버튼
        self.sound_button = tk.Button(self.white_box,image = self.sound_button_image, 
        relief="flat",command=lambda:print("sound")) # 나중에 음성 모듈로 바꿔주기
        self.dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2) # whitebox에 생성될 greenbox 열기 버튼
        self.dic_button = tk.Button(self.white_box,image = self.dic_button_image,relief="flat",
        command=lambda:print("green box")) # open_green_box(self.white_box,self.green_box,self.dictionary_box,dic_button,text)
        self.check_button_image = check_button_image = tk.PhotoImage(file="resource/check_icon.png").subsample(15) # whitebox에 생성될 학습 완료 버튼
        self.check_button = tk.Button(self.white_box,image = check_button_image, relief="flat",command=lambda:print("check")) # check_button_click(check_button)
        self.text_box = tk.Text(self.white_box, fg="black", wrap="word", height=4, padx=20, pady=20, borderwidth=0) # 스크롤 가능한 박스 생성
        self.word = word # 프레임에 들어가는 텍스트 클래스 ( 단어 )
        self.sentence = sentence # 초록색 프레임에 들어가는 텍스트 클래스 ( 예문 )

    # whitebox (단어, 버튼이 있는 box) 위치 설정
    def setting_white_box(self):
        self.white_box.pack(pady=10,fill="x")

    # greenbox(단어 뜻, 예문 있는 box) 위치 설정
    def setting_green_box(self):
        self.green_box.pack(side="bottom",fill="x")
    
    # greenbox에 예문 설정
    def setting_dictionary_box(self):
        self.dictionary_box.insert("end", self.sentence)
        self.dictionary_box.config(state="disabled")
        #sentence_texts.append(self.dictionary_box)

    # 즐겨찾기 버튼 위치 설정
    def setting_favorites_button(self):
        self.favorites_button.image = self.favorites_button_image
        self.favorites_button.pack(anchor = "e")

    # 단어 발음 버튼 위치 설정
    def setting_sound_button(self):
        self.sound_button.image = self.sound_button_image
        self.sound_button.pack(anchor="e",pady = 0)

    # 뜻 여는 버튼 생성
    def setting_dic_button(self):
        self.dic_button.image = self.dic_button_image
        self.dic_button.pack(side="right",anchor="s")

    # 체크 버튼 생성
    def setting_check_button(self):
        self.check_button.image = self.check_button_image
        self.check_button.place(relx=0.0, rely = 0.0)

    # 스크롤 가능한 텍스트 박스 생성
    def setting_scrollbar(self):
        self.text_box.insert(tk.END, self.word)
        self.text_box.config(state="disabled")
        self.text_box.pack(side="top", fill="both", expand=True)
        #self.word_texts.append(self.text_box)

    # 위 함수 전부 실행
    def init_part_dict(self):
        self.setting_white_box()
        self.setting_green_box()
        self.setting_dictionary_box()
        self.setting_favorites_button()
        self.setting_sound_button()
        self.setting_dic_button()
        self.setting_check_button()
        self.setting_scrollbar()

