from tkinter.ttk import Progressbar, Label
import tkinter as tk
from tkinter import ttk
from part_dict import PartDictController
from part_dict import PartDictModel
from titlebar import TitleView
from speak_word import SpeakWord
import math

# part 1 ~ n 까지 박스 생성
class PartView: # part_index는 part 몇 인지, learend_word_list는 각 part에서의 배운 단어 개수가 들어간다. part_dict,part_sentece는 한 파트에 들어갈 단어, 예문, 뜻이다.
    def __init__(self,window,frame,part_dict_model,speak_word_model,dictionary_db): 
        self.window = window
        self.frame = frame
        self.part_dict_model = part_dict_model # 각 파트의 모델(데이터 있음)
        part_controller = PartDictController(self.frame,part_dict_model,speak_word_model) # 파트 눌렀을 때 특정 파트 안의 단어를 보기 위한 클래스
        self.white_box = tk.Frame(self.frame, bg="lightgray",borderwidth=0, relief="ridge",width=600, height=140) 
        self.part_button = tk.Button(self.white_box,relief="flat",text=f"PART {part_dict_model.part_index+1}",width=11,height=2,font="Helvetica",
        command=lambda:part_controller.part_event()) #part controller에 한 파트의 단어,예문 넣었음
        self.learned_word = dictionary_db.learned_word_list[part_dict_model.part_index] # 특정 파트의 배운 단어
        self.progress_label = Label(self.white_box, text=f"학습률: {self.learned_word} / 30 [ {self.learned_word//30*100}% ]",background="white",font="Helvetica") # 학습률 출력
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
class DictionaryModel:
    def __init__(self,dictionary,sentence,learned_word_list,wrong_word_texts,learned_word_texts): #word_cnt는 단어장에 표현할 총 단어 개수, learned_word_list는 각 파트에서 배운 단어 개수
        self.learned_word_list = learned_word_list # 학습률 계산을 위한 list
        self.dictionary = dictionary # 모든 단어
        self.word_cnt = len(self.dictionary) # 모든 단어 개수
        self.sentence = sentence # 모든 예문
        self.wrong_word_texts = wrong_word_texts # 오답노트 데이터 
        self.learned_word_texts = learned_word_texts # 이미 배운 단어 데이터

# 단어장 메인 
class DictionaryMainController:
    def __init__(self,root,partmodel):
        self.root = root
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas)
        # 단어장 db 생성, 단어리스트, 예문 리스트, 배운 단어 개수, 오답노트, 배운 단어 리스트(이미 배운 단어를 가리기 위해)
        self.dictionary_db = partmodel
        self.speak_word_model = SpeakWord() # 단어 발음 구현 클래스 생성

    # 윈도우 사이즈 조정
    def setting_size(self):
        my_windows_width = self.root.winfo_screenwidth()
        my_windows_height = self.root.winfo_screenheight()
        app_width = 700
        app_height = 550
        center_width = (my_windows_width/2)-(app_width/2)
        center_height = (my_windows_height/2)-(app_height/2)
        self.root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    
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
        
    # 위 함수 전부 호출
    def init(self):
        self.setting_size()
        self.setting_canvas()
        self.setting_frame()
        self.setting_scrollbar()
        # 타이틀바 생성 -> 나중에 코드 통합되면 지워도 될듯
        #title = TitleView(self.root,"단어장")
        #title.init_title()

        for part_index in range(0,math.ceil(self.dictionary_db.word_cnt/30)): # 각 파트에 단어 30개만 있다고 가정. 
            if part_index == int(self.dictionary_db.word_cnt/30): # 마지막 케이스 일 때, 나중에 /120으로 수정 -> 마지막 케이스는 단어 개수가 딱 120개가 아니기 때문
                part_dict_model = PartDictModel(part_index,self.dictionary_db,self.dictionary_db.word_cnt % 30) # 한 파트의 모델나중에 10 -> 120으로 수정
            else:
                part_dict_model = PartDictModel(part_index,self.dictionary_db,30) # 한 파트의 모델, 나중에 10 -> 120으로 수정

            partbox = PartView(self.root,self.frame,part_dict_model,self.speak_word_model,self.dictionary_db) # part 1 ~ part n 까지 gui로 구현하기 위한 view 클래스
            partbox.init_part()
        self.root.mainloop()


"""db 관련 """
dictionary = ["apple","banana","chief","depend","eagle","fantastic","golf","high","identify","joke",
"sophisticated","quality","complete","information","consecutive","deliberation","formerly","enhance","decrease","estimate",
"impressive","reduce","beware","innate","restor","necessary","health","renovate","arise","certain",
"policy","circumscribe","prohibit","prohibition","budget","preserve","calcuate","assent","exhibit","safety",
"refuse","expend","require","contribute","competent","insurance","frquently","mandatory","retire","abuse",
"instruct","amend","garner","monetary","financial"
] 
# 나중에 db에 있는 단어장 dictionary에 넣기
word_cnt = len(dictionary) # 단어 총 개수
learned_word_list=[0 for i in range(0,math.ceil(word_cnt/30))] # range(0,파트 개수) -> list에는 각 part에서의 배운 단어 개수가 들어간다. 
sentence = dictionary # 나중에 db에 있는 예문 넣기 ! , 임시로 sentence = dictionary로 했음
wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
learned_word_texts = [] # 배운 단어 리스트 ( 파트별로 구현할 필요 x )

partmodel = DictionaryModel(dictionary,sentence,learned_word_list,wrong_word_texts,learned_word_texts)

# 다른곳에서 partbox 모듈 부를 때
# import partbox as pb
# import tkinter as tk
# root = tk.Tk()
# dictionarymaincontroller = pb.DictionaryMainController(root,pb.partmodel)
# dictionarymaincontroller.init()
