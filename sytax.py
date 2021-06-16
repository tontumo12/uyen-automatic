from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import os
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get ("http://bus.liberal.vn/")
# print (driver.title)

# email = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/input")
# password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/form/div/div/div/div[1]/div[2]/input")
# email.send_keys("admin-nguyen-hue")
# password.send_keys("abc123")
# print("+++++++++++++++++++++++++++++")
# print(password)

# submit_button = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/form/div/div/div/div[2]/button")
# submit_button[0].click()
# # driver.quit()
class SytaxService:

    @classmethod
    def phantichcuphap(cls, sytaxs:list):
        for sytax in sytaxs:
            if(sytax.index('open_web:') > -1):
                url = sytax.split(" ")[1]
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(url)
                print (driver.title)