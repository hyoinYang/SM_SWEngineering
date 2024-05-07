import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# MySQL 연결 설정
mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_TABLE")
)
def delete_word(word):
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "DELETE FROM words WHERE eng_word = %s"
        cursor.execute(sql, (word,))

        # 변경사항을 커밋
        mydb.commit()

        if cursor.rowcount > 0:
            print("단어가 성공적으로 삭제되었습니다.")
        else:
            print("삭제할 단어가 데이터베이스에 존재하지 않습니다.")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()

# 삭제할 단어 입력 받기
delete_word_input = input("삭제할 단어를 입력하세요: ")

# 단어 삭제 함수 호출
delete_word(delete_word_input)
