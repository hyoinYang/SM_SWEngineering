import os
import pandas as pd
import mysql.connector
from db_connection import connect_to_database

# MySQL 연결
mydb = connect_to_database()

if mydb is not None:
    try:
        # 엑셀 파일에서 데이터 읽어오기
        current_path = os.getcwd()
        print(os.path.join(current_path, 'engwords.xlsx'))

        excel_data = pd.read_excel('') #업로든된 파일

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

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()
else:
    print("데이터베이스에 연결할 수 없습니다.")
