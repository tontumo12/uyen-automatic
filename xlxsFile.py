import pandas as pd
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
class WriteFileXlxs:

    @classmethod
    def writeFileXlxs(cls, data, columns, name):
        df = pd.DataFrame(data, columns = columns)

        fileName = './xlxsExporter/' + name
        df.to_excel(fileName)

        print('Export data success')