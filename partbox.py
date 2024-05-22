from tkinter.ttk import Progressbar, Label
import tkinter as tk

# part 1 ~ n 까지 박스 생성
class PartView: # part_index는 part 몇 인지, learend_word_list는 각 part에서의 배운 단어 개수가 들어간다.
    def __init__(self,window,frame,part_index,learned_word):
        self.window = window
        self.frame = frame
        self.white_box = tk.Frame(self.frame, bg="lightgray",borderwidth=0, relief="ridge",width=600, height=140)
        self.part_button = tk.Button(self.white_box,relief="flat",text=f"PART {part_index+1}",width=11,height=2,font="Helvetica",command=lambda:print("part")) #command 나중에 바꾸기
        self.learned_word = learned_word 
        self.progress_label = Label(self.white_box, text=f"학습률: {self.learned_word} / 120 [ {self.learned_word//120*100}% ]",background="white",font="Helvetica") 
        self.progress_bar = Progressbar(self.white_box, orient="horizontal", mode="determinate",length=300)

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
    def __init__(self,word_cnt,learned_word_list): #word_cnt는 단어장에 표현할 총 단어 개수, learned_word_list는 각 파트에서 배운 단어 개수
        self.word_cnt = word_cnt
        self.learned_word_list = learned_word_list
