from titlebar import TitleView
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------- Model -----------------------------
class SignupModel:
    def validate_signup(self):
        messagebox.showinfo("회원가입", "회원가입 완료")

# ----------------------------- View -----------------------------
class SignupView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        title = TitleView(self.root, "회원가입")
        title.init_title()

        # 사용자 이름 라벨 및 텍스트 상자
        username_frame = tk.Frame(title.canvas, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        username_frame.pack(pady = 10)

        username_icon = tk.PhotoImage(file="resource/username_entry.png").subsample(10)
        self.username_label = tk.Label(username_frame, image=username_icon, relief="solid", bd=0, cursor="hand2")
        self.username_label.image = username_icon
        self.username_label.pack(side="left", padx=5)
        
        self.username_entry = tk.Entry(username_frame, relief="flat", bg="#F0F0F0")
        self.username_entry.pack(side="left", padx=5)
        self.username_entry.insert(0, "Username")

        # 비밀번호 라벨 및 텍스트 상자
        password_frame = tk.Frame(title.canvas, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        password_frame.pack(pady=10)

        password_icon = tk.PhotoImage(file="resource/password_entry.png").subsample(37)
        self.password_label = tk.Label(password_frame, image=password_icon, relief="flat", bd=0)
        self.password_label.image = password_icon
        self.password_label.pack(side="left", padx=5)
        self.password_entry = tk.Entry(password_frame, relief="flat", bg="#F0F0F0")
        self.password_entry.pack(side="left", padx=5)
        self.password_entry.insert(0, "password")

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

        # 이메일 라벨 및 텍스트 상자
        email_frame = tk.Frame(title.canvas, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        email_frame.pack(pady=10)

        email_icon = tk.PhotoImage(file="resource/email_entry.png").subsample(24)
        self.email_label = tk.Label(email_frame, image=email_icon, relief="flat", bd=0)
        self.email_label.image = email_icon
        self.email_label.pack(side="left", padx=5)
        self.email_entry = tk.Entry(email_frame, relief="flat", bg="#F0F0F0")
        self.email_entry.pack(side="left", padx=5)
        self.email_entry.insert(0, "생년월일")

        # 회원가입 버튼
        signup_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
        signup_button = tk.Button(title.canvas, image=signup_icon, relief="flat", bd=0, command=lambda:SignupModel.validate_signup(self), cursor="hand2")
        signup_button.image = signup_icon

        signup_button.pack(pady=10)

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()

# ----------------------------- Controller -----------------------------
class SignupController:
    def __init__(self, root):
        self.root = root

        #self.model = SignupModel()
        self.view = SignupView(root)
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
    app = SignupController(root)

    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    root.mainloop()