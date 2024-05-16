import mysql.connector
from db_connection import connect_to_database

mydb = connect_to_database()

def read_all_words():
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "SELECT * FROM words"
        cursor.execute(sql)

        # 결과 가져오기
        words = cursor.fetchall()

        if len(words) == 0:
            print("데이터베이스에 단어가 없습니다.")
        else:
            print(words)
            return words
            # for word in words:
                # print("단어:", word[0])  # 단어 출력
                # print("의미:", word[1])  # 의미 출력
                # print("")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()
def main():
    read_all_words()

if __name__ == "__main__":
    main()
