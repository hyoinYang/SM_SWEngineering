import random
from wordDB.db_connection import connect_to_database
from login import login
mydb = connect_to_database()
mycursor = mydb.cursor()

def get_random_question():
    # 데이터베이스에서 무작위로 단어, 뜻, 예시 문장, 예시 문장 뜻 가져오기
    mycursor.execute("SELECT eng_word, kor_word, example_sentence, kor_example_sentence FROM words ORDER BY RAND() LIMIT 1")
    question_data = mycursor.fetchone()
    return question_data

def get_random_choices(answer, word_list):
    # 정답을 제외한 다른 단어를 무작위로 선택하여 선지로 제공
    choices = [answer]
    while len(choices) < 4:
        random_word = random.choice(word_list)
        if random_word != answer and random_word not in choices:
            choices.append(random_word)
    random.shuffle(choices)
    return choices

def word_test(mem_id):
    while True:
        # 무작위 문제 가져오기
        word, meaning, example_sentence, example_sentence_meaning = get_random_question()

        # 빈칸에 들어갈 단어 선택
        blank_word = word
        sentence_with_blank = example_sentence.replace(word, "_____")
        print("\n문장:", sentence_with_blank)
        print("뜻:", example_sentence_meaning)

        # 단어장에서 중복되지 않는 다른 단어들을 무작위로 선택하여 선지로 제공
        mycursor.execute("SELECT eng_word FROM words WHERE eng_word != %s ORDER BY RAND() LIMIT 3", (word,))
        word_list = [record[0] for record in mycursor.fetchall()]
        choices = get_random_choices(word, word_list)

        while True:
            # 선지 출력
            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice}")

            # 사용자 입력 받기
            user_choice = input("정답을 선택하세요 (1~4, 종료하려면 'exit' 입력): ").strip()

            # 종료 확인
            if user_choice.lower() == 'exit':
                mycursor.close()
                mydb.close()
                return

            # 정답 확인
            if user_choice.isdigit() and 1 <= int(user_choice) <= 4:
                selected_word = choices[int(user_choice) - 1]
                if selected_word == word:
                    insert_query = "INSERT INTO Correct_words (eng_word, member_id) VALUES (%s, %s)"
                    val = (word, mem_id)
                    mycursor.execute(insert_query, val)
                    mydb.commit()
                    print("정답입니다!")
                    print("정답:", word)
                    print("뜻:", meaning)
                else:
                    insert_query = "INSERT INTO Wrong_words (eng_word, member_id) VALUES (%s, %s)"
                    val = (word, mem_id)
                    mycursor.execute(insert_query, val)
                    mydb.commit()
                    print("틀렸습니다. 정답은 '{}'입니다.".format(word))
                    print("뜻:", meaning)
                break
            else:
                print("올바른 선택지를 입력하세요. (1~4 중 하나를 입력하세요.)")

# 테스트 시작
word_test("unhi")
