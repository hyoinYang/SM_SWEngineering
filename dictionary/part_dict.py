import tkinter as tk
from tkinter import messagebox

import random
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from wordClass import WordDBModel
from login import LoginModel

# 한 파트 단어의 db
class PartDictModel:
    def __init__(self,part_index,dictionary_db,cnt): 
        self.word_texts = [] # 흰색 프레임에 들어가는 텍스트 클래스
        self.sentence_texts = [] # 초록색 프레임에 들어가는 텍스트 클래스 ( 예문 )
        self.part_index = part_index # 파트 몇 인지
        self.word = dictionary_db.dictionary[part_index*30:part_index*30+cnt] # 이 파트에 들어가는 단어 
        self.sentence = dictionary_db.sentence[part_index*30:part_index*30+cnt] # 이 파트에 들어가는 예문
        self.random_index=list(range(0,len(self.word))) # 랜덤 함수에서 사용
        self.dictionary_db = dictionary_db # 전체 단어장 db
        
# gui 구현
class PartDictView:
    def __init__(self,i,frame,model,controller):
        self.i = i # 인덱스
        self.model = model #  각 파트의 모델 ( PartDictModel )
        self.controller = controller # 각 파트의 controller

        self.white_box = tk.Frame(frame, bg="white",borderwidth=2, relief="ridge") # 단어가 적혀있는 box
        self.green_box = tk.Frame(self.white_box, bg="white",borderwidth=0, relief="ridge") # 단어 뜻, 예문이 적혀있는 box
        self.dictionary_box = tk.Text(self.green_box, height=12,bg="lightgreen",borderwidth=0) # 단어 뜻, 예문

        self.favorites_button_image = tk.PhotoImage(file="resource/favorites_icon.png").subsample(15) # whitebox에 생성될 즐겨찾기 버튼 이미지
        self.favorites_button = tk.Button(self.white_box,image = self.favorites_button_image,
        relief="flat",command=lambda:self.controller.favorites_button_click(self.favorites_button,self.i)) # 즐겨찾기 버튼 생성

        self.sound_button_image = tk.PhotoImage(file="resource/sound_icon.png").subsample(15) # whitebox에 생성될 단어 발음 듣기 버튼 이미지
        self.sound_button = tk.Button(self.white_box,image = self.sound_button_image, 
        relief="flat",command=lambda:controller.sound_button_click(self.sound_button,self.i)) # 단어 발음 듣기 버튼 생성

        self.dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2) # whitebox에 생성될 greenbox 열기 버튼 이미지
        self.dic_button = tk.Button(self.white_box,image = self.dic_button_image,relief="flat",
        command=lambda:self.controller.open_green_box(self.dictionary_box,self.dic_button,self.green_box)) # greenbox 여는 버튼 생성

        self.check_button_image = check_button_image = tk.PhotoImage(file="resource/check_icon.png").subsample(15) # whitebox에 생성될 학습 완료 버튼
        self.check_button = tk.Button(self.white_box,image = check_button_image, relief="flat",
        command=lambda:self.controller.check_button_click(self.check_button,self.i)) # 학습한 단어 버튼 생성

        self.text_box = tk.Text(self.white_box, fg="black", wrap="word", height=4, padx=20, pady=20, borderwidth=0) # 스크롤 가능한 박스 생성

        self.random_button = tk.Button(frame,bg="white",text="랜덤",font=("Helvetica", 15),
        command=lambda:self.controller.random_button_click(self.random_button,model.word,model.sentence)) # 랜덤 버튼 생성
        self.sequence_button = tk.Button(frame,bg="white",text="순행",font=("Helvetica", 15),
        command=lambda:self.controller.sequence_button_click(self.sequence_button,model.word,model.sentence)) # 순행 버튼 생성
    
    # whitebox (단어, 버튼이 있는 box) 위치 설정
    def setting_white_box(self):
        self.white_box.pack(pady=10,fill="x")

    # greenbox(단어 뜻, 예문 있는 box) 위치 설정
    def setting_green_box(self):
        self.green_box.pack(side="bottom",fill="x")
    
    # greenbox에 예문 설정
    def setting_dictionary_box(self):
        self.dictionary_box.insert("end", self.model.sentence[self.i])
        self.dictionary_box.config(state="disabled")
        self.model.sentence_texts.append(self.dictionary_box)

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
        self.text_box.insert(tk.END, self.model.word[self.i])
        self.text_box.config(state="disabled")
        self.text_box.pack(side="top", fill="both", expand=True)
        self.model.word_texts.append(self.text_box)

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

    # 순행 버튼 설정
    def setting_random_button(self):
        self.random_button.pack(side="top",anchor="center")

