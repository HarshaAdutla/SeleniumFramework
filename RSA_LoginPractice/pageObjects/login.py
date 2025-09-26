from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")


    def login(self, username, password):
        """This will return the object for shop page."""
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")    # If we are working in one url then we can keep it in the conftest file.
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page