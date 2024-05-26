from titlebar import TitleView
from partbox import PartModel
from partbox import PartView
from part_dict import PartDictModel
from speak_word import SpeakWord

import tkinter as tk
import math

root = tk.Tk() # 윈도우 생성
#화면 크키 조정
my_windows_width = root.winfo_screenwidth()
my_windows_height = root.winfo_screenheight()
app_width = 700
app_height = 550
center_width = (my_windows_width/2)-(app_width/2)
center_height = (my_windows_height/2)-(app_height/2)
root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")

dictionary = ["apple","banana","chief","depend","eagle","fantastic","golf","high","identify","joke",
"sophisticated","quality","complete","information","consecutive","deliberation","formerly","enhance","decrease","estimate",
"impressive","reduce","beware","innate","restor","necessary","health","renovate","arise","certain",
"policy","circumscribe","prohibit","prohibition","budget","preserve","calcuate","assent","exhibit","safety",
"refuse","expend","require","contribute","competent","insurance","frquently","mandatory","retire","abuse",
"instruct","amend","garner","monetary","financial"
] # 나중에 db에 있는 단어장 dictionary에 넣기

word_cnt = len(dictionary) # 단어 총 개수
learned_word_list=list(range(0,math.ceil(word_cnt/30))) # range(0,파트 개수) -> list에는 각 part에서의 배운 단어 개수가 들어간다. 
sentence = dictionary # 나중에 db에 있는 예문 넣기 ! , 임시로 sentence = dictionary로 했음
wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
learned_word_texts = [] # 배운 단어 리스트 ( 파트별로 구현할 필요 x )

# 타이틀바 생성
title = TitleView(root)
title.init_title()

# 단어장 db 생성 
dictionary_db = PartModel(dictionary,sentence,learned_word_list,wrong_word_texts,learned_word_texts) # 단어리스트, 예문 리스트, 배운 단어 개수, 오답노트, 배운 단어 리스트(이미 배운 단어를 가리기 위해)

# 단어 발음 구현 클래스 생성
speak_word_model = SpeakWord()

# 단어장 GUI 생성
for part_index in range(0,math.ceil(dictionary_db.word_cnt/30)): # 각 파트에 단어 10개만 있다고 가정. 나중에 /120으로 수정
    if part_index == int(dictionary_db.word_cnt/30): # 마지막 케이스 일 때, 나중에 /120으로 수정 -> 마지막 케이스는 단어 개수가 딱 120개가 아니기 때문
        part_dict_model = PartDictModel(part_index,dictionary_db,dictionary_db.word_cnt % 10) # 한 파트의 모델나중에 10 -> 120으로 수정
    else:
        part_dict_model = PartDictModel(part_index,dictionary_db,30) # 한 파트의 모델, 나중에 10 -> 120으로 수정

    partbox = PartView(root,title.frame,part_dict_model,speak_word_model,dictionary_db) # part 1 ~ part n 까지 gui로 구현하기 위한 view 클래스
    partbox.init_part()

root.mainloop()