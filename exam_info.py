import mysql.connector
from wordDB.db_connection import connect_to_database

mydb = connect_to_database()

def get_exam_info():
    try:
        # MySQL 쿼리 실행
        cursor = mydb.cursor(buffered=True)
        sql = "SELECT * FROM exam_info"
        cursor.execute(sql)
        result = cursor.fetchone()
        return result  # 단어가 존재하면 True, 존재하지 않으면 False 반환
    except mysql.connector.Error as err:
        print("MySQL 오류:", err)
    finally:
        cursor.close()

def main():
    print(get_exam_info())


# 스크립트를 직접 실행할 때만 main 함수를 호출합니다.
if __name__ == "__main__":
    main()
