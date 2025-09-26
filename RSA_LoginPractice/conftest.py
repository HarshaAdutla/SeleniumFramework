import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")



@pytest.fixture(scope="function")
def browser_instance(request):
    """ Invoke Required Browser Instance """
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()

    #  Got this form the chatgpt for Google Chrome password popups which selenium can't handle.
    # But still facing some issue here.

    # options = webdriver.ChromeOptions()
    # prefs = {
    #     "credentials_enable_service": False,
    #     "profile.password_manager_enabled": False
    # }
    # options.add_experimental_option("prefs", prefs)
    #
    # driver = webdriver.Chrome(options=options)

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--run-headless")   # We can run the test in headless mode by using this argument.
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        chrome_options.add_experimental_option("prefs", prefs)

    elif browser_name == 'firefox':
        """
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        
        The firefox won't support --start-maximized we can use the driver.maximize_window() after driver instance.
        """

        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()

    driver.implicitly_wait(5)
    yield driver
    driver.close()





"""
We can pass argument values from the command line options too.
And to use any options we need to register them in the conftest file before we use them.


"""