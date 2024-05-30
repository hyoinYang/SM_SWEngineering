import tkinter as tk
import tkinter as ttk
import random



# gui 구현
class AnswerNoteView:
    def __init__(self,i,frame,model,controller):
        self.i = i # 인덱스
        self.model = model # 전체 db
        self.controller = controller # 각 파트의 controller

        self.white_box = tk.Frame(frame, bg="white",borderwidth=2, relief="ridge") # 단어가 적혀있는 box
        self.green_box = tk.Frame(self.white_box, bg="white",borderwidth=0, relief="ridge") # 단어 뜻, 예문이 적혀있는 box
        self.dictionary_box = tk.Text(self.green_box, height=12,bg="lightgreen",borderwidth=0) # 단어 뜻, 예문

        self.favorites_button_image = tk.PhotoImage(file="resource/favorites_icon.png").subsample(15) # whitebox에 생성될 즐겨찾기 버튼 이미지
        self.favorites_button = tk.Button(self.white_box,image = self.favorites_button_image,
        relief="flat",command=lambda:self.controller.favorites_button_click(self.favorites_button,self.i)) # 즐겨찾기 버튼 생성

        self.sound_button_image = tk.PhotoImage(file="resource/sound_icon.png").subsample(15) # whitebox에 생성될 단어 발음 듣기 버튼 이미지
        self.sound_button = tk.Button(self.white_box,image = self.sound_button_image, 
        relief="flat",command=lambda:controller.sound_button_click(self.sound_button,self.i)) # 단어 발음 듣기 버튼 생성

        self.dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2) # whitebox에 생성될 greenbox 열기 버튼 이미지
        self.dic_button = tk.Button(self.white_box,image = self.dic_button_image,relief="flat",
        command=lambda:self.controller.open_green_box(self.dictionary_box,self.dic_button,self.green_box)) # greenbox 여는 버튼 생성

        self.check_button_image = check_button_image = tk.PhotoImage(file="resource/check_icon.png").subsample(15) # whitebox에 생성될 학습 완료 버튼
        self.check_button = tk.Button(self.white_box,image = check_button_image, relief="flat",
        command=lambda:self.controller.check_button_click(self.check_button,self.i)) # 학습한 단어 버튼 생성

        self.text_box = tk.Text(self.white_box, fg="black", wrap="word", height=4, padx=20, pady=20, borderwidth=0) # 스크롤 가능한 박스 생성
    
        self.random_button = tk.Button(frame,bg="white",text="랜덤",font=("Helvetica", 15),
        command=lambda:self.controller.random_button_click(self.random_button,self.model.wrong_word_texts,self.model.wrong_sentence)) # 랜덤 버튼 생성
        self.sequence_button = tk.Button(frame,bg="white",text="순행",font=("Helvetica", 15),
        command=lambda:self.controller.sequence_button_click(self.sequence_button,self.model.word,self.model.sentence)) # 순행 버튼 생성
    
    # whitebox (단어, 버튼이 있는 box) 위치 설정
    def setting_white_box(self):
        self.white_box.pack(pady=10,fill="x")

    # greenbox(단어 뜻, 예문 있는 box) 위치 설정
    def setting_green_box(self):
        self.green_box.pack(side="bottom",fill="x")
    
    # greenbox에 예문 설정
    def setting_dictionary_box(self):
        self.dictionary_box.insert("end", self.model.wrong_sentence[self.i])
        self.dictionary_box.config(state="disabled")
        self.model.wrong_sentence_class.append(self.dictionary_box)

    # 단어 발음 버튼 위치 설정
    def setting_sound_button(self):
        self.sound_button.image = self.sound_button_image
        self.sound_button.pack(anchor="e",pady = 0)

    # 뜻 여는 버튼 생성
    def setting_dic_button(self):
        self.dic_button.image = self.dic_button_image
        self.dic_button.pack(side="right",anchor="s")

    # 스크롤 가능한 텍스트 박스 생성
    def setting_scrollbar(self):
        self.text_box.insert(tk.END, self.model.wrong_word_texts[self.i])
        self.text_box.config(state="disabled")
        self.text_box.pack(side="top", fill="both", expand=True)
        self.model.wrong_word_class.append(self.text_box)

    # 위 함수 전부 실행
    def init_dict(self):
        self.setting_white_box()
        self.setting_green_box()
        self.setting_dictionary_box()
        self.setting_sound_button()
        self.setting_dic_button()
        self.setting_scrollbar()

    # 순행 버튼 설정
    def setting_random_button(self):
        self.random_button.pack(side="top",anchor="center")

