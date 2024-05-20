# login.py

from wordDB.db_connection import connect_to_database

mydb = connect_to_database()
mycursor = mydb.cursor()

# 로그인 상태를 저장할 전역 변수
logged_in_user = None

# Member 테이블 생성 쿼리
create_table_query = """
CREATE TABLE IF NOT EXISTS Member (
    id VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    name VARCHAR(255),
    dob DATE
)
"""

# 테이블 생성
mycursor.execute(create_table_query)

class Member:
    def __init__(self, id, password, name, dob):
        self.id = id
        self.password = password
        self.name = name
        self.dob = dob

def check_duplicate_id(id):
    check_query = "SELECT id FROM Member WHERE id = %s"
    mycursor.execute(check_query, (id,))
    result = mycursor.fetchone()
    return result is not None

def register_member(member):
    insert_query = "INSERT INTO Member (id, password, name, dob) VALUES (%s, %s, %s, %s)"
    values = (member.id, member.password, member.name, member.dob)
    mycursor.execute(insert_query, values)
    mydb.commit()

def find_id_by_name_dob(name, dob):
    find_query = "SELECT id FROM Member WHERE name = %s AND dob = %s"
    mycursor.execute(find_query, (name, dob))
    result = mycursor.fetchone()
    return result[0] if result else None

def find_password_by_id_name_dob(id, name, dob):
    find_query = "SELECT password FROM Member WHERE id = %s AND name = %s AND dob = %s"
    mycursor.execute(find_query, (id, name, dob))
    result = mycursor.fetchone()
    return result[0] if result else None

def login(id, password):
    login_query = "SELECT name FROM Member WHERE id = %s AND password = %s"
    mycursor.execute(login_query, (id, password))
    result = mycursor.fetchone()
    if result:
        return result[0]
    elif id == 'admin' and password == 'admin':
        return 'admin'
    else:
        return None

def main():
    global logged_in_user
    while True:
        print("\n1. 회원가입")
        print("2. 로그인")
        print("3. 아이디 찾기")
        print("4. 비밀번호 찾기")
        print("5. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            print("회원가입을 시작합니다.")
            id = input("아이디를 입력하세요: ")
            while check_duplicate_id(id):
                print("이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.")
                id = input("아이디를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            name = input("이름을 입력하세요: ")
            while not name.isalpha():
                print("이름은 문자열로 입력해주세요.")
                name = input("이름을 입력하세요: ")
            dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
            while len(dob) != 10 or not dob[0:4].isdigit() or dob[4] != '-' or not dob[5:7].isdigit() or dob[7] != '-' or not dob[8:10].isdigit():
                print("생년월일은 YYYY-MM-DD 형식으로 입력해주세요.")
                dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

            new_member = Member(id, password, name, dob)
            register_member(new_member)
            print("회원가입이 완료되었습니다.")
        elif choice == '2':
            print("로그인을 시작합니다.")
            id = input("아이디를 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            name = login(id, password)
            if name:
                logged_in_user = id
                if name == 'admin':
                    print(f"{name}님, 환영합니다!")
                    print("관리자 모드로 로그인되었습니다.")
                    while True:
                        print("\n1. 회원 목록 보기")
                        print("2. 종료")
                        admin_choice = input("관리자 모드 메뉴를 선택하세요: ")
                        if admin_choice == '1':
                            print("회원 목록:")
                            mycursor.execute("SELECT * FROM Member")
                            for member in mycursor:
                                print(f"ID: {member[0]}, 이름: {member[2]}, 생년월일: {member[3]}")
                        elif admin_choice == '2':
                            print("프로그램을 종료합니다.")
                            break
                        else:
                            print("잘못된 입력입니다. 다시 시도하세요.")
                else:
                    print(f"{name}님, 환영합니다!")
            else:
                print("아이디 또는 비밀번호가 일치하지 않습니다.")
        elif choice == '3':
            print("아이디를 찾습니다.")
            name = input("이름을 입력하세요: ")
            dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
            while not dob[0:4].isdigit() or not dob[5:7].isdigit() or not dob[8:10].isdigit() or len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
                print("잘못된 생년월일 형식입니다. 다시 입력해주세요.")
                dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
            found_id = find_id_by_name_dob(name, dob)
            if found_id:
                print(f"{name}님의 아이디는 {found_id} 입니다.")
            else:
                print("일치하는 회원 정보가 없습니다.")
        elif choice == '4':
            print("비밀번호를 찾습니다.")
            id = input("아이디를 입력하세요: ")
            name = input("이름을 입력하세요: ")
            dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
            while not dob[0:4].isdigit() or not dob[5:7].isdigit() or not dob[8:10].isdigit() or len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
                print("잘못된 생년월일 형식입니다. 다시 입력해주세요.")
                dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
            found_password = find_password_by_id_name_dob(id, name, dob)
            if found_password:
                print(f"{name}님의 비밀번호는 {found_password} 입니다.")
            else:
                print("일치하는 회원 정보가 없습니다.")
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
