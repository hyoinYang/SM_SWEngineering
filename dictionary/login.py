import tkinter as tk
from tkinter import ttk, messagebox
from sidebar import open_sidebar_window

class LoginPage:

    # -------------------------------- 윈도우 생성 --------------------------------
    def __init__(self, root):
        self.root = root
        self.root.title("토익 단어장")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#d9d9d9')
        self.root.geometry("700x550")

        self.setup_ui()

    # -------------------------------- 화면 구성 --------------------------------
    def setup_ui(self):
        self.style.configure('Title.TFrame', background='#838383')
        
        # 회색바 프레임
        title_bar_frame = ttk.Frame(self.root, style='Title.TFrame', height=30)
        title_bar_frame.pack(fill='x', pady=10)
        
        # 톱니바퀴 아이콘
        gear_icon = tk.PhotoImage(file="resource/gear_icon.png").subsample(10)
        gear_button = tk.Label(title_bar_frame, image=gear_icon, relief="flat", bd=0, bg="#838383", cursor="hand2")
        gear_button.image = gear_icon
        gear_button.pack(side="left", padx=5)

        # "토익단어" 텍스트
        text_label = tk.Label(title_bar_frame, text="토익단어", font=("Helvetica", 15), bg="#838383")
        text_label.pack(side="left", padx=5)

        # 사이드바 버튼
        sidebar_icon = tk.PhotoImage(file="dictionary/assets/frame2/title_bar_frame_image/sidebar_icon.png").subsample(10)
        sidebar_button = tk.Button(title_bar_frame, image=sidebar_icon, relief="flat", bd=0, command=lambda:open_sidebar_window(root), bg="#838383", cursor="hand2")
        sidebar_button.image = sidebar_icon
        sidebar_button.pack(side="right", padx=10)

        # 사용자 이름 라벨 및 텍스트 상자
        username_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        username_frame.pack(pady=10)

        username_icon = tk.PhotoImage(file="resource/username_entry.png").subsample(1)
        self.username_label = tk.Label(username_frame, image=username_icon, relief="solid", bd=0, cursor="hand2")
        self.username_label.image = username_icon
        self.username_label.pack(side="left", padx=5)
        
        self.username_entry = tk.Entry(username_frame, relief="flat", bg="#F0F0F0")
        self.username_entry.pack(side="left", padx=5)
        self.username_entry.insert(0, "Username")

        # 비밀번호 라벨 및 텍스트 상자
        password_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        password_frame.pack(pady=10)

        password_icon = tk.PhotoImage(file="resource/password_entry.png").subsample(1)
        self.password_label = tk.Label(password_frame, image=password_icon, relief="flat", bd=0)
        self.password_label.image = password_icon
        self.password_label.pack(side="left", padx=5)
        self.password_entry = tk.Entry(password_frame, relief="flat", bg="#F0F0F0")
        self.password_entry.pack(side="left", padx=5)
        self.password_entry.insert(0, "password")

        # 로그인 버튼
        login_icon = tk.PhotoImage(file="resource/login_btn.png").subsample(2)
        login_button = tk.Button(self.root, image=login_icon, relief="flat", bd=0, command=self.validate_login, cursor="hand2")
        login_button.image = login_icon
  
        login_button.pack(pady=20)

        # 회원가입 버튼
        signup_icon = tk.PhotoImage(file="resource/signup_btn.png").subsample(2)
        signup_button = tk.Button(self.root, image=signup_icon, relief="flat", bd=0, command=self.validate_login, cursor="hand2")
        signup_button.image = signup_icon

        signup_button.pack(pady=10)

    # -------------------------------- 버튼의 이벤트 --------------------------------
    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "12345":
            messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))
        else:
            messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

    def validate_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "12345":
            messagebox.showinfo("로그인 성공", "환영합니다, {}님!".format(username))
        else:
            messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()