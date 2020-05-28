import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import allure

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install());
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

@allure.description("Validate with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_Login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    enter_username("Admin")
    enter_password("admin123")
    driver.find_element_by_id("btnLogin").click()
    time.sleep(3)
    assert "dashboard" in driver.current_url

@allure.description("Validate with Invalid credentials")
@allure.severity(severity_level="NORMAL")
def test_InvalidLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    enter_username("Admin1")
    enter_password("admin12")
    driver.find_element_by_id("btnLogin").click()
    time.sleep(3)
    try:
        assert "dashboard" in driver.current_url
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)

@allure.step("Entering username as {0}")
def enter_username(username):
    driver.find_element_by_id("txtUsername").send_keys(username)

@allure.step("Entering password as {0}")
def enter_password(password):
    driver.find_element_by_id("txtPassword").send_keys(password)