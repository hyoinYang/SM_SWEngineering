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
            for word in words:
                print("단어:", word[0])  # 단어 출력
                print("의미:", word[1])  # 의미 출력
                print("")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()

# 모든 단어 불러오기
read_all_words()
