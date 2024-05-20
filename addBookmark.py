from wordDB.db_connection import connect_to_database
from login import login
mydb = connect_to_database()
mycursor = mydb.cursor()

def add_bookmark(mem_id, eng_word):
    insert_query = "INSERT INTO Correct_words (eng_word, member_id) VALUES (%s, %s)"
    val = (eng_word, mem_id)
    mycursor.execute(insert_query, val)
    print("북마크에 추가했습니다.")
    return True

def add_studied_word(mem_id, eng_word):
    insert_query = "INSERT INTO Studied_words (eng_word, member_id) VALUES (%s, %s)"
    val = (eng_word, mem_id)
    mycursor.execute(insert_query, val)
    return True
