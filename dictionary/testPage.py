import tkinter as tk
from tkinter import ttk, messagebox
import part_dict as star
import partbox as pb
import math

# ----------------------------- Model -----------------------------
class TestModel:
    combo_values = []
    
    # 문제들을 담는 배열입니다.
    questions = ["test", "ttt"]
    question_num = 2

    for part_index in range(0, math.ceil(pb.partmodel.word_cnt/30)): # part 개수 계산
        combo_values.append("PART " + str(part_index+1))


    def __init__(self, root):
        self.root = root

# ----------------------------- View -----------------------------
class TestView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    # UI 생성 코드
    def setup_ui(self):
        # 콤보박스 생성
        part_combo_box = ttk.Combobox(self.root, values=TestModel.combo_values)
        part_combo_box.pack(padx=5)
        part_combo_box.bind("<<ComboboxSelected>>", TestController.select_part)

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

        idx = 0
        # 문제 개수와 문제에 맞는 박스(초록색) 생성
        for i in range(TestModel.question_num):
            text = TestModel.questions[idx]
            TestView.create_scrollable_text(frame, i, text)
            idx=idx+1

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
    def __init__(self, root, partmodel):
        self.model = TestModel
        self.view = TestView(root)
        self.partmodel = partmodel

    def open_testPage_window(self):
        self.view.open_testPage_window()

    # 콤보박스 선택에 맞춰서 문제들을 셋팅하는 함수입니다.
    # 세팅방법은 임의로 정했습니다. 원래라면 데이터베이스에서 찾아와야 합니다.
    # 데이터베이스에 연결시: Model 내 questions를 수정해야 합니다. (questions를 Model 내에서 그대로 출력합니다.)
    def select_part(event):
        part = event.widget.get()
        print(part)
        
        if (part == "PART 1"):
            selected_questions=TestModel.questions[0]
        
    
"""
if __name__ == "__main__":
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()"""