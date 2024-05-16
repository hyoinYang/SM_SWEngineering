import openai
import os
import pandas as pd
import time
from dotenv import load_dotenv
from db_connection import connect_to_database

# MySQL 연결
mydb = connect_to_database()
load_dotenv()

openai.api_key = os.getenv("api_key")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
# gpt api 호출해서 문장 반환
def make_sentence(word):
    prompt = f"'{word}' 영어 단어가 문장 하나 만들어줘"
    response = get_completion(prompt)
    return response

# gpt api 호출해서 한국어로 번역
def translate_to_korean(sen):
    prompt = f"'{sen}' 를 한국어로 번역해줘"
    response = get_completion(prompt)
    return response

# db에 문장 추가
def insert_sentence(eng_word, sentence):
    mycursor = mydb.cursor()
    sql = "UPDATE words SET example_sentence = '{}' WHERE eng_word = '{}'".format(sentence, eng_word)
    mycursor.execute(sql)
    mydb.close()


# example_sentence 비어있음 -> 영문 추가
def get_all_null_sentences():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT eng_word FROM words WHERE example_sentence IS NULL")
    null_example_rows = mycursor.fetchall()
    for row in null_example_rows:
        eng_word = row[0]
        print(eng_word)
        sentence = make_sentence(eng_word)
        print(sentence)
        sql = "UPDATE words SET example_sentence = %s WHERE eng_word = %s"
        val=(sentence, eng_word)
        mycursor.execute(sql,val)
        mydb.commit()
    mydb.close()

# kor example_sentence 비어있음 -> 한국어 추가
def trans_kor_null_sentences():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT eng_word, example_sentence FROM words WHERE kor_example_sentence IS NULL")
    null_example_rows = mycursor.fetchall()
    for row in null_example_rows:
        eng_word = row[0]
        sen = row[1]
        print(sen)
        kor_sentence = translate_to_korean(sen)
        print(kor_sentence)
        sql = "UPDATE words SET kor_example_sentence = %s WHERE eng_word = %s"
        val=(kor_sentence, eng_word)
        mycursor.execute(sql,val)
        mydb.commit()
    mydb.close()
trans_kor_null_sentences()
