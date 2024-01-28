import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USERNAME = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASS")
SIMILAR_ACCOUNT = os.environ.get("SIMILAR_ACCOUNT")
CLICK = "arguments[0].click()"
SCROLL = "arguments[0].scrollTop = arguments[0].scrollHeight"


class InstaFollower:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=option)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        sleep(2)

        username = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

        password = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        try:
            captcha = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div[2]/div')))
            if captcha:
                input("Unusual log in occurred.\n Please do the needed process and press ENTER...")
        except TimeoutException:
            print("No unusual login occurred.")

        try:
            save_info = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                                             '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
            self.driver.execute_script(CLICK, save_info)
        except NoSuchElementException:
            print("No need to save info.")

        try:
            notification = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1')))
            self.driver.execute_script(CLICK, notification)
        except NoSuchElementException:
            print("No need to confirm notification.")

    def find_followers(self):
        search = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]/div/div')))
        self.driver.execute_script(CLICK, search)

        search_bar = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')))
        search_bar.send_keys(SIMILAR_ACCOUNT)

        similar_account = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a/div[1]/div/div/div[2]/div/div/div')))
        self.driver.execute_script(CLICK, similar_account)

        followers = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')))
        self.driver.execute_script(CLICK, followers)

        popup = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._aano")))

        for i in range(10):
            self.driver.execute_script(SCROLL, popup)
            sleep(10)

    def scrap_follower_list(self):
        no_of_followers = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span').text
        followers_list = []

        for i in range(int(no_of_followers)):
            follower_element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH,
                                                                                                    f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i + 1}]')))

            string = follower_element.text.split("\n")
            follower = (string[0] + " - " + string[1])
            followers_list.append(follower)

        with open("Followers.txt", mode="w", encoding="utf-8") as file:
            for fwl in followers_list:
                file.write(f"{fwl} \n")


mybot = InstaFollower()
mybot.login()
mybot.find_followers()
mybot.scrap_follower_list()