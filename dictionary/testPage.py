import tkinter as tk
from tkinter import ttk, messagebox
#from sidebar import open_sidebar_window

questions = []

def submit_answer(event):
    entry = event.widget
    answer = entry.get()
    print("Submitted Answer:", answer)
    entry.delete(0, "end")  # 입력창 초기화

# 문제 유형에 맞춰서 질문들을 셋팅하는 함수.
def print_selected_item(event):
    selected_item = combo_box.get()

    if selected_item == "PART1":
        # questions와 관련된 로직
        return questions
    elif selected_item == "PART2":
        return questions
    else:
        return questions

    

def close_testPage(window):
    # 테스트 내용을 저장하는 로직
    window.destroy()

# 윈도우 생성
root = tk.Tk()
root.title("단어 테스트")

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

# 회색바 꾸미기: "단어 테스트" 글씨 넣기
text_label = tk.Label(title_bar_frame, text="단어 테스트", font=("Helvetica", 15))
text_label.pack(side="left", padx=5)

# 회색바 꾸미기: 사이드바 버튼 넣기
# 이때 사이드바 버튼을 누르면, 테스트 내용들이 저장되고, 윈도우가 꺼진다.
sidebar_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:close_testPage(root))
sidebar_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
sidebar_button.pack(side="right", padx=5)

# 스타일 설정
style = ttk.Style()

# 콤보박스 스타일 설정
style.configure('Custom.TCombobox', background='#4f4f4f')

# 콤보박스를 담을 프레임 생성
combo_frame = tk.Frame(root, bg="#d9d9d9", width=600, height=100)
combo_frame.place(x=50, y=70)

# 문제 유형을 고르는 콤보박스 추가
test_num = ["PART1", "PART2", "PART3"]
combo_box = ttk.Combobox(root, value = test_num)
combo_box.pack()
combo_box.bind("<<ComboboxSelected>>", print_selected_item)  # 콤보박스에서 항목 선택 시 호출될 함수 연결


# 캔버스 프레임 생성
canvas_frame = tk.Frame(root, bg="#d9d9d9", width=500, height=300)
canvas_frame.place(x=150, y=300)

# 스크롤바 생성
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# 캔버스 생성
canvas = tk.Canvas(canvas_frame)
canvas.pack(side="left", fill="both", expand=True)

# 캔버스의 스크롤 지원 설정
canvas.configure(yscrollcommand=scrollbar.set)

# 문제들을 담는 캔버스에 캔버스 위젯 추가
inner_frame = tk.Frame(canvas, bg="lightgreen")  # 내부 프레임 생성
# 내부 프레임을 캔버스에 추가
canvas.create_window((0, 0), window=inner_frame, anchor="nw")


# 내부 프레임에 위젯들 추가 (예시로 10개의 레이블과 엔트리 추가)
for i in range(1, 11):

    question_number = f"{i}:"
    number_label = tk.Label(inner_frame, text=question_number, bg="white")
    number_label.pack(fill="x")
        
    label_text = f"Test Question {i}: This is a long question that will wrap to the next line"
    label = tk.Label(inner_frame, text=label_text, bg="lightgreen", padx=10, pady=5, wraplength=400, anchor="w")
    label.pack(fill="x")

    # label_text를 label 너비에 맞게 조정하여 설정
    label.config(text=label_text)

    # label 너비보다 긴 텍스트를 처리하기 위해 개행 문자 추가
    while label.winfo_reqwidth() > label.winfo_width():
        # 현재 label_text의 길이를 반으로 줄임
        half_length = len(label_text) // 2
        # 반으로 줄인 길이에서 마지막 공백 위치를 찾음
        last_space = label_text.rfind(' ', 0, half_length)
        # 공백을 기준으로 label_text를 두 줄로 분할
        label_text = label_text[:last_space] + '\n' + label_text[last_space+1:]

    # 최종 label_text 설정
    label.config(text=label_text)


    entry = tk.Entry(inner_frame, bg="lightgreen")
    entry.pack(fill="x")
    entry.bind("<Return>", submit_answer)  # 엔터 키로 답변 제출

# 스크롤 설정
scrollbar.config(command=canvas.yview)

# 내부 프레임의 크기 업데이트
inner_frame.update_idletasks()

# 캔버스의 스크롤 지역을 내부 프레임의 크기로 설정하여 스크롤 영역 조정
canvas.config(scrollregion=canvas.bbox("all"))

# 캔버스 프레임을 윈도우에 추가
canvas_frame.pack()

# 캔버스를 아래로 50픽셀 이동
canvas_frame.place(x=150, y=200)

# 윈도우 실행
root.mainloop()

