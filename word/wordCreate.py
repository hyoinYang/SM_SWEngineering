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
        return bool(result)  # 단어가 존재하면 True, 존재하지 않으면 False 반환
    except mysql.connector.Error as err:
        print("MySQL 오류:", err)
    finally:
        cursor.close()

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

add_word()
