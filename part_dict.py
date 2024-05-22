import tkinter as tk
from tkinter import ttk
import random
class PartDictView:








# 각 파트 단어의 db
class PartDictModel:
    def __init__(self):
        self.word_texts = [] # 프레임에 들어가는 텍스트 클래스 ( 단어 )
        self.sentence_texts = [] # 초록색 프레임에 들어가는 텍스트 클래스 ( 예문 )
        self.wrong_word_texts = [] # 오답노트에 들어가는 텍스트 문자( 단어 )
        self.random_index=list(range(0,10)) # 랜덤 함수에서 사용, 임시로 단어 10개라고 설정했기 때문에 range(0,10)으로 설정함 
        self.learned_word = 0 # 이 파트에서 배운 단어 개수 
        self.learning_rate = 0.0 # 이 파트에서 배운 단어 학습률
