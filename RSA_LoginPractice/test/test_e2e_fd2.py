import json

import pytest


# Here I am using rhe test_e2e_fd.py file, but I am adding data parametrization to it.

# We can see that I have defined all the data which is username, password, product name and country name are defined as variables in this script only.
# Now I am going to define all the data in one json file and I will read that file in here so the script will become more clean.
# We are hard coding anything in the script anymore.
# For that I have created a new directory called data in the framework design folder.
# We will be having more and more test cases right, so I am naming the data file same as test script so that we can see data set is fot which test
# case.

# We know how to read files in python right. So I am reading the file using file operations.



from pageObjects.login import LoginPage




test_data_path = "data/test_e2e_fd2.json"
# test_data_path = "/Users/harsha/PycharmProjects/Python Selenium Test/framework_design/data/test_e2e_fd2.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# In the test data json file we have defined two sets of data which means test will run two times.
# To run like this(with two data sets) we need to make sure that the test should be able to handle the two data sets.
# These two sets are called two test data parameters. So we need to use the parametrization to run test like this.
# Like we define the fixtures we have parametrization in the pytest so we can use that like below.
# I am applying parametrization to my test here
# When we define the parametrization we need to pass that to the test function as well.


@pytest.mark.parametrize("test_data_list", test_list)
def test_e2e(browser_instance, test_data_list):
    driver = browser_instance

    login_page = LoginPage(driver)
    shop_page = login_page.login(test_data_list["userEmail"], test_data_list["userPassword"])      # Capturing the object for shop page.

    # Here One Pop up is displayed but not able to interact with it. so commenting this code.
    # try:
    #     alert = driver.switch_to.alert      # Alert didn't appear in the normal flow but in the automation. And also the alert is not accessible.
    #     alert.accept()
    # except NoAlertPresentException:
    #     print("Alert didn't appeared")

    shop_page.shopping(test_data_list["productName"])
    final_page = shop_page.go_to_cart()  # Capturing the object fot the cart page.
    final_page.checkout()   # Capturing the object for the success page.
    final_page.enter_delivery_address(test_data_list["countryName"])
    message = final_page.validation()
    print(message)
    assert "Success" in message
    print("Assertion Success.")








