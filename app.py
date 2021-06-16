from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import os
from sytax import SytaxService

driver = webdriver.Chrome(ChromeDriverManager().install())

os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def phantichcuphap(sytaxs:list):
    for sytax in sytaxs:
        if(sytax.find('name:') > -1):
            query = sytax.split("name: ")[1]
            print(style.CYAN + query + ' ---------------START')
        if(sytax.find('open_web:') > -1):
            url = sytax.split(" ")[1]
            openWebUrl(url, sytax)
        if(sytax.find('-compare-') > -1):
            # query = sytax.split(": ")[1]
            openElementAndCheckText(sytax)
        if(sytax.find('-input-') > -1):
            # query = sytax.split("find_xpath: ")[1]
            openElementAndInputData(sytax)
        if(sytax.find('-click-') > -1):
            # query = sytax.split("find_xpath: ")[1]
            openElementAndClickButton(sytax)
        if(sytax.find('check_title:') > -1):
            query = sytax.split("check_title: ")[1]
            checkTitleWebSite(query, sytax)

def openWebUrl(url, sytax):
    try:
        driver.get(url)
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndCheckText(sytax):
    try:
        element = getContentElement(sytax, ' -compare- ')
        if(element.text == sytax.split(' -compare- ')[1]):
            print(style.GREEN + sytax + ' ---------------SUCCESS')
        else:
            print(style.RED + sytax + ' ---------------ERROR')
    except:
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndInputData(sytax):
    try:
        xpath = getContentElement(sytax,' -input- ')
        xpath.send_keys(sytax.split(' -input- ')[1])
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndClickButton(sytax):
    try:
        xpath = getContentElement(sytax,' -click- ')
        xpath.click()
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        print(style.RED + sytax + ' ---------------ERROR')

def checkTitleWebSite(query, sytax):
    try:
        if(driver.current_url == query):
            print(style.GREEN + sytax + ' ---------------SUCCESS')
        else:
            print(style.RED + sytax + ' ---------------ERROR')
    except:
        print(style.RED + sytax + ' ---------------ERROR')

def getXpathElement(query):
    try:
        xpath = driver.find_element_by_xpath(query)
        return xpath
    except:
        print(style.RED + "Không tìm thấy xpath: " + query)

def getIdElement(query):
    try:
        xpath = driver.find_element_by_id(query)
        return xpath
    except:
        print(style.RED + "Không tìm thấy id: " + query)

def getClassElement(query):
    try:
        xpath = driver.ind_elements_by_class_name(query)
        return xpath[0]
    except:
        print(style.RED + "Không tìm thấy class: " + query)

def getContentElement(sytax,text):
    try:
        if(sytax.find('find_xpath: ') > -1):
            query = sytax.split("find_xpath: ")[1]
            element = getXpathElement(query.split(text)[0])
            return element
        elif(sytax.find('find_id: ') > -1):
            query = sytax.split("find_id: ")[1]
            element = getIdElement(query.split(text)[0])
            return element
        elif(sytax.find('find_class: ') > -1):
            query = sytax.split("find_class: ")[1]
            element = getClassElement(query.split(text)[0])
            return element
    except:
        print(style.RED + "Không tìm thấy element")

entries = os.listdir('uyentestcase/')
for entry in entries:
    f = open('uyentestcase/'+entry, 'r')
    str = f.read()
    listText = str.split("\n")
    phantichcuphap(listText)
    # print(listText)