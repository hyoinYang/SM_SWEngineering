import tkinter as tk
from tkinter import messagebox
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from userClass import UserModel


# ----------------------------- Model -----------------------------
class SignupModel:
    def validate_signup(root, username_entry, password_entry, birth_entry, name_entry):
        import login as loginPage
        usermodel = UserModel()
        
        username = username_entry.get()
        password = password_entry.get()
        birth = birth_entry.get()
        name = name_entry.get()
        print(username, password, birth, name)
        if (usermodel.check_duplicate_id(username)):
            messagebox.showinfo("회원가입", "이 아이디는 사용되고 있습니다.")
        else:
            usermodel.register_member(username, password, name, birth)
            messagebox.showinfo("회원가입", "회원가입 완료")
            
            for fm in root.winfo_children():
                fm.destroy()
                root.update()

            login_fm=tk.Frame(root)
            login_fm.pack(fill=tk.BOTH, expand=True)
            controller = loginPage.LoginController(login_fm)


# ----------------------------- View -----------------------------
class SignupView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):

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

        # 이름 라벨 및 텍스트 상자
        name_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        name_frame.pack(pady=10)

        name_icon = tk.PhotoImage(file="resource/name_entry.png").subsample(4)
        self.name_label = tk.Label(name_frame, image=name_icon, relief="flat", bd=0)
        self.name_label.image = name_icon
        self.name_label.pack(side="left", padx=5)
        self.name_entry = tk.Entry(name_frame, relief="flat", bg="#F0F0F0")
        self.name_entry.pack(side="left", padx=5)
        self.name_entry.insert(0, "이름")

        # 생년월일 라벨 및 텍스트 상자
        birth_frame = tk.Frame(self.root, relief="solid", borderwidth=1, highlightbackground="gray", highlightcolor="gray")
        birth_frame.pack(pady=10)

        birth_icon = tk.PhotoImage(file="resource/email_entry.png").subsample(24)
        self.birth_label = tk.Label(birth_frame, image=birth_icon, relief="flat", bd=0)
        self.birth_label.image = birth_icon
        self.birth_label.pack(side="left", padx=5)
        self.birth_entry = tk.Entry(birth_frame, relief="flat", bg="#F0F0F0")
        self.birth_entry.pack(side="left", padx=5)
        self.birth_entry.insert(0, "생년월일")

        # 회원가입 버튼
        signup_button = tk.Button(self.root, font=('Helvetica', 15, 'bold'), text="               회원가입               ", bg="#838383", relief="flat", bd=0, command=lambda:SignupModel.validate_signup(self.root, self.username_entry, self.password_entry, self.birth_entry, self.name_entry), cursor="hand2")

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