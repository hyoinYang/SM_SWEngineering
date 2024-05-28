from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#from word_managing_page import ManagementController
from exam_place_seyeon import EtsPlaceController

import partbox as pb

# 파일 경로가 모두 resource 로 간소화됐기 때문에 아래 코드는 필요 없을 것 같아 주석처리했습니다. 나중에 처리해야함!!!!!!!!!!
"""
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./resource")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

"""
# ----------------------------- View -----------------------------
class SidebarView:
    def __init__(self, root):
        self.root = root
        self.toggle_btn = None  # toggle_btn을 클래스 속성으로 지정
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry('700x550')
        self.root.title('Admin')
        self.root.configure(background="#FFFFFF")

        
        head_frame = tk.Frame(self.root, bg='#838383', highlightbackground='white', highlightthickness=1)
        head_frame.pack(side=tk.TOP, fill=tk.X)
        self.toggle_btn = tk.Button(head_frame, text='≡', bg='#838383', fg='black', font=('Bold, 40'), bd=0, activebackground='#838383', activeforeground='black', cursor='hand2', command=self.toggle_menu)
        self.toggle_btn.pack(side=tk.RIGHT)

        """
        title_lb=tk.Label(head_frame, text='토익 시험 일정', bg='#838383', fg='black', font=('Helvetica', 15, 'bold'), bd=0)
        title_lb.pack(side='left', padx=5)

        head_frame.pack(side=tk.TOP, fill=tk.X)
        head_frame.pack_propagate(False)
        head_frame.configure(height=50)"""

        self.toggle_menu()  # toggle_menu를 호출할 때 toggle_btn을 사용하도록 변경
        self.root.mainloop()

    def toggle_menu(self):
        if hasattr(self, 'toggle_menu_fm'):
            self.toggle_menu_fm.destroy()  # 이전의 toggle_menu_fm이 있다면 파괴

        self.toggle_menu_fm=tk.Frame(self.root, bg='#838383')

        toggle_btn1 = tk.Button(self.toggle_menu_fm, text='단어장', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2', command=lambda:SidebarController.validate_word(root))
        toggle_btn1.pack(anchor='center')

        canvas1 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas1.pack()
        canvas1.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn2 = tk.Button(self.toggle_menu_fm, text='단어 테스트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn2.pack(anchor='center')

        canvas2 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas2.pack()
        canvas2.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn3 = tk.Button(self.toggle_menu_fm, text='오답노트', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn3.pack(anchor='center')

        canvas3 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas3.pack()
        canvas3.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn4 = tk.Button(self.toggle_menu_fm, text='토익 시험 날짜', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn4.pack(anchor='center')

        canvas4 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas4.pack()
        canvas4.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn5 = tk.Button(self.toggle_menu_fm, text='토익 고사장 안내', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn5.pack(anchor='center')

        canvas5 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas5.pack()
        canvas5.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn6 = tk.Button(self.toggle_menu_fm, text='시험 점수 조회', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn6.pack(anchor='center')

        canvas6 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas6.pack()
        canvas6.create_line(0, 0, 300, 0, fill='gray')

        toggle_btn7 = tk.Button(self.toggle_menu_fm, text='로그아웃', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
        toggle_btn7.pack(anchor='center')

        canvas7 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
        canvas7.pack()
        canvas7.create_line(0, 0, 300, 0, fill='gray')

        # 관리자 전용 기능을 추가합니다. 사용자가 관리자일 경우에만 보입니다.
        if SidebarController.is_admin:
            canvas7 = tk.Canvas(self.toggle_menu_fm, width=300, height=2, highlightthickness=0, bg='black')
            canvas7.pack()
            canvas7.create_line(0, 0, 300, 0, fill='gray')

            toggle_btn7 = tk.Button(self.toggle_menu_fm, text='관리자 전용 기능', font=('Helvetica', 15, 'bold'), bd=0, bg='#838383', fg='black', activebackground='#838383', activeforeground='black', cursor='hand2')
            toggle_btn7.pack(anchor='center')

        window_height= 700
        menu_width = 300
        window_width = self.root.winfo_width()

        x_position = window_width - menu_width

        self.toggle_menu_fm.place(x=x_position, y=50, height=window_height, width=menu_width)

        self.toggle_btn.config(text='≡', font=('Bold, 40'), command=self.collapse_toggle_menu)

    def collapse_toggle_menu(self):
        self.toggle_menu_fm.destroy()
        self.toggle_btn.config(text='≡', command=self.toggle_menu)
        

class SidebarController:
    is_admin = True 
    def __init__(self, root):
        self.view = SidebarView(root)

    def validate_word(root):
        dictionarymaincontroller = pb.DictionaryMainController(root,pb.partmodel)
        dictionarymaincontroller.init()

"""
root = tk.Tk()
controller = SidebarController(root)
root.mainloop()
"""


if __name__ == "__main__":
    root = tk.Tk()
    app = SidebarController(root)
    """
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    """
    root.mainloop()