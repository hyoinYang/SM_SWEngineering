from wordDB.db_connection import connect_to_database

class UserModel:
    def __init__(self):
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor()

    def check_duplicate_id(self, user_id):
        check_query = "SELECT id FROM Member WHERE id = %s"
        self.cursor.execute(check_query, (user_id,))
        result = self.cursor.fetchone()
        return result is not None

    def register_member(self, user_id, password, name, dob):
        insert_query = "INSERT INTO Member (id, password, name, dob) VALUES (%s, %s, %s, %s)"
        values = (user_id, password, name, dob)
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def find_id_by_name_dob(self, name, dob):
        find_query = "SELECT id FROM Member WHERE name = %s AND dob = %s"
        self.cursor.execute(find_query, (name, dob))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def find_password_by_id_name_dob(self, user_id, name, dob):
        find_query = "SELECT password FROM Member WHERE id = %s AND name = %s AND dob = %s"
        self.cursor.execute(find_query, (user_id, name, dob))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def login(self, user_id, password):
        login_query = "SELECT name FROM Member WHERE id = %s AND password = %s"
        self.cursor.execute(login_query, (user_id, password))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_all_members(self):
        self.cursor.execute("SELECT * FROM Member")
        return self.cursor.fetchall()

class UserView:
    @staticmethod
    def show_menu():
        print("\n1. 회원가입")
        print("2. 로그인")
        print("3. 아이디 찾기")
        print("4. 비밀번호 찾기")
        print("5. 종료")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_members(members):
        print("회원 목록:")
        for member in members:
            print(f"ID: {member[0]}, 이름: {member[2]}, 생년월일: {member[3]}")

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def main(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("메뉴를 선택하세요: ")

            if choice == '1':
                self.register_member()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.find_id()
            elif choice == '4':
                self.find_password()
            elif choice == '5':
                self.view.display_message("프로그램을 종료합니다.")
                break
            else:
                self.view.display_message("잘못된 입력입니다. 다시 시도하세요.")

    def register_member(self):
        self.view.display_message("회원가입을 시작합니다.")
        user_id = self.view.get_input("아이디를 입력하세요: ")
        while self.model.check_duplicate_id(user_id):
            self.view.display_message("이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.")
            user_id = self.view.get_input("아이디를 입력하세요: ")
        password = self.view.get_input("비밀번호를 입력하세요: ")
        name = self.view.get_input("이름을 입력하세요: ")
        while not name.isalpha():
            self.view.display_message("이름은 문자열로 입력해주세요.")
            name = self.view.get_input("이름을 입력하세요: ")
        dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        while len(dob) != 10 or not dob[0:4].isdigit() or dob[4] != '-' or not dob[5:7].isdigit() or dob[7] != '-' or not dob[8:10].isdigit():
            self.view.display_message("생년월일은 YYYY-MM-DD 형식으로 입력해주세요.")
            dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")

        self.model.register_member(user_id, password, name, dob)
        self.view.display_message("회원가입이 완료되었습니다.")

    def login(self):
        self.view.display_message("로그인을 시작합니다.")
        user_id = self.view.get_input("아이디를 입력하세요: ")
        password = self.view.get_input("비밀번호를 입력하세요: ")
        name = self.model.login(user_id, password)
        if name:
            if name == 'admin':
                self.view.display_message(f"{name}님, 환영합니다!")
                self.view.display_message("관리자 모드로 로그인되었습니다.")
                while True:
                    self.view.display_message("\n1. 회원 목록 보기\n2. 종료")
                    admin_choice = self.view.get_input("관리자 모드 메뉴를 선택하세요: ")
                    if admin_choice == '1':
                        members = self.model.get_all_members()
                        self.view.display_members(members)
                    elif admin_choice == '2':
                        self.view.display_message("프로그램을 종료합니다.")
                        break
                    else:
                        self.view.display_message("잘못된 입력입니다. 다시 시도하세요.")
            else:
                self.view.display_message(f"{name}님, 환영합니다!")
        else:
            self.view.display_message("아이디 또는 비밀번호가 일치하지 않습니다.")

    def find_id(self):
        self.view.display_message("아이디를 찾습니다.")
        name = self.view.get_input("이름을 입력하세요: ")
        dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        while not dob[0:4].isdigit() or not dob[5:7].isdigit() or not dob[8:10].isdigit() or len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
            self.view.display_message("잘못된 생년월일 형식입니다. 다시 입력해주세요.")
            dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        found_id = self.model.find_id_by_name_dob(name, dob)
        if found_id:
            self.view.display_message(f"{name}님의 아이디는 {found_id} 입니다.")
        else:
            self.view.display_message("일치하는 회원 정보가 없습니다.")

    def find_password(self):
        self.view.display_message("비밀번호를 찾습니다.")
        user_id = self.view.get_input("아이디를 입력하세요: ")
        name = self.view.get_input("이름을 입력하세요: ")
        dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        while not dob[0:4].isdigit() or not dob[5:7].isdigit() or not dob[8:10].isdigit() or len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
            self.view.display_message("잘못된 생년월일 형식입니다. 다시 입력해주세요.")
            dob = self.view.get_input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        found_password = self.model.find_password_by_id_name_dob(user_id, name, dob)
        if found_password:
            self.view.display_message(f"{name}님의 비밀번호는 {found_password} 입니다.")
        else:
            self.view.display_message("일치하는 회원 정보가 없습니다.")

if __name__ == "__main__":
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)
    controller.main()
