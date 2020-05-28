import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install());
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
assert "dashboard" in driver.current_url
driver.close()
driver.quit()
