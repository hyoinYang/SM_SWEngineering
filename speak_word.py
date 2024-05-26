import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""영어 단어, 영어 문장 발음 구현 완료
   언어 감지를 영어로 고정하는건 미완성
"""

class SpeakWord:
    def __init__(self):
        self.count = 0
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new") # 웹페이지 보이지 않도록
        self.driver = webdriver.Chrome(options=options) # options=options
        self.driver.get("https://papago.naver.com/")

    def speak_Word(self): #입력된 단어, 예문을 발음하는 기능
        self.driver.find_element(By.XPATH,"//*[@id='btn-toolbar-source']/span[1]/span/span/button").click()

    def input_Word(self,word): # 입력된 단어, 예문을 입력하는 기능
        self.driver.find_element(By.XPATH,"//*[@id='txtSource']").send_keys(word)
        time.sleep(1) 

    def erase_English(self): # 입력된 단어, 예문을 지움
        self.driver.find_element(By.XPATH,"//*[@id='sourceEditArea']/button").click()

    def close_Web(self): # 웹페이지 닫음 ( 크롤링 기능은 유지 )
        self.driver.close()
    
    def init_speak(self,word):
        if self.count==1:
            self.erase_English()
        self.input_Word(word)
        self.speak_Word()
        self.count = 1




# count = 0 # 영어 예문을 말하기 위한 변수
# if __name__ == "__main__": # speak_word.py를 모듈로 불러올 때 이 코드는 실행 안 됨
#     crawling_START()
#     while True:
#         word = input("영어단어를 적어주세요: ")
#         if word == 'stop': # stop 입력하면 웹 닫음
#             close_Web()
#             break
#         if word == 'wait': # 웹이 닫히고 다시 열리는지 테스트 ( 실제 단어장에 구현 X )
#             close_Web()
#             crawling_START()
#             count=0
#             continue
#         if count == 1:
#             erase_English()
#         input_Word(word)
#         speak_Word(word)
#         count = 1


