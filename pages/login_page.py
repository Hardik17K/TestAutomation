import pytest
from selenium.webdriver.common.by import By
import time



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # click login
    def enter_user(self, user):
        username = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div[1]/div/input")
        username.send_keys(user) #set user

    def enter_password(self, passwd):
        password = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/input')
        password.send_keys(passwd)

    def login(self):
        login = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/button')
        # time.sleep(20)
        login.click()
        time.sleep(20)

    def assert_url(self):
        expected_url = "https://testing-assessment-foh15kew9-edvora.vercel.app/s"
        curr_url = self.driver.current_url
        assert expected_url == curr_url, "Failed to login because of faulty login functionality"
