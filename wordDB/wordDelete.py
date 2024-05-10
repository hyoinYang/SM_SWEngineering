import mysql.connector
from db_connection import connect_to_database
from wordExist import check_word_exist

# MySQL 연결
mydb = connect_to_database()

def delete_word(word):
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "DELETE FROM words WHERE eng_word = %s"
        #sql = "TRUNCATE words"
        cursor.execute(sql, (word,))

        # 변경사항을 커밋
        mydb.commit()

        print("단어가 성공적으로 삭제되었습니다.")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()

def main():
    # 삭제할 단어 입력 받기
    delete_word_input = input("삭제할 단어를 입력하세요: ")
    if(check_word_exist(delete_word_input)):
        delete_word(delete_word_input)
    else:
        # 단어 삭제 함수 호출
        print("단어가 데이터베이스에 존재하지 않습니다.")

if __name__ == "__main__":
    main()
