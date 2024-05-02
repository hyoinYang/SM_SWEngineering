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

def check_word_exist(word):
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor()
        sql = "SELECT * FROM words WHERE eng_word = %s"
        cursor.execute(sql, (word,))
        result = cursor.fetchone()
        if result:
            print("단어:", result[0])  # 단어 출력
            print("의미:", result[1])  # 의미 출력
            return True  # 단어가 존재하면 True 반환
        else:
            print("단어가 데이터베이스에 존재하지 않습니다.")
            return False  # 단어가 존재하지 않으면 False 반환
    except mysql.connector.Error as err:
        print("MySQL 오류:", err)
    finally:
        cursor.close()

# 검색할 단어 입력 받기
search_word = input("검색할 단어를 입력하세요: ")

# 단어가 데이터베이스에 있는지 확인
check_word_exist(search_word)
