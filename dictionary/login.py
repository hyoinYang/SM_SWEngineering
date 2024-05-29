from titlebar import TitleView
import tkinter as tk
from tkinter import ttk, messagebox
from signup import SignupController

# ----------------------------- Model -----------------------------
class LoginModel:
    def validate_login(self, username, password):
        if username == "admin" and password == "12345":
            messagebox.showinfo("로그인", "%s님 환영합니다", username)
        else:
            messagebox.showinfo("로그인", "누구세요?")
    
    def validate_signup(self, root):
        messagebox.showinfo("회원가입", "회원가입 창으로 이동합니다")

        for widget in root.winfo_children():
            widget.destroy()

        SignupController(root)

# ----------------------------- View -----------------------------
class LoginView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        #title = TitleView(self.root, "로그인")
        #title.init_title()

        # 사용자 이름 라벨 및 텍스트 상자
        username_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        username_frame.pack(pady = 10)

        username_icon = tk.PhotoImage(file="resource/username_entry.png").subsample(10)
        self.username_label = tk.Label(username_frame, image=username_icon, relief="solid", bd=0, cursor="hand2")
        self.username_label.image = username_icon
        self.username_label.pack(side="left", padx=5)
        
        self.username_entry = tk.Entry(username_frame, relief="flat", bg="#F0F0F0")
        self.username_entry.pack(side="left", padx=5)
        self.username_entry.insert(0, "Username")

        # 비밀번호 라벨 및 텍스트 상자
        password_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        password_frame.pack(pady=10)

        password_icon = tk.PhotoImage(file="resource/password_entry.png").subsample(37)
        self.password_label = tk.Label(password_frame, image=password_icon, relief="flat", bd=0)
        self.password_label.image = password_icon
        self.password_label.pack(side="left", padx=5)
        self.password_entry = tk.Entry(password_frame, relief="flat", bg="#F0F0F0")
        self.password_entry.pack(side="left", padx=5)
        self.password_entry.insert(0, "password")

        # 로그인 버튼
        login_icon = tk.PhotoImage(file="resource/login_btn.png").subsample(2)
        login_button = tk.Button(self.root, image=login_icon, relief="flat", bd=0, command=lambda:LoginModel.validate_login(self, "testid", "testpass"), cursor="hand2")
        login_button.image = login_icon
  
        login_button.pack(pady=20)

        # 회원가입 버튼
        signup_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
        signup_button = tk.Button(self.root, image=signup_icon, relief="flat", bd=0, command=lambda:LoginModel.validate_signup(self, self.root), cursor="hand2")
        signup_button.image = signup_icon

        signup_button.pack(pady=10)

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()

    def show_login_success_message(self, username):
        messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))

    def show_login_failure_message(self):
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

# ----------------------------- Controller -----------------------------
class LoginController:
    def __init__(self, root):
        self.model = LoginModel()
        self.view = LoginView(root)
        #self.bind_events()

    def validate_login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        if self.model.validate_login(username, password):
            self.view.show_login_success_message(username)
        else:
            self.view.show_login_failure_message()
    
    def handle_btn1_click(root):
        pass

"""if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    my_windows_width = root.winfo_screenwidth()
    my_windows_height = root.winfo_screenheight()
    app_width = 700
    app_height = 550
    center_width = (my_windows_width/2)-(app_width/2)
    center_height = (my_windows_height/2)-(app_height/2)
    root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")
    root.mainloop()"""
