import mysql.connector

# Establishing a connection to MySQL
mydb = mysql.connector.connect(
  host="DESKTOP-VNK1SEU",
  user="smu",
  password="1310",
  database="smu_db"
)

mycursor = mydb.cursor()

# Create a table for storing member information if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS members (id VARCHAR(255) PRIMARY KEY, password VARCHAR(255), name VARCHAR(255), dob VARCHAR(10))")

class Member:
    def __init__(self, id, password, name, dob):
        self.id = id
        self.password = password
        self.name = name
        self.dob = dob

def check_duplicate_id(id):
    mycursor.execute("SELECT * FROM members WHERE id = %s", (id,))
    if mycursor.fetchone():
        return True
    return False

def register_member():
    print("회원가입을 시작합니다.")
    while True:
        id = input("아이디를 입력하세요: ")
        if check_duplicate_id(id):
            print("이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.")
        else:
            break

    password = input("비밀번호를 입력하세요: ")

    while True:
        name = input("이름을 입력하세요: ")
        if not name.isalpha():
            print("이름은 문자만 입력해주세요.")
        else:
            break

    while True:
        dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        if len(dob) != 10 or not dob[0:4].isdigit() or not dob[5:7].isdigit() or not dob[8:].isdigit() or dob[4] != '-' or dob[7] != '-':
            print("올바른 생년월일 형식을 입력해주세요.")
        else:
            break

    sql = "INSERT INTO members (id, password, name, dob) VALUES (%s, %s, %s, %s)"
    val = (id, password, name, dob)
    mycursor.execute(sql, val)
    mydb.commit()

    print("회원가입이 완료되었습니다.")

def find_id_by_name_dob():
    print("아이디를 찾습니다.")
    name = input("이름을 입력하세요: ")
    dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

    mycursor.execute("SELECT id FROM members WHERE name = %s AND dob = %s", (name, dob))
    result = mycursor.fetchone()

    if result:
        print(f"{name}님의 아이디는 {result[0]} 입니다.")
    else:
        print("일치하는 회원 정보가 없습니다.")

def find_password_by_id_name_dob():
    print("비밀번호를 찾습니다.")
    id = input("아이디를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

    mycursor.execute("SELECT password FROM members WHERE id = %s AND name = %s AND dob = %s", (id, name, dob))
    result = mycursor.fetchone()

    if result:
        print(f"{name}님의 비밀번호는 {result[0]} 입니다.")
    else:
        print("일치하는 회원 정보가 없습니다.")

def main():
    while True:
        print("\n1. 회원가입")
        print("2. 아이디 찾기")
        print("3. 비밀번호 찾기")
        print("4. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            register_member()
        elif choice == '2':
            find_id_by_name_dob()
        elif choice == '3':
            find_password_by_id_name_dob()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
