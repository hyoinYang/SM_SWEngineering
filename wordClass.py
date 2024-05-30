from wordDB.db_connection import connect_to_database
from wordDB.makeSen import make_sentence, translate_to_korean
import random
from userClass import UserModel
from wordDB.db_connection import connect_to_database
from wordDB.makeSen import make_sentence, translate_to_korean
import random
from userClass import UserModel

class WordDBModel:
    def __init__(self):
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor(buffered=True)
        
    # part 수 return
    def get_part(self):
        query1 = "SELECT part FROM words ORDER BY id DESC LIMIT 1"
        self.cursor.execute(query1)
        part = self.cursor.fetchone()[0]
        return part

    ####### CREATE #######
    def check_word_exist(self, word):
        check_query = "SELECT * FROM words WHERE eng_word = %s"
        self.cursor.execute(check_query, (word,))
        result = self.cursor.fetchone()
        return bool(result)

    def define_part(self):
        query1 = "SELECT part FROM words ORDER BY id DESC LIMIT 1"
        self.cursor.execute(query1)
        part = self.cursor.fetchone()[0]
        query2 = "SELECT count(*) FROM words WHERE part = %s"
        self.cursor.execute(query2, (part,))
        count = self.cursor.fetchone()[0]
        if count < 30:
            return part
        else:
            return part + 1

    def define_id(self):
        query1 = "SELECT id FROM words ORDER BY id DESC LIMIT 1"
        self.cursor.execute(query1)
        id = self.cursor.fetchone()[0]
        return id + 1

    def add_word(self, word, meaning):
        if self.check_word_exist(word):
            return "이미 데이터베이스에 존재하는 단어입니다."
        else:
            example_sentence = make_sentence(word)
            kor_example_sentence = translate_to_korean(example_sentence)
            part = self.define_part()
            id = self.define_id()
            sql = "INSERT INTO words (eng_word, kor_word, example_sentence, kor_example_sentence, part, id) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (word, meaning, example_sentence, kor_example_sentence, part, id)
            self.cursor.execute(sql, val)
            self.conn.commit()
            return "단어가 성공적으로 추가되었습니다."

    ####### READ #######
    def read_words_by_part(self, part):
        sql = "SELECT * FROM words WHERE part = %s"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        return words
    def read_eng_words(self):
        sql = "SELECT eng_word FROM words"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        total = []
        if words is not None:
            for word in words:
                total.append(word[0])
        return total
    def read_kor_words(self):
        sql = "SELECT kor_word FROM words"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        total = []
        if words is not None:
            for word in words:
                total.append(word[0])
        return total
    def read_sentece(self):
        sql = "SELECT example_sentence FROM words"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        total = []
        if words is not None:
            for word in words:
                total.append(word[0])
        return total
    def read_kor_sentece(self):
        sql = "SELECT kor_example_sentence FROM words"
        self.cursor.execute(sql)
        words = self.cursor.fetchall()
        total = []
        if words is not None:
            for word in words:
                total.append(word[0])
        return total

    ####### UPDATE #######
    def update_word(self, word, contents):
        sql = "UPDATE words SET kor_word = %s WHERE eng_word = %s"
        self.cursor.execute(sql, (contents, word,))
        self.conn.commit()
        return True

    ####### DELETE #######
    def delete_word(self, word):
        sql = "DELETE FROM words WHERE eng_word = %s"
        self.cursor.execute(sql, (word,))
        self.conn.commit()
        return "단어가 성공적으로 삭제되었습니다."

    ####### WORDTEST - wrong, correct words #######
    def get_words_from_part(self, part):
        query = "SELECT eng_word, kor_word, example_sentence, kor_example_sentence FROM words WHERE part = %s"
        self.cursor.execute(query, (part,))
        words = self.cursor.fetchall()
        return words

    def get_random_choices(self, answer, part):
        query = "SELECT eng_word FROM words WHERE eng_word != %s AND part = %s"
        self.cursor.execute(query, (answer, part))
        word_list = [record[0] for record in self.cursor.fetchall()]
        choices = [answer]
        while len(choices) < 4:
            if len(word_list) == 0:
                break
            random_word = random.choice(word_list)
            if random_word not in choices:
                choices.append(random_word)
        random.shuffle(choices)
        return choices

    def record_correct_word(self, word, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            insert_query = "INSERT INTO Correct_words (eng_word, member_id) VALUES (%s, %s)"
            self.cursor.execute(insert_query, (word, real_id))
            self.conn.commit()

    def record_wrong_word(self, word, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            insert_query = "INSERT INTO Wrong_words (eng_word, member_id) VALUES (%s, %s)"
            self.cursor.execute(insert_query, (word, real_id))
            self.conn.commit()

    ###########

    def get_all_wrong_words(self, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s", (mem_id,))
        result = self.cursor.fetchone()
        print(result)

        # 결과가 있는지 확인
        if result:
            real_id = result[0]

            # 두 번째 쿼리 실행
            sql = "SELECT w.* FROM words w JOIN Wrong_words ww ON w.eng_word = ww.eng_word WHERE ww.member_id = %s"
            self.cursor.execute(sql, (real_id,))
            return self.cursor.fetchall()
        else:
            return []  # 결과가 없으면 빈 리스트 반환

    def get_all_correct_words(self, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            sql = "SELECT w.* FROM words w JOIN Correct_words cw ON w.eng_word = cw.eng_word WHERE cw.member_id = %s"
            self.cursor.execute(sql, (real_id,))
            return self.cursor.fetchall()
        else:
            return []

    ####### BOOKMARK #######
    def add_bookmark(self, mem_id, eng_word):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            insert_query = "INSERT INTO Bookmark_words (eng_word, member_id) VALUES (%s, %s)"
            val = (eng_word, real_id)
            self.cursor.execute(insert_query, val)
            self.conn.commit()
            return True
    def add_bookmark_by_userName(self, mem_id, eng_word):
        insert_query = "INSERT INTO Bookmark_words (eng_word, member_id) VALUES (%s, %s)"
        val = (eng_word, mem_id)
        self.cursor.execute(insert_query, val)
        self.conn.commit()
        return True
    
    def get_all_bookmarks(self, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            sql = "SELECT w.* FROM words w JOIN Bookmark_words bw ON w.eng_word = bw.eng_word WHERE bw.member_id = %s"
            self.cursor.execute(sql, (real_id,))
            return self.cursor.fetchall()
        else:
            return []
    def get_all_bookmarks_word_by_userName(self, mem_id):
        sql1 = "select * from Bookmark_words where member_id = %s"
        self.cursor.execute(sql1, (mem_id, ))
        if(self.cursor.fetchone() is None):
            return []
        else:
            sql2 = "SELECT w.eng_word FROM words w JOIN Bookmark_words bw ON w.eng_word = bw.eng_word WHERE bw.member_id = %s"
            self.cursor.execute(sql2, (mem_id,))
        return self.cursor.fetchall()
    def get_all_bookmarks_sentence_by_userName(self, mem_id):
        sql1 = "select * from Bookmark_words where member_id = %s"
        self.cursor.execute(sql1, (mem_id, ))
        if(self.cursor.fetchone() is None):
            return []
        else:
            sql = "SELECT w.kor_word, w.example_sentence, w.kor_example_sentence FROM words w JOIN Bookmark_words bw ON w.eng_word = bw.eng_word WHERE bw.member_id = %s"
            self.cursor.execute(sql, (mem_id,))
            return self.cursor.fetchall()
    ####### STUDIED_WORDS #######
    def add_studied_word(self, mem_id, eng_word):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            insert_query = "INSERT INTO Studied_words (eng_word, member_id) VALUES (%s, %s)"
            val = (eng_word, real_id)
            self.cursor.execute(insert_query, val)
            self.conn.commit()
            return True

    def get_all_studied_words(self, mem_id):
        self.cursor.execute("SELECT user_id FROM sessions WHERE session_id=%s",(mem_id,))
        result = self.cursor.fetchone()
        if result:
            real_id = result[0]
            sql = "SELECT w.* FROM words w JOIN Studied_words sw ON w.eng_word = sw.eng_word WHERE sw.member_id = %s"
            self.cursor.execute(sql, (real_id,))
            return self.cursor.fetchall()
        else:
            return []

class WordView:
    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

    def display_words(self, words):
        if not words:
            print("데이터베이스에 단어가 없습니다.")
        else:
            for word in words:
                print("단어:", word[0])
                print("의미:", word[1])
                print("예문:", word[2])
                print("예문해석:", word[3])
                print("")

    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

    def get_user_choice(self):
        return input("정답을 선택하세요 (1~4, 종료하려면 'exit' 입력): ").strip()

    def display_word_list(self, words):
        if not words:
            print("목록이 비어 있습니다.")
        else:
            for word in words:
                print("단어:", word[0])
                print("의미:", word[1])
                print("예문:", word[2])
                print("예문해석:",word[3])
                print("")

    def display_wrong_words(self, words):
        print("\n틀린 단어 목록:")
        self.display_word_list(words)

    def display_correct_words(self, words):
        print("\n맞은 단어 목록:")
        self.display_word_list(words)

    def display_bookmarks(self, words):
        print("\n북마크 목록:")
        self.display_word_list(words)

    def display_studied_words(self, words):
        print("\n공부한 단어 목록:")
        self.display_word_list(words)

    def display_question(self, word, sentence, meaning, choices):
        sentence_with_blank = sentence.replace(word, "_____")
        print("\n문장:", sentence_with_blank)
        print("뜻:", meaning)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

    def get_user_choice(self):
        return input("정답을 선택하세요 (1~4, 종료하려면 'exit' 입력): ").strip()

class WordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.UserModel = UserModel()
        self.current_session_id = None

    def login(self):
        user_id = self.view.get_input("사용자 ID를 입력하세요: ")
        password = self.view.get_input("비밀번호를 입력하세요: ")
        user = self.UserModel.verify_user(user_id, password)
        if user:
            self.current_session_id = self.UserModel.create_session(user_id)
            self.view.display_message(f"{user[1]}님, 환영합니다!")
        else:
            self.view.display_message("로그인 실패: 잘못된 사용자 ID 또는 비밀번호입니다.")

    def logout(self):
        if self.current_session_id:
            self.UserModel.destroy_session(self.current_session_id)
            self.current_session_id = None
            self.view.display_message("로그아웃 되었습니다.")
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    ####### CREATE #######
    def add_word(self):
        word = self.view.get_input("추가할 단어를 입력하세요: ")
        meaning = self.view.get_input("단어의 의미를 입력하세요: ")
        message = self.model.add_word(word, meaning)
        self.view.display_message(message)

    ####### READ #######
    def read_words_by_part(self):
        part = self.view.get_input("읽을 파트를 입력하세요: ")
        words = self.model.read_words_by_part(part)
        self.view.display_words(words)

    ####### UPDATE #######
    def update_word(self):
        word = self.view.get_input("수정할 단어를 입력하세요: ")
        contents = self.view.get_input("단어의 새로운 의미를 입력하세요: ")
        success = self.model.update_word(word, contents)
        if success:
            self.view.display_message("단어가 성공적으로 수정되었습니다.")
        else:
            self.view.display_message("단어 수정에 실패했습니다.")

    ####### DELETE #######
    def delete_word(self):
        word = self.view.get_input("삭제할 단어를 입력하세요: ")
        message = self.model.delete_word(word)
        self.view.display_message(message)

    ####### WORDTEST - wrong, correct words #######
    def take_quiz(self):
        if self.current_session_id:
            part = self.view.get_input("테스트할 파트를 입력하세요: ")
            words = self.model.get_words_from_part(part)
            if not words:
                self.view.display_message("선택한 파트에 단어가 없습니다.")
                return
            random.shuffle(words)
            for word in words:
                choices = self.model.get_random_choices(word[0], part)
                self.view.display_question(word[0], word[2], word[3], choices)
                while True:
                    user_choice = self.view.get_user_choice()
                    if user_choice.lower() == 'exit':
                        return  # 퀴즈를 종료하고 메서드를 종료합니다.
                    try:
                        user_choice = int(user_choice)
                        if user_choice not in [1, 2, 3, 4]:
                            raise ValueError("잘못된 입력입니다. 1에서 4 사이의 숫자를 입력하세요.")
                        break  # 유효한 입력이므로 루프를 종료합니다.
                    except (ValueError, IndexError):
                        self.view.display_message("잘못된 입력입니다. 1에서 4 사이의 숫자를 입력하세요.")

                if choices[user_choice - 1] == word[0]:
                    self.view.display_message("정답입니다!")
                    self.model.record_correct_word(word[0], self.current_session_id)
                else:
                    self.view.display_message(f"오답입니다. 정답은 {word[0]}입니다.")
                    self.model.record_wrong_word(word[0], self.current_session_id)
        else:
            self.view.display_message("퀴즈를 시작하기 전에 로그인하세요.")

    def view_wrong_words(self):
        if self.current_session_id:
            words = self.model.get_all_wrong_words(self.current_session_id)
            self.view.display_wrong_words(words)
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    def view_correct_words(self):
        if self.current_session_id:
            words = self.model.get_all_correct_words(self.current_session_id)
            self.view.display_correct_words(words)
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    ####### BOOKMARK #######
    def add_bookmark(self):
        if self.current_session_id:
            eng_word = self.view.get_input("북마크할 단어를 입력하세요: ")
            success = self.model.add_bookmark(self.current_session_id, eng_word)
            if success:
                self.view.display_message("단어가 북마크에 추가되었습니다.")
            else:
                self.view.display_message("단어 추가에 실패했습니다.")
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    def view_bookmarks(self):
        if self.current_session_id:
            words = self.model.get_all_bookmarks(self.current_session_id)
            self.view.display_bookmarks(words)
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    ####### STUDIED_WORDS #######
    def add_studied_word(self):
        if self.current_session_id:
            eng_word = self.view.get_input("공부한 단어를 입력하세요: ")
            success = self.model.add_studied_word(self.current_session_id, eng_word)
            if success:
                self.view.display_message("공부한 단어로 추가되었습니다.")
            else:
                self.view.display_message("단어 추가에 실패했습니다.")
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

    def view_studied_words(self):
        if self.current_session_id:
            words = self.model.get_all_studied_words(self.current_session_id)
            self.view.display_studied_words(words)
        else:
            self.view.display_message("로그인 상태가 아닙니다.")

def main():
    model = WordDBModel()
    view = WordView()
    controller = WordController(model, view)

    while True:
        print("\n1. 로그인")
        print("2. 로그아웃")
        print("3. 단어 조회")
        print("4. 단어 수정")
        print("5. 단어 추가")
        print("6. 단어 삭제")
        print("7. 틀린 단어 목록 조회")
        print("8. 맞은 단어 목록 조회")
        print("9. 북마크 추가")
        print("10. 학습한 단어로 추가")
        print("11. 학습한 단어 목록 조회")
        print("12. 단어 테스트")
        print("13. 북마크 단어 목록 조회")  # 북마크 단어 목록 조회 추가
        print("14. 종료")

        choice = view.get_input("메뉴를 선택하세요: ")

        if choice == '1':
            controller.login()
        elif choice == '2':
            controller.logout()
        elif choice == '3':
            controller.read_words_by_part()
        elif choice == '4':
            controller.update_word()
        elif choice == '5':
            controller.add_word()
        elif choice == '6':
            controller.delete_word()
        elif choice == '7':
            controller.view_wrong_words()
        elif choice == '8':
            controller.view_correct_words()
        elif choice == '9':
            controller.add_bookmark()
        elif choice == '10':
            controller.add_studied_word()
        elif choice == '11':
            controller.view_studied_words()
        elif choice == '12':
            controller.take_quiz()
        elif choice == '13':
            controller.view_bookmarks()
        elif choice == '14':
            view.display_message("프로그램을 종료합니다.")
            break
        else:
            view.display_message("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()