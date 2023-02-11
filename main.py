from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
USER_NAME = 'ddddd'
TWITTER_PASSWORD = 'vvvvvv'
TWITTER_EMAIL = 'shlomo.mica@outlook.co.il'
TWITTER_URL = 'https://twitter.com/i/flow/signup'
WEB_SPEED = 'https://www.speedtest.net/'

s = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=s)

PROMISED_UP = 150
PROMISED_DOWN = 10


class InternetSpeedTwitterBot:
    def __init__(self, driver_class, pace_up, pace_down):
        self.selenium_driver = driver_class
        self.up = pace_up
        self.down = pace_down

    def get_internet_speed(self):
        self.selenium_driver.get(WEB_SPEED)
        cookies = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div[1]/div/button')
        cookies.click()
        time.sleep(2)
        go = driver.find_element(By.CLASS_NAME, 'start-text')
        go.click()
        time.sleep(50)
        upload_rate = driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        time.sleep(2)
        download_rate = driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        x = {"upload": float(upload_rate.text), "download": float(download_rate.text)}
        print(x)
        return x

    def tweet_at_provider(self):
        self.selenium_driver.get(TWITTER_URL)
        time.sleep(2)
        twitter_entry_button = driver.find_element(By.XPATH,
                                                   '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                                   '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span['
                                                   '2]/span/span')
        twitter_entry_button.click()
        time.sleep(2)
        Twitter_mail_input = driver.find_element(By.XPATH,
                                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                                 '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                 '2]/div/input')
        Twitter_mail_input.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        Twitter_mail_input.send_keys(Keys.ENTER)
        time.sleep(2)

        Twitter_username_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div['
                                                               '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                               '2]/label/div/div[2]/div/input')
        Twitter_username_input.send_keys(USER_NAME)
        time.sleep(2)
        Twitter_username_input.send_keys(Keys.ENTER)
        time.sleep(3)
        twittwer_pass = driver.find_element(By.NAME, 'password')
        time.sleep(2)
        twittwer_pass.send_keys(TWITTER_PASSWORD)
        twittwer_pass.send_keys(Keys.ENTER)
        time.sleep(99)


Q = InternetSpeedTwitterBot(driver, PROMISED_UP, PROMISED_DOWN)
real_up_down_rate = Q.get_internet_speed()
if real_up_down_rate["upload"] < PROMISED_UP or real_up_down_rate["download"] < PROMISED_DOWN:  # 150
    print("tweet pace not as promised")

if real_up_down_rate["download"] < PROMISED_DOWN:  # 10
    print("tweet down")
Q.tweet_at_provider()
time.sleep(2)
# Enter_twitter_button = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[' \
#                        '2]/div/div/div/div[7]/span[2]/span/span '
