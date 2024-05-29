from wordDB.db_connection import connect_to_database
from mysql.connector import Error

def check_mysql_connection():
    try:
        # MySQL 연결 설정
        mydb = connect_to_database()

        if mydb.is_connected():
            print("MySQL 데이터베이스에 성공적으로 연결되었습니다.")
            mycursor = mydb.cursor()
            # 간단한 쿼리 실행으로 연결 확인
            mycursor.execute("SELECT DATABASE();")
            record = mycursor.fetchone()
            print("현재 연결된 데이터베이스:", record)

    except Error as e:
        print("MySQL 연결에 실패했습니다:", e)

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    check_mysql_connection()
