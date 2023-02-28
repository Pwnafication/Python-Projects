from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\ChromeWebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print("Check", price.tag_name)
# print(price.get_attribute('innerHTML'))
# driver.quit()

###XPATH###
# driver.get("https://www.python.org/")
# dict = {}
# for n in range(0, 5):
#     dict[n] = {"time": driver.find_element(By.XPATH,
#                                            f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n + 1}]/time').text,
#                "name": driver.find_element(By.XPATH,
#                                            f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n + 1}]/a').text}

# print(dict)

### class= ###
# driver.get("https://www.python.org/")
# dates = driver.find_elements(By.CLASS_NAME, "event-widget div ul li time")
# names = driver.find_elements(By.CLASS_NAME, "event-widget div ul li a")
#
# dates_list = [date.text for date in dates]
# names_list = [name.text for name in names]
#
# print(dates_list)
# print(names_list)

###This was an <div id=XX> ###
# driver.get("https://en.wikipedia.org/wiki/Main_Page/")
# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
# print(article_count)
# driver.quit()

driver.get("https://app.usertesting.com/users/sign_in/")
email_field = driver.find_element(By.NAME,"email")
email_field.send_keys("NoobBotAPI@gmail.com")
time.sleep(3)
email_field.send_keys(Keys.ENTER)

