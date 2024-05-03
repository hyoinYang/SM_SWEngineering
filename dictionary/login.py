import tkinter as tk
from tkinter import ttk, messagebox
from sidebar import open_sidebar_window

# 데이터 코드 필요) 로그인 로직 작성
def validate_login():
    # 여기에 로그인 검증 로직을 추가하세요
    username = username_entry.get()
    password = password_entry.get()
    
    # 간단한 검증: username이 "admin", password가 "12345"인 경우에만 로그인 성공으로 가정
    if username == "admin" and password == "12345":
        messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")


#  데이터 코드 필요) 회원가입 로직 작성
def validate_signup():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "12345":
        messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")


# 사이드바 클릭시 로직
def validate_sidebar(current_window):
    open_sidebar_window(current_window)


# 윈도우 생성
root = tk.Tk()
root.title("로그인 화면")

# 스타일 설정
style = ttk.Style()
style.theme_use('clam')  # 스타일 테마 선택 (Tkinter의 기본 테마 중 하나)

# 회색 바 스타일 설정
style.configure('TFrame', background='#d9d9d9')  # 회색 바 색상 설정

# 윈도우 크기 설정
root.geometry("700x550")

# 회색 바 스타일 설정
style.configure('TFrame', background='#838383')  # 스타일에 색상을 지정합니다.

# 회색 바 프레임
title_bar_frame = ttk.Frame(root, style='TFrame', height=30)
title_bar_frame.pack(fill='x')
title_bar_frame.pack(pady=10)

# 회색바 꾸미기: 톱니바퀴 이미지 넣기
gear_icon = tk.PhotoImage(file="resource/gear_icon.png").subsample(10)

gear_button = tk.Label(title_bar_frame, image=gear_icon, relief="flat", bd=0)
gear_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
gear_button.pack(side="left", padx=5)

# 회색바 꾸미기: "토익단어" 글씨 넣기
text_label = tk.Label(title_bar_frame, text="토익단어", font=("Helvetica", 15))
text_label.pack(side="left", padx=5)

# 회색바 꾸미기: 사이드바 버튼 넣기
sidebar_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:validate_sidebar(root))
sidebar_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
sidebar_button.pack(side="right", padx=5)


# 사용자 이름 라벨 및 텍스트 상자
username_label = tk.Label(root, text="사용자 이름:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# 비밀번호 라벨 및 텍스트 상자
password_label = tk.Label(root, text="비밀번호:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# 로그인 버튼
login_button = tk.Button(root, text="로그인", command=validate_login, bg="#838383")
login_button.pack(pady=10)

# 회원가입 버튼
signup_button = tk.Button(root, text="회원가입", command=validate_signup, bg="#838383")
signup_button.pack(pady=10)


# 윈도우 실행
root.mainloop()
