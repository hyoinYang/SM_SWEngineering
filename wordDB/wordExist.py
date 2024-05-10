import mysql.connector
from db_connection import connect_to_database

mydb = connect_to_database()

def check_word_exist(word):
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "SELECT * FROM words WHERE eng_word = %s"
        cursor.execute(sql, (word,))
        result = cursor.fetchone()
        return bool(result)  # 단어가 존재하면 True, 존재하지 않으면 False 반환
    except mysql.connector.Error as err:
        print("MySQL 오류:", err)
    finally:
        cursor.close()

def main():
    # 검색할 단어 입력 받기
    search_word = input("검색할 단어를 입력하세요: ")

    # 단어가 데이터베이스에 있는지 확인
    if (check_word_exist(search_word)):
        print("단어가 데이터베이스에 존재합니다.")
    else:
        print("단어가 데이터베이스에 존재하지 않습니다.")


# 스크립트를 직접 실행할 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    main()
