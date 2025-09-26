from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




def waiting(driver, locator):

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located(locator))

