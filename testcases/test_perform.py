import pytest
from pages.login_page import LoginPage
from pages.sign_in import SignInPage
from pages.settings import SettingsPage

@pytest.mark.usefixtures("setup")
class TestPerformActions:

    def test_createAccount(self):
        sp = SignInPage(self.driver)
        sp.go_to_signin()
        sp.enter_user("H1708")
        sp.enter_passwd("H1708")
        sp.create_account()
        sp.assert_url()

    def test_settingsPersonalInfoSave(self):
        setp = SettingsPage(self.driver)
        setp.edit_personal_info()
        setp.fname("Hardik")
        setp.dob("08172001")
        setp.gender("female")
        setp.mobile("9876543210")
        setp.address("subhash nagar")
        setp.save()

    def test_settingsPersonalInfoCancel(self):
        setp = SettingsPage(self.driver)
        setp.back_to_url()
        setp.cancel()

    def test_settingsSecuritySave(self):
        setp = SettingsPage(self.driver)
        setp.edit_security()
        setp.change_password("h1708")
        setp.save_security()

    def test_settingsSecurityCancel(self):
        setp = SettingsPage(self.driver)
        setp.edit_security()
        setp.cancel_security()

    def test_settingsLogout(self):
        setp = SettingsPage(self.driver)
        setp.logout()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.enter_user("H1708")
        lp.enter_password("H1708")
        lp.login()
        lp.assert_url()



