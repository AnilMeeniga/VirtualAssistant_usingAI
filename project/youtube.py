from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class music:
    def __init__(self):
        service=Service(executable_path=r"C:\Users\dilli\.cache\selenium\chromedriver\win64\130.0.6723.69\chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        #video=self.driver.find_element(By.XPATH,'//*[@id="video-title"]')
        video=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,'//a[@id="video-title"]')))
        video.click()  
        time.sleep(240)
