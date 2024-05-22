import tkinter as tk
from tkinter import ttk
import random
"""
1. 단어 조회에 체크 표시
2. 단어 개수에 따라 part 정해지도록
3. assets 파일 지우고 resource에 옮기기
"""
word_texts = [] # 프레임에 들어가는 텍스트 클래스( 단어 )
sentence_texts = [] # 초록색 프레임에 들어가는 텍스트 클래스 ( 예문 )
wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
random_index=list(range(0,10)) # 랜덤 함수에서 사용, 임시로 단어 10개라고 설정했기 때문에 range(0,10)으로 설정함 
learned_word = 0 # 학습한 단어 개수
learning_rate = 0.0 # 학습률

# 사이드바 클릭시 로직
def validate_sidebar(current_window):
    #open_sidebar_window(current_window)
    current_window.destroy()

# 단어장에서 초록 박스를 버튼으로 여는 함수
def open_green_box(white_box,green_box,dictionary_box,dic_button,text):
    dictionary_box.pack(fill="both", expand=True)
    dic_button_image = tk.PhotoImage(file="resource/button_6.png").subsample(2,2)
    dic_button.config(
        command=lambda:close_green_box(white_box,green_box,dictionary_box,dic_button,text),
        image=dic_button_image
    )
    dic_button.image = dic_button_image
    
# 단어장에서 초록 박스를 버튼으로 닫는 함수
def close_green_box(white_box,green_box,dictionary_box,dic_button,text):
    dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2)
    dic_button.config(
        command=lambda:open_green_box(white_box,green_box,dictionary_box,dic_button,text),
        image=dic_button_image
    )
    dic_button.image = dic_button_image
    dictionary_box.pack_forget()
    green_box.config(height=1)

# 단어장에서 랜덤 버튼 클릭
def random_button_click(sequence_button,dic_list):
    random.shuffle(random_index)
    for new_text,new_sentence,i in zip(word_texts,sentence_texts,random_index):
        new_text.config(state=tk.NORMAL)
        new_sentence.config(state=tk.NORMAL)
        new_text.delete("1.0",tk.END)
        new_sentence.delete("1.0",tk.END)
        new_text.insert(tk.END,dic_list[random_index[i]])
        new_sentence.insert(tk.END,dic_list[random_index[i]])

    sequence_button.config(text="순행",command=lambda:sequence_button_click(sequence_button,dic_list))

# 단어장에서 순행 버튼 클릭
def sequence_button_click(sequence_button,dic_list):
    index = list(range(0,10))
    for new_text,new_sentence,i in zip(word_texts,sentence_texts,index):
        new_text.config(state=tk.NORMAL)
        new_sentence.config(state=tk.NORMAL)
        new_text.delete("1.0",tk.END)
        new_sentence.delete("1.0",tk.END)
        new_text.insert(tk.END,dic_list[i])
        new_sentence.insert(tk.END,dic_list[i])

    sequence_button.config(text="랜덤",command=lambda:random_button_click(sequence_button,dic_list))

# 즐겨찾기 버튼 
def favorites_button_click(favorites_button,word_index):
    favorites_button.config(bg="yellow")
    favorites_button.after(1000,lambda:favorites_button.config(bg="SystemButtonFace"))
    word = word_texts[word_index].get("1.0",tk.END).replace("\n","")
    if word in wrong_word_texts:
        print("이미 있음")
        return
    wrong_word_texts.append(word)
    print(f"오답노트에 {word}가 추가되었습니다.")

# 단어 발음 버튼
def sound_button_click(sound_button,i):
    sound_button.config(bg="red")
    sound_button.after(1000,lambda:sound_button.config(bg="SystemButtonFace"))
    word = word_texts[i].get("1.0",tk.END).replace("\n","")
    print(word)

# 학습률 버튼
def check_button_click(check_button):
    global learned_word
    learned_word+=1
    learning_rate = learned_word / len(dic_list) * 100 # 학습률 
    print(f"학습률:{learning_rate}%")
    check_button.config(bg="yellow")
    check_button.after(1000,lambda:check_button.config(bg="SystemButtonFace"))

def create_scrollable_text(parent_frame, text,word_index): # text에는 박스에 있는 영어 단어가 옴
    # 흰색 박스 생성
    white_box = tk.Frame(parent_frame, bg="white",borderwidth=2, relief="ridge")
    white_box.pack(pady=10,fill="x")

    # 초록색 박스 생성
    green_box = tk.Frame(white_box, bg="white",borderwidth=0, relief="ridge")
    green_box.pack(side="bottom",fill="x")
    
    # 단어 상자 생성
    dictionary_box = tk.Text(green_box, height=12,bg="lightgreen",borderwidth=0)
    dictionary_box.insert("end", text)
    dictionary_box.config(state="disabled")
    sentence_texts.append(dictionary_box)

    # 즐겨찾기 버튼 생성
    favorites_button_image = tk.PhotoImage(file="resource/favorites_icon.png").subsample(15)
    favorites_button = tk.Button(white_box,image = favorites_button_image,relief="flat",command=lambda:favorites_button_click(favorites_button,word_index)) # 나중에 오답노트로 저장하는 모듈로 바꿔주기
    favorites_button.image = favorites_button_image
    favorites_button.pack(anchor = "e")

    #음성 버튼 생성
    sound_button_image = tk.PhotoImage(file="resource/sound_icon.png").subsample(15)
    sound_button = tk.Button(white_box,image = sound_button_image, relief="flat",command=lambda:sound_button_click(sound_button,word_index)) # 나중에 음성 모듈로 바꿔주기
    sound_button.image = sound_button_image
    sound_button.pack(anchor="e",pady = 0)

    # 뜻 여는 버튼 생성
    dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2)
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

def open_dic_part_window(current_window,part): #part는 part1,part2,...,part6을 구분하는 파라미터 정수가 들어옴
        # 기존 윈도우 내용 삭제
    for widget in current_window.winfo_children():
        widget.destroy()

    # 스타일 설정
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

    # 랜덤, 순행 버튼
    sequence_button = tk.Button(current_window,bg="white",text="랜덤",font=("Helvetica", 15),command=lambda:random_button_click(sequence_button,dic_list))
    sequence_button.pack(side="top",anchor="center")

    # Canvas 생성
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

    # 임시 단어 케이스, 파트에 따라 단어가 달라지도록
    # 5/7 까지 수정, -> 버튼 part 별로 command 설정하기
    global dic_list
    if part==1:
        dic_list=["apple","banana","chief","depend","eagle","fantastic","golf","high","identify","joke"]
    elif part == 2:
        dic_list=["sophisticated","quality","complete","information","consecutive","deliberation","formerly","enhance","decrease","estimate"]
    elif part == 3:
        dic_list=["impressive","reduce","beware","innate","restor","necessary","health","renovate","arise","certain"]
    elif part == 4:
        dic_list=["delicate","disturb","speculate","scenery","consist","deficit","symptom","exceed","direct","policy"]
    elif part == 5:
        dic_list = ["policy","circumscribe","prohibit","prohibition","budget","preserve","calcuate","assent","exhibit","safety"]
    elif part == 6:
        dic_list = ["refuse","expend","require","contribute","competent","insurance","frquently","mandatory","retire","abuse"]
    # 문제 개수에 맞는 초록색 박스 생성
    for word_index in range(len(dic_list)):
        create_scrollable_text(frame, dic_list[word_index],word_index)

    # 윈도우 실행
    current_window.mainloop()