# partbox.py에서 part 눌렀을 때 이벤트 처리, 
class PartDictController: 
    def __init__(self,root,model,speak_model):
        self.root = root
        self.model = model # partdictmodel이 있어야 함 -> 각 파트마다 존재, 각 파트에 필요한 데이터 들어있음
        self.speak_model = speak_model

    def part_event(self): # word, sentence가 이 파트에서 출력할 단어, 예문 리스트
        for widget in self.root.winfo_children():
            if str(type(widget)) == "<class 'tkinter.Scrollbar'>":
                continue
            widget.destroy()
        
        for i in range(0,len(self.model.word)):
            partdict = PartDictView(i,self.root,self.model,self)
            if i == 0: # 처음에 랜덤 버튼 생성
                partdict.setting_random_button()
            partdict.init_part_dict() # gui 구현

    # 단어장에서 초록 박스를 버튼으로 여는 함수
    def open_green_box(self,dictionary_box,dic_button,green_box):
        dictionary_box.pack(fill="both", expand=True)
        dic_button_image = tk.PhotoImage(file="resource/button_6.png").subsample(2,2)
        dic_button.config(
            command=lambda:self.close_green_box(dictionary_box,dic_button,green_box),
            image=dic_button_image
        )
        dic_button.image = dic_button_image
        
    # 단어장에서 초록 박스를 버튼으로 닫는 함수
    def close_green_box(self,dictionary_box,dic_button,green_box):
        dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2)
        dic_button.config(
            command=lambda:self.open_green_box(dictionary_box,dic_button,green_box),
            image=dic_button_image
        )
        dic_button.image = dic_button_image
        dictionary_box.pack_forget()
        green_box.config(height=1)
        
    # 단어장에서 랜덤 버튼 클릭
    def random_button_click(self,sequence_button,word,sentence): # dic_list는 한 파트에 들어갈 단어
        random.shuffle(self.model.random_index)
        for new_text,new_sentence,i in zip(self.model.word_texts,self.model.sentence_texts,self.model.random_index):
            new_text.config(state=tk.NORMAL)
            new_sentence.config(state=tk.NORMAL)
            new_text.delete("1.0",tk.END)
            new_sentence.delete("1.0",tk.END)
            new_text.insert(tk.END,word[self.model.random_index[i]])
            new_sentence.insert(tk.END,sentence[self.model.random_index[i]])
            sequence_button.config(text="순행",command=lambda:self.sequence_button_click(sequence_button,word,sentence))

    # 단어장에서 순행 버튼 클릭
    def sequence_button_click(self,sequence_button,word,sentence):
        index = list(range(0,10))
        for new_text,new_sentence,i in zip(self.model.word_texts,self.model.sentence_texts,index):
            new_text.config(state=tk.NORMAL)
            new_sentence.config(state=tk.NORMAL)
            new_text.delete("1.0",tk.END)
            new_sentence.delete("1.0",tk.END)
            new_text.insert(tk.END,word[i])
            new_sentence.insert(tk.END,sentence[i])

        sequence_button.config(text="랜덤",command=lambda:self.random_button_click(sequence_button,word,sentence))

    # 단어 발음 버튼
    def sound_button_click(self,sound_button,i):
        sound_button.config(bg="red")
        sound_button.after(1000,lambda:sound_button.config(bg="SystemButtonFace"))
        word = self.model.word_texts[i].get("1.0",tk.END).replace("\n","")
        self.speak_model.init_speak(word)

    # 즐겨찾기 버튼 
    def favorites_button_click(self,favorites_button,word_index):
        WordDB = WordDBModel()
        Login = LoginModel()
        username = Login.current_user
        favorites_button.config(bg="yellow")
        favorites_button.after(1000,lambda:favorites_button.config(bg="SystemButtonFace"))
        word = self.model.word_texts[word_index].get("1.0",tk.END).replace("\n","")
        #sentence = self.model.sentence_texts[word_index].get("1.0",tk.END)
        self.model.dictionary_db.wrong_word_texts
        if word in self.model.dictionary_db.wrong_word_texts: # 중복 처리가 안 됨...
            messagebox.showinfo("단어장",f"{word}는 이미 즐겨찾기 목록에 있습니다 !")
            return
        # ### mysql 디비추가함
        WordDB.add_bookmark_by_userName(username, word)


        # self.model.dictionary_db.wrong_word_texts.append(word)
        # self.model.dictionary_db.wrong_sentence.append(sentence)

        # print(f"오답노트에 {word},{sentence}가 추가되었습니다.")

    # 학습률 버튼
    def check_button_click(self,check_button,word_index):
        check_button.config(bg="yellow")
        check_button.after(1000,lambda:check_button.config(bg="SystemButtonFace"))
        word = self.model.word_texts[word_index].get("1.0",tk.END).replace("\n","") # 학습률 버튼을 누른 단어 가져오기
        if word in self.model.dictionary_db.learned_word_texts: # 이미 배운 단어인지 확인
            messagebox.showinfo("단어장",f"{word}는 이미 학습한 단어 입니다 !")
            return
        self.model.dictionary_db.learned_word_list[self.model.part_index]+=1 # 특정 파트에 배운 단어 개수 추가
        self.model.dictionary_db.learned_word_texts.append(word) # 배운 단어라고 기억하기