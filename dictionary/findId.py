import tkinter as tk
from tkinter import messagebox
from findPassword import Controller as FindController
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from userClass import UserModel

# ----------------------------- Model -----------------------------
class FindModel:
    def validate_find_password(self, root):
        import findPassword as fs

        messagebox.showinfo("아이디 찾기", "비밀번호 찾기 페이지로 이동합니다.")
        
        for widget in root.winfo_children():
            widget.destroy()    

        fs.Controller(root)

    def validate_find_id(name_entry, birth_entry):
        username = name_entry.get()
        birth = birth_entry.get()
        usermodel = UserModel()
        result = usermodel.find_id_by_name_dob(username, birth)
        if (result):
            messagebox.showinfo("아이디:", f"아이디는 {result}입니다.")
        else:
            messagebox.showinfo("아이디 찾기", "존재하지 않는 정보입니다.")


    def get_password(self):
        return self.password_entry.get()

# ----------------------------- View -----------------------------
class FindView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
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
        self.birth_entry.bind("<Return>", lambda e:FindModel.check_id(self.name_entry, self.birth_entry))
        self.birth_entry.insert(0, "생년월일")

        # 아이디 찾기 버튼
        find_id_button = tk.Button(self.root, font=('Helvetica', 10, 'bold'), text="                 아이디 찾기                 ", bg="#838383", relief="flat", bd=0, command=lambda:FindModel.validate_find_id(self.name_entry, self.birth_entry), cursor="hand2")
        find_id_button.pack(pady=10)

        # 비밀번호 찾기 버튼
        find_password_button = tk.Button(self.root, font=('Helvetica', 10, 'bold'), text="               비밀번호 찾기               ", bg="#838383", relief="flat", bd=0, command=lambda:FindModel.validate_find_password(self, self.root), cursor="hand2")

        find_password_button.pack(pady=10)


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