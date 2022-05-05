import pytest
from selenium.webdriver.common.by import By
import time

# click signin\
class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_signin(self):
        sign_in_button = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/p[2]/button')
        sign_in_button.click()
        time.sleep(4)

    def enter_user(self, user):
        sign_in_user = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div/input')
        sign_in_user.send_keys("h1708")

    def enter_passwd(self, passwd):
        sign_in_password = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/input')
        time.sleep(2)
        sign_in_password.send_keys("h1708")

    def create_account(self):
        create_account = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/button')
        create_account.click()
        time.sleep(10)
        self.driver.switch_to.alert.accept()
        time.sleep(10)

    def assert_url(self):
        expected_url = "https://testing-assessment-foh15kew9-edvora.vercel.app/s"
        curr_url = self.driver.current_url
        assert expected_url == curr_url, "Failed to login because of faulty login functionality"