import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)

    driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()
