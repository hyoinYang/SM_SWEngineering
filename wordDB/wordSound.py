import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""영어 단어, 영어 문장 발음 구현 완료
   언어 감지를 영어로 고정하는건 미완성
"""

def crawling_START(): # 크롤링 시작 기능, 웹페이지 열기
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # 웹페이지 보이지 않도록
    #options.add_argument("excludeSwitches",['enable-logging'])
    driver = webdriver.Chrome(options=options) # options=options
    driver.get("https://papago.naver.com/")

def speak_Word(word): #입력된 단어, 예문을 발음하는 기능
    driver.find_element(By.XPATH,"//*[@id='btn-toolbar-source']/span[1]/span/span/button").click()
    time.sleep(1) 

def input_Word(word): # 입력된 단어, 예문을 입력하는 기능
    driver.find_element(By.XPATH,"//*[@id='txtSource']").send_keys(word)
    time.sleep(1) 

def erase_English(): # 입력된 단어, 예문을 지움
    driver.find_element(By.XPATH,"//*[@id='sourceEditArea']/button").click()

def close_Web(): # 웹페이지 닫음 ( 크롤링 기능은 유지 )
    driver.close()

#count = 0 # 영어 예문을 말하기 위한 변수

def wordSound(word): # speak_word.py를 모듈로 불러올 때 이 코드는 실행 안 됨
    count = 0
    crawling_START()
    while(True):
        time.sleep(1) 
        if count == 1:
            erase_English()
            close_Web()
            break
        #word = input("영어단어를 적어주세요: ")
        # if word == 'stop': # stop 입력하면 웹 닫음
        #     close_Web()
        #     break
        input_Word(word)
        speak_Word(word)
        count = 1


if __name__ == "__main__":
    wordSound("word")