from wordDB.db_connection import connect_to_database
from login import login
mydb = connect_to_database()
mycursor = mydb.cursor()

def get_all_wrong_words(mem_id):
    mycursor.execute("SELECT eng_word FROM Wrong_words where member_id = %s", (mem_id,))
    word_list = [record[0] for record in mycursor.fetchall()]
    for word in word_list:
        mycursor.execute("SELECT * FROM words WHERE eng_word = %s", (word,))
        return mycursor.fetchall()

def get_all_correct_words(mem_id):
    mycursor.execute("SELECT eng_word FROM Correct_words where member_id = %s", (mem_id,))
    word_list = [record[0] for record in mycursor.fetchall()]
    for word in word_list:
        mycursor.execute("SELECT * FROM words WHERE eng_word = %s", (word,))
        return mycursor.fetchall()

def get_all_bookmark(mem_id):
    mycursor.execute("SELECT eng_word FROM Bookmark_words where member_id = %s", (mem_id,))
    word_list = [record[0] for record in mycursor.fetchall()]
    for word in word_list:
        mycursor.execute("SELECT * FROM words WHERE eng_word = %s", (word,))
        return mycursor.fetchall()

print(get_all_wrong_words("unhi"))
