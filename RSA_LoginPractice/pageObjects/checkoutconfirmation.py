import time

from selenium.webdriver.common.by import By

from utils.waits import waiting




class CheckoutConfirmation:

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn-success")
        self.country_edit_box = (By.ID, "country")
        self.select_country = (By.LINK_TEXT, "India")
        self.element_locator = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.success_button = (By.CSS_SELECTOR, "input[class*='btn-success']")
        self.success_message = (By.CSS_SELECTOR, ".alert-success")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()  # Check out button


    def enter_delivery_address(self, country):
        self.driver.find_element(*self.country_edit_box).send_keys(country)
        waiting(self.driver, self.element_locator)  # Added this waiting in the conftest for repeated use.
        self.driver.find_element(*self.select_country).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.success_button).click()


    def validation(self):
        message = self.driver.find_element(*self.success_message).text
        # self.driver.save_screenshot("full_page.png")
        return message


