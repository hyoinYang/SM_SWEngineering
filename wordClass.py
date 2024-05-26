from wordDB.db_connection import connect_to_database
from wordDB.makeSen import make_sentence, translate_to_korean
import random

class WordModel:
    def __init__(self):
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor()

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
        self.cursor.execute(sql, (part,))
        words = self.cursor.fetchall()
        return words

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
        insert_query = "INSERT INTO Correct_words (eng_word, member_id) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (word, mem_id))
        self.conn.commit()

    def record_wrong_word(self, word, mem_id):
        insert_query = "INSERT INTO Wrong_words (eng_word, member_id) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (word, mem_id))
        self.conn.commit()


    ###########

    def get_all_wrong_words(self, mem_id):
        sql = "SELECT w.* FROM words w JOIN Wrong_words ww ON w.eng_word = ww.eng_word WHERE ww.member_id = %s"
        self.cursor.execute(sql, (mem_id,))
        return self.cursor.fetchall()

    def get_all_correct_words(self, mem_id):
        sql = "SELECT w.* FROM words w JOIN Correct_words cw ON w.eng_word = cw.eng_word WHERE cw.member_id = %s"
        self.cursor.execute(sql, (mem_id,))
        return self.cursor.fetchall()

    ####### BOOKMARK #######
    def add_bookmark(self, mem_id, eng_word):
        insert_query = "INSERT INTO Bookmark_words (eng_word, member_id) VALUES (%s, %s)"
        val = (eng_word, mem_id)
        self.cursor.execute(insert_query, val)
        self.conn.commit()
        return True

    def get_all_bookmarks(self, mem_id):
        sql = "SELECT w.* FROM words w JOIN Bookmark_words bw ON w.eng_word = bw.eng_word WHERE bw.member_id = %s"
        self.cursor.execute(sql, (mem_id,))
        return self.cursor.fetchall()

    ####### STUDIED_WORDS #######
    def add_studied_word(self, mem_id, eng_word):
        insert_query = "INSERT INTO Studied_words (eng_word, member_id) VALUES (%s, %s)"
        val = (eng_word, mem_id)
        self.cursor.execute(insert_query, val)
        self.conn.commit()
        return True

    def get_all_studied_words(self, mem_id):
        sql = "SELECT w.* FROM words w JOIN Studied_words sw ON w.eng_word = sw.eng_word WHERE sw.member_id = %s"
        self.cursor.execute(sql, (mem_id,))
        return self.cursor.fetchall()


class WordView:
    def display_words(self, words):
        if not words:
            print("데이터베이스에 단어가 없습니다.")
        else:
            for word in words:
                print("단어:", word[0])
                print("의미:", word[1])
                print("")

    def display_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

    def display_question(self, sentence, meaning, choices):
        print("\n문장:", sentence)
        print("뜻:", meaning)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

    def get_user_choice(self):
        return input("정답을 선택하세요 (1~4, 종료하려면 'exit' 입력): ").strip()
    def add_bookmark(self, mem_id):
        eng_word = self.view.get_input("북마크에 추가할 단어를 입력하세요: ")
        if self.model.check_word_exist(eng_word):
            if self.model.add_bookmark(mem_id, eng_word):
                self.view.display_message("북마크에 추가했습니다.")
            else:
                self.view.display_message("북마크 추가 중 오류가 발생했습니다.")
        else:
            self.view.display_message("해당 단어는 데이터베이스에 존재하지 않습니다.")

    def add_studied_word(self, mem_id):
        eng_word = self.view.get_input("학습한 단어로 추가할 단어를 입력하세요: ")
        if self.model.check_word_exist(eng_word):
            if self.model.add_studied_word(mem_id, eng_word):
                self.view.display_message("학습한 단어 목록에 추가했습니다.")
            else:
                self.view.display_message("학습한 단어 추가 중 오류가 발생했습니다.")
        else:
            self.view.display_message("해당 단어는 데이터베이스에 존재하지 않습니다.")
    def display_word_list(self, words):
        if not words:
            print("목록이 비어 있습니다.")
        else:
            for word in words:
                print("단어:", word[1])  # Assuming index 1 is the English word
                print("의미:", word[2])  # Assuming index 2 is the meaning
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
    def display_question(self, sentence, meaning, choices):
        print("\n문장:", sentence)
        print("뜻:", meaning)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")

    def get_user_choice(self):
        return input("정답을 선택하세요 (1~4, 종료하려면 'exit' 입력): ").strip()

class WordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def read_all_words(self, part):
        words = self.model.read_words_by_part(part)
        if words is not None:
            self.view.display_words(words)
        else:
            self.view.display_message("단어를 가져오는 중 오류가 발생했습니다.")

    def update_word(self):
        word = self.view.get_input("수정할 단어를 입력하세요: ")
        if self.model.check_word_exist(word):
            contents = self.view.get_input("수정할 내용을 입력하세요: ")
            if self.model.update_word(word, contents):
                self.view.display_message("단어가 성공적으로 업데이트되었습니다.")
            else:
                self.view.display_message("단어 업데이트 중 오류가 발생했습니다.")
        else:
            self.view.display_message("수정할 단어가 존재하지 않습니다.")

    def check_word_existence(self):
        word = self.view.get_input("검색할 단어를 입력하세요: ")
        if self.model.check_word_exist(word):
            self.view.display_message("단어가 데이터베이스에 존재합니다.")
        else:
            self.view.display_message("단어가 데이터베이스에 존재하지 않습니다.")

    def add_word(self):
        word = self.view.get_input("추가할 단어를 입력하세요: ")
        meaning = self.view.get_input("단어의 의미를 입력하세요: ")
        message = self.model.add_word(word, meaning)
        self.view.display_message(message)

    def delete_word(self):
        word = self.view.get_input("삭제할 단어를 입력하세요: ")
        if self.model.check_word_exist(word):
            message = self.model.delete_word(word)
            self.view.display_message(message)
        else:
            self.view.display_message("삭제할 단어가 존재하지 않습니다.")
    def add_bookmark(self, mem_id):
        eng_word = self.view.get_input("북마크에 추가할 단어를 입력하세요: ")
        if self.model.check_word_exist(eng_word):
            if self.model.add_bookmark(mem_id, eng_word):
                self.view.display_message("북마크에 추가했습니다.")
            else:
                self.view.display_message("북마크 추가 중 오류가 발생했습니다.")
        else:
            self.view.display_message("해당 단어는 데이터베이스에 존재하지 않습니다.")

    def add_studied_word(self, mem_id):
        eng_word = self.view.get_input("학습한 단어로 추가할 단어를 입력하세요: ")
        if self.model.check_word_exist(eng_word):
            if self.model.add_studied_word(mem_id, eng_word):
                self.view.display_message("학습한 단어 목록에 추가했습니다.")
            else:
                self.view.display_message("학습한 단어 추가 중 오류가 발생했습니다.")
        else:
            self.view.display_message("해당 단어는 데이터베이스에 존재하지 않습니다.")
    def get_wrong_words(self, mem_id):
        wrong_words = self.model.get_all_wrong_words(mem_id)
        self.view.display_wrong_words(wrong_words)

    def get_correct_words(self, mem_id):
        correct_words = self.model.get_all_correct_words(mem_id)
        self.view.display_correct_words(correct_words)

    def get_bookmarks(self, mem_id):
        bookmarks = self.model.get_all_bookmarks(mem_id)
        self.view.display_bookmarks(bookmarks)

    def get_studied_words(self, mem_id):
        studied_words = self.model.get_all_studied_words(mem_id)
        self.view.display_studied_words(studied_words)
    def word_test(self, mem_id):
        while True:
            part = self.view.get_input("시험 볼 파트 번호를 입력하세요 (종료하려면 'exit' 입력): ").strip()
            if part.lower() == 'exit':
                return
            if not part.isdigit():
                self.view.display_message("올바른 파트 번호를 입력하세요.")
                continue

            part = int(part)
            words = self.model.get_words_from_part(part)
            if not words:
                self.view.display_message("해당 파트 번호에 대한 단어가 없습니다.")
                continue

            for word_data in words:
                word, meaning, example_sentence, example_sentence_meaning = word_data
                sentence_with_blank = example_sentence.replace(word, "_____")
                choices = self.model.get_random_choices(word, part)
                self.view.display_question(sentence_with_blank, example_sentence_meaning, choices)

                while True:
                    user_choice = self.view.get_user_choice()
                    if user_choice.lower() == 'exit':
                        return

                    if user_choice.isdigit() and 1 <= int(user_choice) <= 4:
                        selected_word = choices[int(user_choice) - 1]
                        if selected_word == word:
                            self.model.record_correct_word(word, mem_id)
                            self.view.display_message("정답입니다!")
                        else:
                            self.model.record_wrong_word(word, mem_id)
                            self.view.display_message(f"틀렸습니다. 정답은 '{word}'입니다.")
                        break
                    else:
                        self.view.display_message("올바른 선택지를 입력하세요. (1~4 중 하나를 입력하세요.)")

            self.view.display_message(f"파트 {part}의 모든 단어를 테스트했습니다.")
            break

def main():
    model = WordModel()
    view = WordView()
    controller = WordController(model, view)

    while True:
        print("\n1. 단어 조회")
        print("2. 단어 수정")
        print("3. 단어 추가")
        print("4. 단어 삭제")
        print("5. 틀린 단어 목록 조회")
        print("6. 맞은 단어 목록 조회")
        print("7. 북마크 목록 조회")
        print("8. 북마크 추가")
        print("9. 학습한 단어로 추가")
        print("10. 학습한 단어 목록 조회")
        print("11. 단어 테스트")
        print("12. 종료")

        choice = view.get_input("메뉴를 선택하세요: ")

        if choice == '1':
            part = int(view.get_input("조회할 파트를 입력하세요: "))
            controller.read_all_words(part)
        elif choice == '2':
            controller.update_word()
        elif choice == '3':
            controller.add_word()
        elif choice == '4':
            controller.delete_word()
        elif choice == '5':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.get_wrong_words(mem_id)
        elif choice == '6':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.get_correct_words(mem_id)
        elif choice == '7':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.get_bookmarks(mem_id)
        elif choice == '8':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.add_bookmark(mem_id)
        elif choice == '9':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.add_studied_word(mem_id)
        elif choice == '10':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.get_studied_words(mem_id)
        elif choice == '11':
            mem_id = view.get_input("회원 ID를 입력하세요: ")
            controller.word_test(mem_id)
        elif choice == '12':
            view.display_message("프로그램을 종료합니다.")
            break
        else:
            view.display_message("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
