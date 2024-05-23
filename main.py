from titlebar import TitleView
from partbox import PartModel
from partbox import PartView
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

word_cnt = 90 # 단어장에 들어갈 전체 단어 개수, 추 후에 수정 !!
learned_word_list=list(range(0,word_cnt//10)) # range(0,파트 개수) -> list에는 각 part에서의 배운 단어 개수가 들어간다.

# 타이틀바 생성
title = TitleView(root)
title.init_title()

# 단어장 db 생성
dictionary_db = PartModel(word_cnt,learned_word_list)

# 단어장 GUI 생성
for part_index in range(0,int(word_cnt/10)):
    part = PartView(root,title.frame,part_index,learned_word_list[part_index])
    part.init_part()

# 
root.mainloop()

