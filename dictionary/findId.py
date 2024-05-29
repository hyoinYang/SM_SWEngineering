from titlebar import TitleView
import tkinter as tk
from tkinter import ttk, messagebox
from findPassword import Controller as FindController

# ----------------------------- Model -----------------------------
class FindModel:
    def validate_find_password(self):
        messagebox.showinfo("아이디 찾기", "비밀번호 찾기 페이지로 이동합니다.")
        FindController(self)

    def validate_find_id(self):
        messagebox.showinfo("아이디 찾기", "아이디는 ####입니다.")

# ----------------------------- View -----------------------------
class FindView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        title = TitleView(self.root, "아이디 찾기")
        title.init_title()

        # 이름 라벨 및 텍스트 상자
        name_frame = tk.Frame(title.canvas, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        name_frame.pack(pady=10)

        name_icon = tk.PhotoImage(file="resource/name_entry.png").subsample(4)
        self.name_label = tk.Label(name_frame, image=name_icon, relief="flat", bd=0)
        self.name_label.image = name_icon
        self.name_label.pack(side="left", padx=5)
        self.name_entry = tk.Entry(name_frame, relief="flat", bg="#F0F0F0")
        self.name_entry.pack(side="left", padx=5)
        self.name_entry.insert(0, "이름")

        # 생년월일 라벨 및 텍스트 상자
        birth_frame = tk.Frame(title.canvas, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        birth_frame.pack(pady=10)

        email_icon = tk.PhotoImage(file="resource/email_entry.png").subsample(24)
        self.email_label = tk.Label(birth_frame, image=email_icon, relief="flat", bd=0)
        self.email_label.image = email_icon
        self.email_label.pack(side="left", padx=5)
        self.email_entry = tk.Entry(birth_frame, relief="flat", bg="#F0F0F0")
        self.email_entry.pack(side="left", padx=5)
        self.email_entry.insert(0, "생년월일")

        # 아이디 찾기 버튼
        find_id_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
        find_id_button = tk.Button(title.canvas, text="                 아이디 찾기                 ", bg="#838383", relief="flat", bd=0, command=lambda:FindModel.validate_find_id(self), cursor="hand2")
        find_id_button.image = find_id_icon

        find_id_button.pack(pady=10)

        # 비밀번호 찾기 버튼
        find_password_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
        find_password_button = tk.Button(title.canvas, text="                 비밀번호 찾기                 ", bg="#838383", relief="flat", bd=0, command=lambda:FindModel.validate_find_password(self), cursor="hand2")
        find_password_button.image = find_password_icon

        find_password_button.pack(pady=10)

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()


# ----------------------------- Controller -----------------------------
class FindController:
    def __init__(self, root):
        self.root = root
        self.model = FindModel()
        self.view = FindView(root)
        root.mainloop()
        #self.bind_events()

    def validate_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        if self.model.validate_login(username, password):
            self.view.show_login_success_message(username)
        else:
            self.view.show_login_failure_message()

if __name__ == "__main__":
    root = tk.Tk()
    app = FindController(root)
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")

