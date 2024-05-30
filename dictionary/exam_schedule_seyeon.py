import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from examInfoClass import ExamDBModel


class TOEICScheduleModel:
    examDB=ExamDBModel()
    exam_info=examDB.get_exam_info()

    def __init__(self):
        pass

class TOEICScheduleView:
    def __init__(self, root):
        self.root = root
        self.create_schedule_table()

    def create_schedule_table(self):
        root = self.root
        self.tree = ttk.Treeview(root, columns=("일정", "접수기간", "성적발표"), show="headings")
        self.tree.heading("일정", text="일정")
        self.tree.heading("접수기간", text="접수기간")
        self.tree.heading("성적발표", text="성적발표")

        self.tree.pack(pady=20)

        # 트리뷰이 스타일 설정
        self.tree.style = ttk.Style()
        self.tree.style.configure("Treeview.Item", background="#FFFFFF")  # 아이템 배경색
        self.tree.style.configure("Treeview.Heading", background="#FFFFFF", foreground="#000000", font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
        self.tree.style.configure("Treeview.Separator")  # 구분선 배경색

        # 트리뷰이 열 너비 설정 및 구분선 추가
        self.tree.column("일정", width=200, anchor="center")
        self.tree.column("접수기간", width=200, anchor="center")
        self.tree.column("성적발표", width=200, anchor="center")

        # 트리뷰이 스타일 설정: 구분선 색상 및 두께 조정
        self.tree.style.configure("Treeview.Separator", background="#FFFFFF", foreground="#FFFFFF", thickness=0)

        # 트리뷰의 행 높이 설정
        self.tree.style.configure("Custom.Treeview", rowheight=30)  # 행 높이를 30으로 설정
        self.tree.configure(style="Custom.Treeview")

        self.tree.insert("", tk.END, values=("", ""))
        for info in TOEICScheduleModel.exam_info:
            self.tree.insert("", tk.END, values=list(info.values()))
            self.tree.insert("", tk.END, values=("─" * 100, "─" * 100, "─" * 100))

class TOEICScheduleController:
    def __init__(self, root):
        self.model = TOEICScheduleModel
        self.view = TOEICScheduleView(root)


    def run(self):
        self.view.mainloop()
