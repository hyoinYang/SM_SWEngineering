import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 은희님!!!!!!!!!!!! 여기 데이터들어가니까 수정해주시면 됩니다!!!!!!!!!!!!!!!!!!!!!!!
#exam_info 변수명 그대로 두고, 일정, 접수기간, 성적발표 틀 규격만 지켜 주시면 정상 작동 될 듯 합니다! 
#혹시 문제 생기면 # 시험 정보 리스트 트리뷰에 추가 (구분선을 이용해 각 열 사이에 구분 추가) 이 부분이랑 교차 확인 부탁드립니다!

exam_info = [
    {"일정": "2024년 4월 14일 (일) \n09:20",
     "접수기간": "2024년 2월 26일 (월) \n~ 2024년 4월 1일 (월)",
     "성적발표": "2024년 4월 24일 (수) \n12:00"},
    {"일정": "2024년 5월 19일 (일) \n09:20",
     "접수기간": "2024년 3월 25일 (월) \n~ 2024년 5월 13일 (월)",
     "성적발표": "2024년 5월 28일 (화) \n09:20"},
    {"일정": "2024년 6월 16일 (일) \n09:20",
     "접수기간": "2024년 4월 29일 (월) \n~ 2024년 6월 10일 (월)",
     "성적발표": "2024년 6월 25일 (화) \n09:20"},
]
# 여기까지!!!!!!!!!!!!!!!!!!!!!!! ---------------------------------------------------------------------------------

# 창 생성 및 초기 설정
root = tk.Tk()
root.title("토익 시험 일정")
root.geometry("700x550")
root.configure(background="#FFFFFF")  # 흰색 배경색으로 변경

# 스타일 설정
style = ttk.Style()
style.theme_use('clam')  

#---------------------------회색바 내용-------------------------------------------------------------------------------------------------

# 회색 바 스타일 설정
style.configure('TFrame', background='#838383')  

# 회색 바 프레임 생성 및 배치
title_bar_frame = ttk.Frame(root, style='TFrame', height=30)
title_bar_frame.pack(fill='x')

# 톱니바퀴 이미지 경로
gear_icon_path = "dictionary/assets/frame2/title_bar_frame_image/gear_icon.png"

# 메뉴 이미지 경로
menu_icon_path = "dictionary/assets/frame2/title_bar_frame_image/sidebar_icon.png"


# 이미지 불러오기 및 처리
gear_icon = ImageTk.PhotoImage(Image.open(gear_icon_path).resize((30, 30)))
menu_icon = ImageTk.PhotoImage(Image.open(menu_icon_path).resize((30, 30)))

# 톱니바퀴 버튼 생성 및 배치 (회색 바 프레임 내)
gear_button = tk.Button(title_bar_frame, image=gear_icon, borderwidth=0, bg="#838383", cursor="hand2")
gear_button.pack(side=tk.LEFT, padx=20)

# 회색바 꾸미기:  글씨 넣기
text_label = tk.Label(title_bar_frame, text="토익 시험 일정", font=("Helvetica", 15, "bold"), background="#838383")
text_label.pack(side="left", padx=5)

# 메뉴 버튼 생성 및 배치 (회색 바 프레임 내)
menu_button = tk.Button(title_bar_frame, image=menu_icon, borderwidth=0, bg="#838383", cursor="hand2")
menu_button.pack(side=tk.RIGHT, padx=20)

#--------------------안에 표 위젯 내용------------------------------------------------------------------------------------------
# 트리뷰이 위젯 생성
tree = ttk.Treeview(root, columns=("일정", "접수기간", "성적발표"), show="headings")
tree.heading("일정", text="일정")
tree.heading("접수기간", text="접수기간")
tree.heading("성적발표", text="성적발표")

# 트리뷰이 위젯 배치 위 아래 간격을 20픽셀만큼 두겠다는 뜻.
tree.pack(pady=20)

# 트리뷰이 스타일 설정
tree.style = ttk.Style()
tree.style.configure("Treeview.Item", background="#FFFFFF")  # 아이템 배경색
tree.style.configure("Treeview.Heading", background="#FFFFFF", foreground="#000000", font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
tree.style.configure("Treeview.Separator")  # 구분선 배경색



# 트리뷰이 열 너비 설정 및 구분선 추가
tree.column("일정", width=200, anchor="center")
tree.column("접수기간", width=200, anchor="center")
tree.column("성적발표", width=200, anchor="center")

# 트리뷰이 스타일 설정: 구분선 색상 및 두께 조정
tree.style.configure("Treeview.Separator", background="#FFFFFF", foreground="#FFFFFF", thickness=0)

# 트리뷰의 행 높이 설정
style.configure("Custom.Treeview", rowheight=30)  # 행 높이를 30으로 설정
tree.configure(style="Custom.Treeview")

# 시험 정보 리스트 트리뷰에 추가 (구분선을 이용해 각 열 사이에 구분 추가)
tree.insert("", tk.END, values=("", ""))
for info in exam_info:
    tree.insert("", tk.END, values=list(info.values()))
    tree.insert("", tk.END, values=("─" * 100, "─" * 100, "─" * 100))

# 실행
root.mainloop()
