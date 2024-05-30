import tkinter as tk
from tkinter import ttk, messagebox
import part_dict as star
import partbox as pb
import math

# ----------------------------- Model -----------------------------
import math

class TestModel:
    combo_values = []
    questions = []
    question_num = math.ceil(len(pb.partmodel.dictionary) / 30)
    start_idx = 0

    def __init__(self):
        part_size = 30
        total_words = len(pb.partmodel.dictionary)
        num_parts = math.ceil(total_words / part_size)
        for part_index in range(num_parts):
            start_index = part_index * part_size
            end_index = min((part_index + 1) * part_size, total_words)
            part_questions = pb.partmodel.dictionary[start_index:end_index]
            self.questions.extend(part_questions)
            self.combo_values.append("PART " + str(part_index + 1))

    @staticmethod
    def select_part(event):
        part = event.widget.get()  # 선택된 파트
        print(part)
        # 선택된 파트에 해당하는 인덱스 계산
        part_index = int(part.split()[1]) - 1  # "PART X"에서 X에 해당하는 부분 추출하여 인덱스로 변환
        part_size = 30
        total_words = len(pb.partmodel.dictionary)
        start_index = part_index * part_size
        TestModel.start_idx = start_index
        end_index = min((part_index + 1) * part_size, total_words)

        TestModel.questions.clear()

        # 선택된 파트에 해당하는 단어들을 questions 리스트에 추가
        """for dict in range(start_index, end_index):
            TestModel.questions.append = pb.partmodel.dictionary[dict]
        """
        TestModel.questions = pb.partmodel.dictionary[start_index:end_index]

        print(TestModel.start_idx)
        for q in TestModel.questions:
            print(q)

        # 선택된 파트에 따라 question_num 재설정
        TestModel.question_num = min(end_index - start_index, 30)

# ----------------------------- View -----------------------------
class TestView:
    def __init__(self, root, test_model):
        self.root = root
        self.test_model = test_model
        self.green_boxes = []  # 초록색 박스 저장 리스트
        self.setup_ui()

    # UI 생성 코드
    def setup_ui(self):
        # 콤보박스 생성
        part_combo_box = ttk.Combobox(self.root, values=self.test_model.combo_values)
        part_combo_box.pack(padx=5)
        part_combo_box.bind("<<ComboboxSelected>>", lambda e: self.test_model.select_part(e))

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

        # 문제 개수와 문제에 맞는 박스(초록색) 생성
        for i in range(self.test_model.question_num):
            question = self.test_model.questions[i]
            green_box = self.create_scrollable_text(frame, i + self.test_model.start_idx, question)
            self.green_boxes.append(green_box)  # 초록색 박스 추가

        # 윈도우 실행
        self.root.mainloop()

    # 초록색 박스 생성 함수
    def create_scrollable_text(self, parent_frame, question_num, text):
        def handle_enter(event):  # 입력 상자에서 엔터 키를 눌렀을 때의 동작
            user_input = input_box.get()  # 입력 상자에서 입력된 내용 가져오기
            print("User input:", user_input)  # 입력된 내용을 터미널에 출력하기
            input_box.delete(0, "end")  # 입력 상자 초기화

            if user_input == "correct":  # 입력값이 정답과 동일하다면, 입력상자를 O로 초기화
                input_box.insert(0, "O")
            else:
                input_box.insert(0, "X")

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

        return green_box

    # 문제 갱신 함수
    def update_questions(self):
        for i, question in enumerate(self.test_model.questions):
            # 초록색 박스의 텍스트 업데이트
            text_box = self.green_boxes[i].children['text_box']  # children을 사용하여 text_box 참조 얻기
            text_box.config(state="normal")
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, question)
            text_box.config(state="disabled")

# ----------------------------- Controller -----------------------------
class TestController:
    def __init__(self, root):
        self.model = TestModel()
        self.view = TestView(root, self.model)
        #self.partmodel = partmodel

    def open_testPage_window(self):
        pass
    
        
        
    
"""
if __name__ == "__main__":
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()"""