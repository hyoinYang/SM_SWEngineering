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

# 엑셀 파일에서 데이터 읽어오기
excel_data = pd.read_excel('engwords.xlsx')

# MySQL 테이블에 데이터 삽입
cursor = mydb.cursor()
for index, row in excel_data.iterrows():
    word = row['단어']
    meaning = row['뜻']
    sql = "INSERT INTO words (eng_word, kor_word) VALUES (%s, %s)"
    val = (word, meaning)
    cursor.execute(sql, val)

mydb.commit()

print(cursor.rowcount, "record inserted.")