class AnswerNoteController: 
    def __init__(self,root, model,speakmodel):
        self.root = root
        self.model = model 
        self.speak_model = speakmodel
        self.random_index=list(range(0,len(self.model.wrong_word_texts))) # 랜덤 함수에서 사용

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
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def part_event(self): # word, sentence가 이 파트에서 출력할 단어, 예문 리스트
        for i in range(0,len(self.model.wrong_word_texts)): # 오답노트 개수 만큼 반복
            answernote = AnswerNoteView(i,self.frame,self.model,self)
            if i == 0: # 처음에 랜덤 버튼 생성
                answernote.setting_random_button()
            answernote.init_dict() # gui 구현

    # 단어장에서 초록 박스를 버튼으로 여는 함수
    def open_green_box(self,dictionary_box,dic_button,green_box):
        dictionary_box.pack(fill="both", expand=True)
        dic_button_image = tk.PhotoImage(file="resource/button_6.png").subsample(2,2)
        dic_button.config(
            command=lambda:self.close_green_box(dictionary_box,dic_button,green_box),
            image=dic_button_image
        )
        dic_button.image = dic_button_image
        
    # 단어장에서 초록 박스를 버튼으로 닫는 함수
    def close_green_box(self,dictionary_box,dic_button,green_box):
        dic_button_image = tk.PhotoImage(file="resource/button_5.png").subsample(2,2)
        dic_button.config(
            command=lambda:self.open_green_box(dictionary_box,dic_button,green_box),
            image=dic_button_image
        )
        dic_button.image = dic_button_image
        dictionary_box.pack_forget()
        green_box.config(height=1)
        
    # 단어장에서 랜덤 버튼 클릭
    def random_button_click(self,sequence_button,word,sentence): # dic_list는 한 파트에 들어갈 단어
        random.shuffle(self.random_index)
        for new_text,new_sentence,i in zip(self.model.wrong_word_class,self.model.wrong_sentence_class,self.random_index):
            new_text.config(state=tk.NORMAL)
            new_sentence.config(state=tk.NORMAL)
            new_text.delete("1.0",tk.END)
            new_sentence.delete("1.0",tk.END)
            new_text.insert(tk.END,word[self.random_index[i]])
            new_sentence.insert(tk.END,sentence[self.random_index[i]])
            sequence_button.config(text="순행",command=lambda:self.sequence_button_click(sequence_button,word,sentence))

    # 단어장에서 순행 버튼 클릭
    def sequence_button_click(self,sequence_button,word,sentence):
        index = list(range(0,10))
        for new_text,new_sentence,i in zip(self.model.wrong_word_class,self.model.wrong_sentence_class,index):
            new_text.config(state=tk.NORMAL)
            new_sentence.config(state=tk.NORMAL)
            new_text.delete("1.0",tk.END)
            new_sentence.delete("1.0",tk.END)
            new_text.insert(tk.END,word[i])
            new_sentence.insert(tk.END,sentence[i])

        sequence_button.config(text="랜덤",command=lambda:self.random_button_click(sequence_button,word,sentence))

    # 단어 발음 버튼
    def sound_button_click(self,sound_button,i):
        sound_button.config(bg="red")
        sound_button.after(1000,lambda:sound_button.config(bg="SystemButtonFace"))
        word = self.model.wrong_word_class[i].get("1.0",tk.END).replace("\n","")
        self.speak_model.init_speak(word)


