from tkinter.ttk import Progressbar, Label
import tkinter as tk
from part_dict import PartDictController

# part 1 ~ n 까지 박스 생성
class PartView: # part_index는 part 몇 인지, learend_word_list는 각 part에서의 배운 단어 개수가 들어간다. part_dict,part_sentece는 한 파트에 들어갈 단어, 예문, 뜻이다.
    def __init__(self,window,frame,part_dict_model,speak_word_model,dictionary_db): 
        self.window = window
        self.frame = frame
        self.part_dict_model = part_dict_model # 각 파트의 모델(데이터 있음)
        part_controller = PartDictController(frame,part_dict_model,speak_word_model) # 파트 눌렀을 때 특정 파트 안의 단어를 보기 위한 클래스
        self.white_box = tk.Frame(self.frame, bg="lightgray",borderwidth=0, relief="ridge",width=600, height=140) 
        self.part_button = tk.Button(self.white_box,relief="flat",text=f"PART {part_dict_model.part_index+1}",width=11,height=2,font="Helvetica",
        command=lambda:part_controller.part_event()) #part controller에 한 파트의 단어,예문 넣었음
        self.learned_word = dictionary_db.learned_word_list[part_dict_model.part_index] # 특정 파트의 배운 단어
        self.progress_label = Label(self.white_box, text=f"학습률: {self.learned_word} / 120 [ {self.learned_word//120*100}% ]",background="white",font="Helvetica") # 학습률 출력
        self.progress_bar = Progressbar(self.white_box, orient="horizontal", mode="determinate",length=300) # 학습률에 따른 게이지바

    # white_box는 part, 진행률, 학습률이 들어갈 box
    # white_box의 위치를 설정함
    def setting_white_box(self):
        self.white_box.pack_propagate(False)
        self.white_box.pack(pady=10,fill="x")

    # part_button ( ex. part 1, part 2 ...)의 위치를 설정함
    def setting_part_button(self):
        self.part_button.pack(side="top",anchor="nw", padx=10,pady=10)

    # 학습률 글씨 위치 설정
    def setting_learned_word(self):
        self.progress_label.place(relx=0.55,rely=0.73)
    
    # 학습률 상자 생성
    def setting_progress_bar(self):
        self.progress_bar['value']= self.learned_word//120*100 # 학습률 넣기
        self.progress_bar.pack(side="bottom",anchor="sw",padx=10, pady=15)
    
    # 위 함수 전부 호출
    def init_part(self):
        self.setting_white_box()
        self.setting_part_button()
        self.setting_learned_word()
        self.setting_progress_bar()

# 전체 단어 개수, 각 파트에서 배운 단어 개수 db 
class PartModel:
    def __init__(self,dictionary,sentence,learned_word_list,wrong_word_texts,learned_word_texts): #word_cnt는 단어장에 표현할 총 단어 개수, learned_word_list는 각 파트에서 배운 단어 개수
        self.learned_word_list = learned_word_list # 학습률 계산을 위한 list
        self.dictionary = dictionary # 모든 단어
        self.word_cnt = len(self.dictionary) # 모든 단어 개수
        self.sentence = sentence # 모든 예문
        self.wrong_word_texts = wrong_word_texts # 오답노트 데이터 
        self.learned_word_texts = learned_word_texts # 이미 배운 단어 데이터
