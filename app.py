from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import os
import pandas as pd
# from xlcsFile import WriteFileXlxs

driver = webdriver.Chrome(ChromeDriverManager().install())

dataExportColumn1 = []
dataExportColumn2 = []

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

def phantichcuphap(sytaxs:list,entry):
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
            openElementAndClick(sytax)
        if(sytax.find('check_title:') > -1):
            query = sytax.split("check_title: ")[1]
            checkTitleWebSite(query, sytax)
        if(sytax.find('-enter-') > -1):
            openElementAndEnter(sytax)
    data = {
        'TestCase': dataExportColumn1,
        'Result': dataExportColumn2
    }
    fileName = entry.split('.')[0]
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(fileName)
    writeFileXlxs(data,fileName + '.xlsx')
    

def openWebUrl(url, sytax):
    dataExportColumn1.append(sytax)
    try:
        driver.get(url)
        print(style.GREEN + sytax + ' ---------------SUCCESS')
        dataExportColumn2.append('SUCCESS')
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndCheckText(sytax):
    dataExportColumn1.append(sytax)
    try:
        element = getContentElement(sytax, ' -compare- ')
        if(element.text == sytax.split(' -compare- ')[1]):
            dataExportColumn2.append('SUCCESS')
            print(style.GREEN + sytax + ' ---------------SUCCESS')
        else:
            dataExportColumn2.append('ERROR')
            print(style.RED + sytax + ' ---------------ERROR')
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndInputData(sytax):
    dataExportColumn1.append(sytax)
    try:
        xpath = getContentElement(sytax,' -input- ')
        xpath.send_keys(sytax.split(' -input- ')[1])
        dataExportColumn2.append('SUCCESS')
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndClick(sytax):
    dataExportColumn1.append(sytax)
    try:
        xpath = getContentElement(sytax,' -click- ')
        xpath.click()
        dataExportColumn2.append('SUCCESS')
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + sytax + ' ---------------ERROR')

def openElementAndEnter(sytax):
    dataExportColumn1.append(sytax)
    try:
        xpath = getContentElement(sytax,' -enter- ')
        xpath.submit() 
        dataExportColumn2.append('SUCCESS')
        print(style.GREEN + sytax + ' ---------------SUCCESS')
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + sytax + ' ---------------ERROR')

def checkTitleWebSite(query, sytax):
    dataExportColumn1.append(sytax)
    try:
        if(driver.current_url == query):
            dataExportColumn2.append('SUCCESS')
            print(style.GREEN + sytax + ' ---------------SUCCESS')
        else:
            dataExportColumn2.append('ERROR')
            print(style.RED + sytax + ' ---------------ERROR')
    except:
        dataExportColumn2.append('ERROR')
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
    dataExportColumn1.append(sytax)
    try:
        if(sytax.find('find_xpath: ') > -1):
            query = sytax.split("find_xpath: ")[1]
            element = getXpathElement(query.split(text)[0])
            dataExportColumn2.append('SUCCESS')
            return element
        elif(sytax.find('find_id: ') > -1):
            query = sytax.split("find_id: ")[1]
            element = getIdElement(query.split(text)[0])
            dataExportColumn2.append('SUCCESS')
            return element
        elif(sytax.find('find_class: ') > -1):
            query = sytax.split("find_class: ")[1]
            element = getClassElement(query.split(text)[0])
            dataExportColumn2.append('SUCCESS')
            return element
    except:
        dataExportColumn2.append('ERROR')
        print(style.RED + "Không tìm thấy element")

def writeFileXlxs(data, name):
    cars_data = pd.DataFrame(data)

    # df = pd.ExcelWriter(name)

    cars_data.to_excel('./xlxsExporter/' + name, sheet_name="state")

    print('Export data success')

entries = os.listdir('uyentestcase/')

for entry in entries:
    f = open('uyentestcase/'+entry, 'r')
    str = f.read()
    listText = str.split("\n")
    phantichcuphap(listText,entry)
    # print(listText)