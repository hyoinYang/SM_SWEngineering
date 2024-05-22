# from tkinter import *
# Explicit imports to satisfy Flake8
from sidebar import open_sidebar_window
from dic_part import open_dic_part_window
from tkinter import ttk
from tkinter.ttk import Progressbar, Label
import tkinter as tk

word_cnt = 90 # 나중에 데이터베이스에 있는 단어 개수로 바꿔주기, 단어 개수에 따라 part가 많이 생김
learned_word_list=list(range(0,word_cnt//10)) # range(0,파트 개수) -> list에는 각 part에서의 배운 단어 개수가 들어간다.
# 단어장 화면에서 사이드바 여는 함수
def validate_sidebar(current_window):
    open_sidebar_window(current_window)

# image에 접근하기 위해 path 설정

# part1~n frame, 버튼 만드는 함수
def create_dic_part(frame,current_window,part_index):
    white_box = tk.Frame(frame, bg="lightgray",borderwidth=0, relief="ridge",width=600, height=140)
    white_box.pack_propagate(False)
    white_box.pack(pady=10,fill="x")
    # part 1 ~ n 버튼 생성
    part_button = tk.Button(white_box,relief="flat",text=f"PART {part_index+1}",width=11,height=2,font="Helvetica",command=lambda:open_dic_part_window(current_window,part_index+1))
    part_button.pack(side="top",anchor="nw", padx=10,pady=10)
    
    # 학습률 글씨 생성
    learned_word = learned_word_list[part_index]
    progress_label = Label(white_box, text=f"학습률: {learned_word} / 120 [ {learned_word//120*100}% ]",background="white",font="Helvetica") #
    progress_label.place(relx=0.55,rely=0.73)

    # 학습률에 따른 상자 생성
    progress_bar = Progressbar(white_box, orient="horizontal", mode="determinate",length=300)
    progress_bar['value']= learned_word//120*100 # 학습률 넣기
    progress_bar.pack(side="bottom",anchor="sw",padx=10, pady=15)
    
# 단어장 window를 여는 함수 ( ex. login 페이지에서 로그인을 했을 때 )
def open_dic_window(current_window):
    for widget in current_window.winfo_children():
        widget.destroy()    

    style = ttk.Style()
    style.theme_use('clam')  # 스타일 테마 선택 (Tkinter의 기본 테마 중 하나)

    # 회색 바 스타일 설정
    style.configure('TFrame', background='#838383')  # 스타일에 색상을 지정합니다.

    # 회색 바 프레임
    title_bar_frame = ttk.Frame(current_window, style='TFrame', height=30)
    title_bar_frame.pack(fill='x')
    title_bar_frame.pack(pady=10)

    # 회색바 꾸미기: 톱니바퀴 이미지 넣기
    gear_icon = tk.PhotoImage(file="resource/gear_icon.png").subsample(10)
    gear_button = tk.Label(title_bar_frame, image=gear_icon, relief="flat", bd=0,bg='#838383')
    gear_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
    gear_button.pack(side="left", padx=5)

    # 회색바 꾸미기: "토익단어" 글씨 넣기
    text_label = tk.Label(title_bar_frame, text="토익단어", font=("Helvetica", 15))
    text_label.pack(side="left", padx=5)

    # 회색바 꾸미기: 사이드바 버튼 넣기
    sidebar_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

    sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:validate_sidebar(current_window),bg='#838383')
    sidebar_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
    sidebar_button.pack(side="right", padx=5)

    canvas = tk.Canvas(current_window)
    canvas.pack(side="left", fill="both", expand=True)
    
    # 스크롤바 생성
    scrollbar = ttk.Scrollbar(current_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Canvas에 스크롤바 바인딩
    canvas.configure(yscrollcommand=scrollbar.set)

    # 내부 프레임 생성
    frame = tk.Frame(canvas)
    canvas.create_window((30, 0), window=frame, anchor="nw")

    # 내부 프레임의 사이즈 변경 시 Canvas 업데이트
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    for part_index in range(0,int(word_cnt/10)):
        create_dic_part(frame,current_window,part_index)

    # 윈도우 실행
    current_window.mainloop()

# 실행 확인할 수 있게 임시로 해놓은 것. 코드 병합하면 지울 예정임
if __name__ == "__main__":
    root = tk.Tk()
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    open_dic_window(root)
