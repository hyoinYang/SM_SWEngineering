import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

gear_icon_path = "dictionary/assets/frame2/title_bar_frame_image/gear_icon.png"
menu_icon_path = "dictionary/assets/frame2/title_bar_frame_image/sidebar_icon.png"

# -------------------------------- 버튼 관련 함수 구현  --------------------------------
def upload_csv_file():
    print("csv 파일 업로드 완")


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
canvas.create_window((30, 0), window=frame, anchor="nw")

# 회색 박스 생성
gray_box = tk.Frame(frame, bg="#838383")
gray_box.pack(pady=5, fill="x")

textTest="단어 삭제하기"

# 텍스트 박스 생성
text_box = tk.Text(gray_box, bg="#838383", fg="white", wrap="word", height=4, padx=20, pady=20)
text_box.insert("end", textTest)
text_box.config(state="disabled")
text_box.pack(side="top", fill="both", expand=True)

# 입력 상자 생성
input_box = tk.Entry(gray_box, bg="white", fg="black", bd=2)
input_box.pack(side="bottom", fill="x", padx=20, pady=10)


# 단어 추가 칸
gray_box = tk.Frame(frame, bg="gray")
gray_box.pack(pady=5, fill="x")

textTest="단어 추가하기"

text_box = tk.Text(gray_box, bg="gray", fg="white", wrap="word", height=4, padx=20, pady=20)
text_box.insert("end", textTest)
text_box.config(state="disabled")
text_box.pack(side="top", fill="both", expand=True)

# 입력 상자 생성
input_box = tk.Entry(gray_box, bg="white", fg="black", bd=2)
input_box.pack(side="left", fill="x", padx=20, pady=10)

# 입력 상자 생성
input_box = tk.Entry(gray_box, bg="white", fg="black", bd=2)
input_box.pack(side="right", fill="x", padx=20, pady=10)

# 단어 수정 칸
gray_box = tk.Frame(frame, bg="gray")
gray_box.pack(pady=5, fill="x")

textTest="단어 수정하기"

text_box = tk.Text(gray_box, bg="gray", fg="white", wrap="word", height=4, padx=20, pady=20)
text_box.insert("end", textTest)
text_box.config(state="disabled")
text_box.pack(side="top", fill="both", expand=True)

# 입력 상자 생성
input_box = tk.Entry(gray_box, bg="white", fg="black", bd=2)
input_box.pack(side="left", fill="x", padx=20, pady=10)

# 입력 상자 생성
input_box = tk.Entry(gray_box, bg="white", fg="black", bd=2)
input_box.pack(side="right", fill="x", padx=20, pady=10)

# CSV 파일 업로드 버튼
login_button = tk.Button(canvas, text="csv파일 업데이트하기", command=lambda:upload_csv_file, bg="#838383")
login_button.pack(side="bottom", pady=30)



root.mainloop()