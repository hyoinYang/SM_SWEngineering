from titlebar import TitleView
from partbox import PartModel
from partbox import PartView
#from part_dict import PartDictModel
from part_dict import PartDictView

import tkinter as tk

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
] # 나중에 db에 있는 단어장 dictionary에 넣기
word_cnt = len(dictionary) # 단어 총 개수 -> 나중에 1200(?)로 수정
learned_word_list=list(range(0,word_cnt//10)) # range(0,파트 개수) -> list에는 각 part에서의 배운 단어 개수가 들어간다.
sentence = dictionary # 나중에 db에 있는 예문 넣기 ! , 임시로 sentence = dictionary로 했음

# 타이틀바 생성
title = TitleView(root)
title.init_title()

# 단어장 db 생성 -> 단어장, 단어 개수, 파트 별 배운 단어 개수
#dictionary_db = PartModel(dictionary,learned_word_list)

# 단어장 GUI 생성
for part_index in range(0,int(word_cnt/10)): # 각 파트에 단어 10개만 있다고 가정. 나중에 120개로 수정
    partbox = PartView(root,title.frame,part_index,learned_word_list[part_index])
    partbox.init_part()
    for i in range(part_index*10,part_index*10+10):
        partdict = PartDictView(root,dictionary[i],sentence[i])
        partdict.init_part_dict()
root.mainloop()
