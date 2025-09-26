import time

import pytest
from selenium.webdriver.common.by import By


# Here in this script I am using another website for testing.



def test_dummy(browser_instance):
    driver = browser_instance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "inputUsername").send_keys("nomail@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='inputPassword']").send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "logout-btn").click()
    time.sleep(2)




"""
class MyStudent:

    def __init__(self):
        myNewValue = "Nothing"

    def my_function(self):
        print(self.myNewValue)

obj = MyStudent()
obj.my_function()

"""