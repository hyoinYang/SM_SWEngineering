import mysql.connector
from db_connection import connect_to_database
from wordExist import check_word_exist

# MySQL 연결
mydb = connect_to_database()

def add_word():
    # 단어와 의미 입력 받기
    word = input("추가할 단어를 입력하세요: ")
    meaning = input("단어의 의미를 입력하세요: ")

    if check_word_exist(word):
        print("이미 데이터베이스에 존재하는 단어입니다.")
        return

    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "INSERT INTO words (eng_word, kor_word) VALUES (%s, %s)"
        val = (word, meaning)
        cursor.execute(sql, val)

        # 변경사항을 커밋
        mydb.commit()

        print("단어가 성공적으로 추가되었습니다.")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()

def main():
    add_word()

if __name__ == "__main__":
    main()
