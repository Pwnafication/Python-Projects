from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\ChromeWebDriver\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

PROMISED_DOWN = 500
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0
    def get_speeds(self):
        self.driver.get('https://www.speedtest.net/')
        print("Waiting 5 seconds.")
        time.sleep(5)
        print("Attempting to find Go Button.")
        go_button = self.driver.find_element(By.CLASS_NAME,'start-button a')
        print("Attempting to click GO Button.")
        go_button.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.CLASS_NAME,'result-data-value download-speed')
        print(down_speed.text)

        up_speed = self.driver.find_element(By.CLASS_NAME,'result-data-value upload-speed')
        print(up_speed.text)

bot = InternetSpeedTwitterBot()
bot.get_speeds()
