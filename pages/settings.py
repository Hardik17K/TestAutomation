import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def edit_personal_info(self):
        edit_button = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[1]/div/div/button")
        edit_button.click()

    def fname(self, name):
        full_name = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/input")
        full_name.click()
        full_name.send_keys(name)

    def dob(self, date):
        date_of_birth = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/input")
        date_of_birth.click()
        date_of_birth.send_keys(date)

    def gender(self, selection):
        dropdown = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/select")
        dd = Select(dropdown)
        dd.select_by_visible_text(selection)

    def mobile(self, number):
        mobile_number = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div/input")
        mobile_number.click()
        mobile_number.send_keys(number)

    def address(self, addr):
        ad = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div/input")
        ad.click()
        ad.send_keys(addr)

    def save(self):
        save_button = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/div[1]/div/div/button[2]')
        if len(save_button) > 0:
            save_button[0].click()
            time.sleep(10)
            expected_url = "https://testing-assessment-foh15kew9-edvora.vercel.app"
            curr_url = self.driver.current_url
            assert expected_url == curr_url, "Save function not working perfectly as redirecting to other page"
            print("Save function working perfectly")
        else:
            assert len(save_button) > 0, "Element Not Found !!"
        time.sleep(10)

    def back_to_url(self):
        self.driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/s")

    def cancel(self):

        cancel_button = self.driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div[1]/div[1]/div/div/button[1]')
        if len(cancel_button) > 0:
            cancel_button[0].click()
        else:
            assert len(cancel_button) > 0, "Element Not Found !!"
        time.sleep(10)

    def edit_security(self):
        time.sleep(10)
        edit_security_button = self.driver.find_elements(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div/div/button")
        if len(edit_security_button) > 0:
            edit_security_button[0].click()
        else:
            assert len(edit_security_button) > 0, "Element Not Found !!"


    def change_password(self, new_passwd):
        change = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[2]/div/div/div/div/div/input")
        change.click()
        change.send_keys(new_passwd)

    def save_security(self):
        save_button = self.driver.find_elements(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div/div/button[2]")
        if len(save_button) > 0:
            save_button[0].click()
            edit_security_button = self.driver.find_elements(By.XPATH,"/html/body/div/div/main/div/div[2]/div[1]/div/div/button")
            if len(edit_security_button) > 0:
                edit_security_button[0].click()
            else:
                assert len(edit_security_button) > 0, "Save function not working properly due to faulty save button"
        else:
            assert len(save_button) > 0, "Element Not Found !!"
        time.sleep(10)

    def cancel_security(self):
        cancel_button = self.driver.find_elements(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div/div/button[1]")
        if len(cancel_button) > 0:
            cancel_button[0].click()
        else:
            assert len(cancel_button) > 0, "Element Not Found !!"

    def logout(self):
        logout_button = self.driver.find_elements(By.XPATH, "/html/body/div/div/main/div/div[3]/div[1]/div/div/button")
        if len(logout_button) > 0:
            logout_button[0].click()
        else:
            assert len(logout_button) > 0, "Element Not Found !!"

    def assert_url(self):
        expected_url = "https://testing-assessment-foh15kew9-edvora.vercel.app"
        curr_url = self.driver.current_url
        assert expected_url == curr_url, "Failed to logout because logout button not functioning"
        print("Logout function working perfectly")