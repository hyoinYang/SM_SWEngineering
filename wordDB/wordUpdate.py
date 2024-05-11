import mysql.connector
from db_connection import connect_to_database
from wordExist import check_word_exist

# MySQL 연결 설정
mydb = connect_to_database()
def update_word(word, contents):
    try:
        cursor = mydb.cursor()
        sql = "UPDATE words SET kor_word = %s WHERE eng_word = %s"
        cursor.execute(sql, (contents, word,))
        mydb.commit()
        print("단어가 성공적으로 업데이트되었습니다.")
    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()
def main():
    # 검색할 단어 입력 받기
    update_word_input = input("수정할 단어를 입력하세요: ")
    exist_bool = check_word_exist(update_word_input)
    if(exist_bool):
        update_contents = input("수정할 내용을 입력하세요: ")
        # 단어 수정
        update_word(update_word_input, update_contents)
    else:
        print("수정할 단어가 존재하지 않습니다.")

# 스크립트를 직접 실행할 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    main()
