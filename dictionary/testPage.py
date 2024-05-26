import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------- Model -----------------------------
class TestModel:
    def __init__(self):
        self.question_num = 10  # 테스트 문제 개수

    def get_question_text(self, question_num):
        # 테스트 문제 번호에 따른 텍스트 반환
        return f"텍스트 내용입니다. {question_num+1}번째 박스입니다."

# ----------------------------- View -----------------------------
class TestView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    # UI 생성 코드
    def setup_ui(self):
        
        # 기존 윈도우 내용 삭제
        for widget in self.root.winfo_children():
            widget.destroy()

        style = ttk.Style()
        style.theme_use('clam')  # 스타일 테마 선택 (Tkinter의 기본 테마 중 하나)

        # 회색 바 스타일 설정
        style.configure('TFrame', background='#838383')  # 스타일에 색상을 지정합니다.

        # 회색 바 프레임
        title_bar_frame = ttk.Frame(self.root, style='TFrame', height=30)
        title_bar_frame.pack(fill='x')
        title_bar_frame.pack(pady=10)

        # 회색바 꾸미기: 톱니바퀴 이미지 넣기
        gear_icon = tk.PhotoImage(file="resource/gear_icon.png").subsample(10)
        gear_button = tk.Label(title_bar_frame, image=gear_icon, relief="flat", bd=0, bg="#838383", cursor="hand2")
        gear_button.image = gear_icon
        gear_button.pack(side="left", padx=5)

        # 회색바 꾸미기: "토익단어" 글씨 넣기
        text_label = tk.Label(title_bar_frame, text="토익단어", font=("Helvetica", 15), bg="#838383", cursor="hand2")
        text_label.pack(side="left", padx=5)

        # 회색바 꾸미기: 사이드바 버튼 넣기
        sidebar_icon = tk.PhotoImage(file="resource/sidebar_icon.png").subsample(10)

        sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:TestView.validate_sidebar(self), bg="#838383", cursor="hand2")
        sidebar_button.image = gear_icon  # 이미지가 garbage-collected 되는 것을 방지
        sidebar_button.pack(side="right", padx=5)

        # Canvas 생성
        canvas = tk.Canvas(self.root)
        canvas.pack(side="left", fill="both", expand=True)

        # 스크롤바 생성
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Canvas에 스크롤바 바인딩
        canvas.configure(yscrollcommand=scrollbar.set)

        # 내부 프레임 생성
        frame = tk.Frame(canvas)
        canvas.create_window((30, 0), window=frame, anchor="nw")

        # 내부 프레임의 사이즈 변경 시 Canvas 업데이트
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))



        # 문제 개수에 맞는 초록색 박스 생성
        question_num = 10
        for i in range(question_num):
            text = f"텍스트 내용입니다. {i+1}번째 박스입니다."
            TestView.create_scrollable_text(frame, i, text)

        # 윈도우 실행
        self.root.mainloop


    # 사이드바 클릭시 로직
    def validate_sidebar(current_window):
        #open_sidebar_window(current_window)
        current_window.destroy()

    def create_scrollable_text(parent_frame, question_num, text):
        def handle_enter(event):
            # 입력 상자에서 엔터 키를 눌렀을 때의 동작
            user_input = input_box.get()  # 입력 상자에서 입력된 내용 가져오기
            print("User input:", user_input)  # 입력된 내용을 터미널에 출력하기
            input_box.delete(0, "end")  # 입력 상자 초기화

        # 초록색 박스 생성
        green_box = tk.Frame(parent_frame, bg="white")
        green_box.pack(pady=5, fill="x")

        # 흰색 박스 생성 및 배치
        white_box = tk.Frame(green_box, bg="white")
        white_box.pack(side="top", fill="x")

        # 문제번호 텍스트 생성 및 배치
        question_label = tk.Label(white_box, text=question_num, bg="white", fg="black")
        question_label.pack(side="left", padx=10, pady=10)

        # 스크롤 가능한 텍스트 박스 생성
        text_box = tk.Text(green_box, bg="lightgreen", fg="white", wrap="word", height=4, padx=20, pady=20)
        text_box.insert("end", text)
        text_box.config(state="disabled")
        text_box.pack(side="top", fill="both", expand=True)

        # 입력을 받는 박스 생성 및 배치
        input_box = tk.Entry(green_box, bg="white", fg="black", bd=2)
        input_box.pack(side="top", fill="x", padx=20, pady=10)
        input_box.bind("<Return>", handle_enter)  # Enter 키에 대한 이벤트 핸들러 바인딩

# ----------------------------- Controller -----------------------------
class TestController:
    def __init__(self, root):
        self.model = TestModel
        self.view = TestView(root)

    def open_testPage_window(self):
        self.view.open_testPage_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()