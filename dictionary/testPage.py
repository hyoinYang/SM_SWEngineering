import tkinter as tk
from tkinter import ttk, messagebox
import part_dict as star
import partbox as pb
import math
from functools import partial

# ----------------------------- Model -----------------------------
import math

class TestModel:
    def __init__(self):
        self.combo_values = []
        self.questions = []
        self.start_idx = 0
        self.part_size = 30
        self.total_words = len(pb.partmodel.dictionary)
        self.num_parts = math.ceil(self.total_words / self.part_size) # 파트 개수  -> 질문 개수가 아님
        self.text_widgets = []
        self.input_box_widgets = []
        for part_index in range(self.num_parts):
            start_index = part_index * self.part_size
            end_index = min((part_index + 1) * self.part_size, self.total_words)
            part_questions = pb.partmodel.dictionary[start_index:end_index]
            self.questions.extend(part_questions)
            self.combo_values.append("PART " + str(part_index + 1))

    #@staticmethod
    def select_part(self,event): # 파트 선택할 때 이벤트 발생
        part = event.widget.get()  # 선택된 파트
        # 선택된 파트에 해당하는 인덱스 계산
        part_index = int(part.split()[1]) - 1  # "PART X"에서 X에 해당하는 부분 추출하여 인덱스로 변환
        start_index = part_index * self.part_size
        self.start_idx = start_index
        end_index = min((part_index + 1) * self.part_size, self.total_words)
        self.question_num = min(end_index - start_index, 30)
        self.questions.clear()

        # 선택된 파트에 해당하는 단어들을 questions 리스트에 추가

        self.questions = pb.partmodel.dictionary[start_index:end_index] # 단어 들어있음

        self.update_questions()
        # 선택된 파트에 따라 question_num 재설정
        self.question_num = min(end_index - start_index, 30) #

    def update_questions(self):
        for i,question,text_box,input_box in zip(list(range(0,len(self.questions))),self.questions,self.text_widgets,self.input_box_widgets):
            text_box.config(state=tk.NORMAL)
            text_box.delete("1.0",tk.END)
            text_box.insert(tk.END, question)
            # 답 업데이트
            input_box.unbind("<Return>")
        # 새로운 이벤트 핸들러 바인딩
            input_box.bind("<Return>", partial(self.handle_enter, input_box = input_box,text=question))
            

    def handle_enter(self,event,input_box,text):  # 입력 상자에서 엔터 키를 눌렀을 때의 동작
        user_input = input_box.get()  # 입력 상자에서 입력된 내용 가져오기
        input_box.delete(0, "end")  # 입력 상자 초기화

        if user_input == text:  # 입력값이 정답과 동일하다면, 입력상자를 O로 초기화
            messagebox.showinfo("단어 테스트","맞았습니다 !")
        else:
            messagebox.showinfo("단어 테스트","틀렸습니다 !")

# ----------------------------- View -----------------------------
class TestView:
    def __init__(self, root, test_model):
        self.root = root
        self.test_model = test_model
        self.green_boxes = []  # 초록색 박스 저장 리스트
        self.text_widgets = [] # textbox 담는 상자
        self.input_box_widgets = []
        self.part_combo_box = ttk.Combobox(self.root, values=self.test_model.combo_values)
        self.part_combo_box.pack(padx=5)
        self.part_combo_box.bind("<<ComboboxSelected>>", lambda e: self.test_model.select_part(e))
        
        # Canvas 생성
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        # 스크롤바 생성
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Canvas에 스크롤바 바인딩
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # 내부 프레임 생성
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((30, 0), window=self.frame, anchor="nw")

        # 내부 프레임의 사이즈 변경 시 Canvas 업데이트
        self.frame.bind("<Configure>", lambda e:self. canvas.configure(scrollregion=self.canvas.bbox("all")))

    # 초록색 박스 세팅
    def setting_green_box(self):
        for i in range(30):
            try:
                question = self.test_model.questions[i]
                self.create_scrollable_text(self.frame, i + self.test_model.start_idx, question)
            except(IndexError): 
                continue

    # 초록색 박스 생성 함수
    def create_scrollable_text(self, parent_frame, question_num, text):
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
        self.text_widgets.append(text_box)
        
        # 입력을 받는 박스 생성 및 배치
        input_box = tk.Entry(green_box, bg="white", fg="black", bd=2)
        input_box.pack(side="top", fill="x", padx=20, pady=10)
        self.input_box_widgets.append(input_box)
        input_box.bind("<Return>", partial(self.handle_enter, input_box = input_box,text=text))  # Enter 키에 대한 이벤트 핸들러 바인딩

    def handle_enter(self,event,input_box,text):  # 입력 상자에서 엔터 키를 눌렀을 때의 동작
        #print(f"{text}에 대한 handle_enter")
        user_input = input_box.get()  # 입력 상자에서 입력된 내용 가져오기
        input_box.delete(0, "end")  # 입력 상자 초기화

        if user_input == text:  # 입력값이 정답과 동일하다면, 입력상자를 O로 초기화
            messagebox.showinfo("단어 테스트","맞았습니다 !")
        else:
            messagebox.showinfo("단어 테스트","틀렸습니다 !")


    def init(self):
        self.setting_green_box()
    
    # 문제 갱신 함수 -> 파트 바꼈을 때 실행시키면 됨

# ----------------------------- Controller -----------------------------
class TestController:
    def __init__(self, root):
        self.model = TestModel()
        self.view = TestView(root, self.model)
        self.view.init()
        self.model.text_widgets = self.view.text_widgets
        self.model.input_box_widgets = self.view.input_box_widgets

"""     
if __name__ == "__main__":
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()"""