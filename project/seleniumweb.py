from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class inflow:
    def __init__(self):
        service=Service(executable_path=r"C:\Users\dilli\.cache\selenium\chromedriver\win64\130.0.6723.69\chromedriver.exe")
        self.driver=webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        
    def get_info(self,query):
       #self.query=query
       self.driver.get(url="https://www.wikipedia.org")
       search=WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.NAME,'search')))
       search.send_keys(query)
       search_form=self.driver.find_element(By.XPATH,'//*[@id="search-form"]')
       search_form.submit()
       #=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@type="submit"]')))
       #enter.click()
       WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.ID,'firstHeading')))
       summary=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/p[2]')
       summary_text=summary.text
       time.sleep(5)
       self.driver.quit()
       return summary_text
        
       
