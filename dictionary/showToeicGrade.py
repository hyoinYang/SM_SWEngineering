import tkinter as tk
from tkinter import ttk, messagebox

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


# 사이드바 클릭시 로직
def validate_sidebar(current_window):
    #open_sidebar_window(current_window)
    current_window.destroy()

def open_ybm_grade(root):
    # 기존 윈도우 내용 삭제
    for widget in root.winfo_children():
        widget.destroy()

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

    # 회색바 꾸미기: "시험 점수 조회" 글씨 넣기
    text_label = tk.Label(title_bar_frame, text="시험 점수 조회", font=("Helvetica", 15))
    text_label.pack(side="left", padx=5)

    # 회색바 꾸미기: 사이드바 버튼 넣기
    sidebar_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

    sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:validate_sidebar(root))
    sidebar_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
    sidebar_button.pack(side="right", padx=5)

    # 메인 프레임 생성 및 배치
    main_frame = tk.Frame(root, bg="white", height=550)
    main_frame.pack(fill="both", expand=True)

    # 회색 프레임 생성 및 배치
    gray_frame = tk.Frame(main_frame, bg="gray", width=600, height=200)
    gray_frame.place(relx=0.5, rely=0.25, anchor="center")


    # 프레임 생성
    id_frame = tk.Frame(gray_frame)
    id_frame.pack(padx=10, pady=10)

    # 아이콘 이미지 로드
    name_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

    # 아이콘을 표시할 Label 위젯 생성
    icon_label = tk.Label(id_frame, image=sidebar_icon)
    icon_label.pack(side="left")

    # Entry 위젯 생성
    id_entry = tk.Entry(id_frame)
    id_entry.insert(0, "Username")
    id_entry.pack(side="left")

    # 비밀번호 입력 엔트리.
    # 프레임 생성
    pass_frame = tk.Frame(gray_frame)
    pass_frame.pack(padx=10, pady=10)

    # 아이콘 이미지 로드
    password_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

    # 아이콘을 표시할 Label 위젯 생성
    icon_label = tk.Label(pass_frame, image=password_icon)
    icon_label.pack(side="left")

    # Entry 위젯 생성
    pass_entry = tk.Entry(pass_frame)
    pass_entry.insert(0, "Password")
    pass_entry.pack(side="left")



    root.mainloop()
