# From here onwards we are building a framework by using fixtures and page object model(POM).
# This will include
    # Avoiding Hard-coding test data,
    # Using external Test data,
    # Implementing POM,
    # Centralized Reusable code,
    # Defining global Environment variables,
    # Applying Grouping/Tags to run targeted test and running test in parallel mode,
    # Generating HTML Reports,
    # Capture Logs & Screenshots,
    # CI/CD Integration.
import os.path
import sys

# I am using 'TC_21_end_to_end.py' (SeleniumTests) to build the framework.


from pageObjects.login import LoginPage
username = "rahulshettyacademy"
password = "learning"
mobile_name = "Blackberry"
country_name = "Ind"

def test_e2e(browser_instance):
    driver = browser_instance

    login_page = LoginPage(driver)
    shop_page = login_page.login(username, password)      # Capturing the object for shop page.

    # Here One Pop up is displayed but not able to interact with it. so commenting this code.
    # try:
    #     alert = driver.switch_to.alert      # Alert didn't appear in the normal flow but in the automation. And also the alert is not accessible.
    #     alert.accept()
    # except NoAlertPresentException:
    #     print("Alert didn't appeared")

    shop_page.shopping(mobile_name)
    final_page = shop_page.go_to_cart()  # Capturing the object fot the cart page.
    final_page.checkout()   # Capturing the object for the success page.
    final_page.enter_delivery_address(country_name)
    message = final_page.validation()
    print(message)
    assert "Success" in message
    print("Assertion Success.")








