import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

gear_icon_path = "dictionary/assets/frame2/title_bar_frame_image/gear_icon.png"
menu_icon_path = "dictionary/assets/frame2/title_bar_frame_image/sidebar_icon.png"

# -------------------------------- 버튼 관련 함수 구현  --------------------------------
def upload_csv_file():
    print("csv 파일 업로드 완")


# -------------------------------- 엔트리 관련 함수 --------------------------------

# 삭제하기
def delete_enter(event):
    # 입력 상자에서 입력된 내용 가져오기
    word = del_entry.get()
    
    # 입력된 내용을 터미널에 출력하기
    if (word == "삭제할 단어"):
        print("ERROR: 모든 단어 입력 X")
    else:
        print("Delete input:", word) 

        # 입력 상자 초기화
        del_entry.delete(0, "end")
        del_entry.insert(0, "삭제할 단어")

# 수정하기
def modify_enter(event):
    # 입력 상자에서 입력된 내용 가져오기
    word = modify_word_entry.get()
    korean=modify_korean_entry.get()
    example = modify_ex_entry.get()

    # 입력된 내용을 터미널에 출력하기
    if (word == "추가할 단어" or korean == "추가할 단어의 뜻" or example == "추가할 단어의 예문"):
        print("ERROR: 모든 단어 입력 X")
    else:
        print("Modify input) word = %s, korean = %s, example = %s", word, korean, example)
        # 입력 상자 초기화
        add_word_entry.delete(0, "end")
        add_word_entry.insert(0, "추가할 단어")
        add_korean_entry.delete(0, "end")
        add_korean_entry.insert(0, "추가할 단어의 뜻")
        add_ex_entry.delete(0, "end")
        add_ex_entry.insert(0, "추가할 단어의 예문")


# 추가하기
def add_enter(event):
    # 입력 상자에서 입력된 내용 가져오기
    word = add_word_entry.get()
    korean=add_korean_entry.get()
    example = add_ex_entry.get()

    # 입력된 내용을 터미널에 출력하기
    if (word == "추가할 단어" or korean == "추가할 단어의 뜻" or example == "추가할 단어의 예문"):
        print("ERROR: 모든 단어 입력 X")
    else:
        print("Add input) word = %s, korean = %s, example = %s", word, korean, example)
        # 입력 상자 초기화
        add_word_entry.delete(0, "end")
        add_word_entry.insert(0, "추가할 단어")
        add_korean_entry.delete(0, "end")
        add_korean_entry.insert(0, "추가할 단어의 뜻")
        add_ex_entry.delete(0, "end")
        add_ex_entry.insert(0, "추가할 단어의 예문")


# -------------------------------- GUI 초기화 --------------------------------
root = tk.Tk()
root.title("단어 관리")
root.geometry("700x550")
root.configure(background="#FFFFFF")  

style = ttk.Style()
style.theme_use('clam')

# -------------------------------- 회색 바 설정 --------------------------------
style.configure('TFrame', background='#838383')
title_bar_frame = ttk.Frame(root, style='TFrame', height=30)
title_bar_frame.pack(fill='x')

gear_icon = ImageTk.PhotoImage(Image.open(gear_icon_path).resize((30, 30)))
menu_icon = ImageTk.PhotoImage(Image.open(menu_icon_path).resize((30, 30)))

gear_button = tk.Button(title_bar_frame, image=gear_icon, borderwidth=0, bg="#838383", cursor="hand2")
gear_button.pack(side=tk.LEFT, padx=20)

text_label = tk.Label(title_bar_frame, text="단어 관리", font=("Helvetica", 15, "bold"), background="#838383")
text_label.pack(side="left", padx=5)

menu_button = tk.Button(title_bar_frame, image=menu_icon, borderwidth=0, bg="#838383", cursor="hand2")
menu_button.pack(side=tk.RIGHT, padx=20)

# -------------------------------- 내용 --------------------------------
# Canvas 생성
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# 내부 프레임 생성
frame = tk.Frame(canvas)
canvas.create_window((50, 0), window=frame, anchor="nw")

# 회색 박스 생성
delete_box = tk.Frame(frame, bg="#838383")
delete_box.pack(pady=30, fill="x")

# 단어 삭제 칸
del_text_box = tk.Label(delete_box, text="단어 삭제하기", font=("Helvetica", 15), bg="#838383")
del_text_box.pack(padx=5, pady=10)

del_entry = tk.Entry(delete_box, bg="white", fg="black", bd=2, relief="flat")
del_entry.insert(0, "삭제할 단어")
del_entry.pack(padx=20, pady=10)
del_entry.bind("<Return>", delete_enter)

# 단어 추가 칸
add_box = tk.Frame(frame, bg="gray")
add_box.pack(pady=30, fill="x")

add_text_box = tk.Label(add_box, text="단어 추가하기", font=("Helvetica", 15), bg="#838383")
add_text_box.pack(padx=20, pady=10)

add_word_entry = tk.Entry(add_box, bg="white", fg="black", bd=2, relief="flat")
add_word_entry.insert(0, "추가할 단어")
add_word_entry.pack(side="left", padx=20, pady=10)
add_word_entry.bind("<Return>", add_enter)

add_korean_entry = tk.Entry(add_box, bg="white", fg="black", bd=2, relief="flat")
add_korean_entry.insert(0, "추가할 단어의 뜻")
add_korean_entry.pack(side="left", fill="x", padx=20, pady=10)
add_korean_entry.bind("<Return>", add_enter)

add_ex_entry = tk.Entry(add_box, bg="white", fg="black", bd=2, relief="flat")
add_ex_entry.insert(0, "추가할 단어의 예문")
add_ex_entry.pack(side="left", fill="x", padx=20, pady=10)
add_ex_entry.bind("<Return>", add_enter)

# 단어 수정 칸
modify_box = tk.Frame(frame, bg="gray")
modify_box.pack(pady=30, fill="x")

text_box = tk.Label(modify_box, text="단어 수정하기", font=("Helvetica", 15), bg="#838383")
text_box.pack(padx=20, pady=10)

# 입력 상자(수정할 단어) 생성
modify_word_entry = tk.Entry(modify_box, bg="white", fg="black", bd=2, relief="flat")
modify_word_entry.pack(side="left", fill="x", padx=20, pady=10)
modify_word_entry.insert(0, "수정할 단어")
modify_word_entry.bind("<Return>", modify_enter)

# 입력 상자(수정할 내용) 생성
modify_korean_entry = tk.Entry(modify_box, bg="white", fg="black", bd=2, relief="flat")
modify_korean_entry.pack(side="left", fill="x", padx=20, pady=10)
modify_korean_entry.insert(0, "수정할 단어의 뜻")
modify_korean_entry.bind("<Return>", modify_enter)

modify_ex_entry = tk.Entry(modify_box, bg="white", fg="black", bd=2, relief="flat")
modify_ex_entry.pack(side="left", fill="x", padx=20, pady=10)
modify_ex_entry.insert(0, "수정할 단어의 예문")
modify_ex_entry.bind("<Return>", modify_enter)

# CSV 파일 업로드 버튼
upload_csv_icon = tk.PhotoImage(file="resource/csv_upload_btn.png").subsample(2)
upload_csv_button = tk.Button(canvas, image=upload_csv_icon, relief="flat", bd=0, command=lambda:upload_csv_file(), cursor="hand2")
upload_csv_button.image = upload_csv_icon
upload_csv_button.place(x=500, y=450)



root.mainloop()