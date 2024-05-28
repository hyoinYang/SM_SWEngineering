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
        self.driver.find_element(By.XPATH,"//*[@id='ddSourceLanguageButton']/span").click()
        self.driver.find_element(By.XPATH,"//*[@id='ddSourceLanguage']/div[2]/ul/li[3]/a").click()        
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