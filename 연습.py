class Member:
    def __init__(self, id, password, name, dob):
        self.id = id
        self.password = password
        self.name = name
        self.dob = dob

# 관리자 계정 정보 설정
ADMIN_ID = "admin"
ADMIN_PASSWORD = "admin"

def check_duplicate_id(id, members):
    for member in members:
        if member.id == id:
            return True
    return False

def register_member(members):
    print("회원가입을 시작합니다.")
    while True:
        id = input("아이디를 입력하세요: ")
        if check_duplicate_id(id, members):
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
        if not dob.replace("-", "").isdigit():
            print("생년월일은 숫자와 '-'만 입력해주세요.")
        else:
            break

    member = Member(id, password, name, dob)
    return member

def find_id_by_name_dob(members):
    print("아이디를 찾습니다.")
    name = input("이름을 입력하세요: ")
    dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

    found = False
    for member in members:
        if member.name == name and member.dob == dob:
            print(f"{name}님의 아이디는 {member.id} 입니다.")
            found = True
            break

    if not found:
        print("일치하는 회원 정보가 없습니다.")

def find_password_by_id_name_dob(members):
    print("비밀번호를 찾습니다.")
    id = input("아이디를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    dob = input("생년월일을 입력하세요 (YYYY-MM-DD): ")

    found = False
    for member in members:
        if member.id == id and member.name == name and member.dob == dob:
            print(f"{name}님의 비밀번호는 {member.password} 입니다.")
            found = True
            break

    if not found:
        print("일치하는 회원 정보가 없습니다.")

def login(members):
    print("로그인을 시작합니다.")
    id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    if id == ADMIN_ID and password == ADMIN_PASSWORD:
        print("관리자 모드로 로그인되었습니다.")
        return "admin"  # 관리자 모드로 로그인된 것을 표시하기 위한 문자열 반환
    else:
        for member in members:
            if member.id == id and member.password == password:
                print(f"{member.name}님, 환영합니다!")
                return "user"  # 일반 사용자 모드로 로그인된 것을 표시하기 위한 문자열 반환
        print("아이디 또는 비밀번호가 일치하지 않습니다.")

def load_members_from_file():
    members = []
    try:
        with open('members.txt', 'r') as f:
            for line in f:
                id, password, name, dob = line.strip().split(',')
                members.append(Member(id, password, name, dob))
    except FileNotFoundError:
        pass  # 파일이 없는 경우 무시
    return members

def main():
    members = load_members_from_file()
    logged_in_as_admin = False

    while True:
        if logged_in_as_admin:
            print("\n1. 회원 목록 보기")
            print("2. 종료")
        else:
            print("\n1. 회원가입")
            print("2. 로그인")
            print("3. 아이디 찾기")
            print("4. 비밀번호 찾기")
            print("5. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1' and not logged_in_as_admin:
            member = register_member(members)
            members.append(member)
            print("회원가입이 완료되었습니다.")
        elif choice == '2' and not logged_in_as_admin:
            user_type = login(members)
            if user_type == "admin":
                logged_in_as_admin = True
        elif choice == '3' and not logged_in_as_admin:
            find_id_by_name_dob(members)
        elif choice == '4' and not logged_in_as_admin:
            find_password_by_id_name_dob(members)
        elif choice == '5' and not logged_in_as_admin:
            print("프로그램을 종료합니다.")
            break
        elif choice == '1' and logged_in_as_admin:  
            print("회원 목록:")
            for member in members:
                print(f"ID: {member.id}, 이름: {member.name}, 생년월일: {member.dob}")
        elif choice == '2' and logged_in_as_admin:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()