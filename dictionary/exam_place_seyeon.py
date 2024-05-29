from titlebar import TitleView
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# ----------------------------- Model -----------------------------
class EtsPlaceModel:
    
    ets_icon_path = "resource/ets.png"
    member_login_icon_path = "resource/member_login_icon.png"
    non_member_login_icon_path = "resource/non_member_login_icon.png"

    def __init__(self):
        self.urls = {
            "exam_place": "https://m.exam.toeic.co.kr/receipt/centerMap.php",
            "member_login": "https://www.ybmnet.co.kr/common/login.asp?url=%2Fcommon%2FcertifyResponse.php%3FreturnUrl%3D%2Freceipt%2FconfirmList.php&what=m.exam.toeic.co.kr",
            "non_member_login": "https://certify.ybmnet.co.kr/common/certiModuleExam/certify_step1.asp?returnUrl=https%3A%2F%2Fm.exam.toeic.co.kr%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php&loginWhat=m.exam.toeic.co.kr&loginUrl=%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php"
        }

# ----------------------------- View -----------------------------
class EtsPlaceView:
    def __init__(self, root):
        self.root = root
        self.setup_gui()
    
    def setup_gui(self):
        self.ets_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.ets_icon_path))
        self.member_login_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.member_login_icon_path))
        self.non_member_login_icon = ImageTk.PhotoImage(Image.open(EtsPlaceModel.non_member_login_icon_path))

        self.ets_button = tk.Button(self.root, image=self.ets_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
        self.ets_button.pack(pady=(20, 0))

        self.ets_label = tk.Label(self.root, text="[ 고사장 조회 ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
        self.ets_label.pack(pady=(0, 30))

        self.member_login_button = tk.Button(self.root, image=self.member_login_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
        self.member_login_button.pack()

        self.member_login_label = tk.Label(self.root, text="[ 회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
        self.member_login_label.pack(pady=(0, 30))

        self.non_member_login_button = tk.Button(self.root, image=self.non_member_login_icon, borderwidth=0, bg="#FFFFFF", cursor="hand2")
        self.non_member_login_button.pack()

        self.non_member_login_label = tk.Label(self.root, text="[ 비회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
        self.non_member_login_label.pack()
    
    def setup_menu(self):
        self.menu.add_command(label="                   단어장                 ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="                 단어 테스트               ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="                  오답노트                 ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="               토익 시험 날짜               ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="              토익 고사장 안내              ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="               시험 점수 조회               ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        for _ in range(9):
            self.menu.add_command(label=" ", font=("Helvetica", 15, "bold"))
        self.menu.add_separator()
        self.menu.add_command(label="                  로그아웃                  ", font=("Helvetica", 15, "bold"))
    
    def show_menu(self, event):
        x = self.root.winfo_x() + self.title_bar_frame.winfo_width() - 355  # 메뉴가 표시될 x 좌표
        y = self.root.winfo_y() + self.title_bar_frame.winfo_height() + 30  # 메뉴가 표시될 y 좌표
        self.menu.post(x, y)

# ----------------------------- Controller -----------------------------
class EtsPlaceController:
    def __init__(self, root):
        self.model = EtsPlaceModel()
        self.view = EtsPlaceView(root)
        self.bind_events()
    
    def bind_events(self):
        self.view.ets_button.config(command=self.open_link)
        self.view.member_login_button.config(command=self.open_member_login_link)
        self.view.non_member_login_button.config(command=self.open_non_member_login_link)
    
    def open_link(self):
        webbrowser.open(self.model.urls["exam_place"])
    
    def open_member_login_link(self):
        webbrowser.open(self.model.urls["member_login"])
    
    def open_non_member_login_link(self):
        webbrowser.open(self.model.urls["non_member_login"])

# ----------------------------- Main -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = EtsPlaceController(root)
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    root.mainloop()