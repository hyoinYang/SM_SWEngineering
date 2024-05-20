import mysql.connector
from db_connection import connect_to_database
from wordExist import check_word_exist
from makeSen import make_sentence,translate_to_korean

# MySQL 연결
mydb = connect_to_database()
def define_part():
    cursor = mydb.cursor()
    query1 = "SELECT part FROM words ORDER BY id DESC LIMIT 1"
    cursor.execute(query1)
    part = cursor.fetchone()[0]
    query2 = "SELECT count(*) FROM words WHERE part = %s"
    cursor.execute(query2,(part,))
    count = cursor.fetchone()[0]
    if (count <30):
        return part
    else:
        return part+1
def define_id():
    cursor = mydb.cursor()
    query1 = "SELECT id FROM words ORDER BY id DESC LIMIT 1"
    cursor.execute(query1)
    id = cursor.fetchone()[0]
    return id+1

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
        example_sentence = make_sentence(word)
        kor_example_sentence =translate_to_korean(example_sentence)
        part = define_part()
        id = define_id()
        sql = "INSERT INTO words (eng_word, kor_word, example_sentence, kor_example_sentence, part, id) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (word, meaning, example_sentence, kor_example_sentence, part, id)
        cursor.execute(sql, val)

        # 변경사항을 커밋
        mydb.commit()

        print("단어가 성공적으로 추가되었습니다.")

    except mysql.connector.Error as err:
        print("MySQL 오류:", err)

    finally:
        # 연결 종료
        cursor.close()

def main():
    add_word()

if __name__ == "__main__":
    main()
