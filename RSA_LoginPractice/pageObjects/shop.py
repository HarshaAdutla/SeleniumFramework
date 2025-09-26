import time

from selenium.webdriver.common.by import By


from pageObjects.checkoutconfirmation import CheckoutConfirmation


class ShopPage:


    def __init__(self, driver):
        self.driver = driver
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.product_name = (By.XPATH, "div/h4/a")
        self.add_to_cart_button = (By.XPATH, "div/button")
        self.checkout_button = (By.CSS_SELECTOR, ".btn-primary")


    def shopping(self, mobile_name):
        """Performs the shopping, adding items to the cart."""
        all_products = self.driver.find_elements(*self.products)

        for product in all_products:
            item_name = product.find_element(*self.product_name).text       # For Product name we can keep the locator in here also. Bcz we are not
            # performing any action on it. But I modified here.
            if item_name == mobile_name:
                product.find_element(*self.add_to_cart_button).click()  # Add to cart button. This also no need to modify we can keep the
                # exact locator right here itself.
                time.sleep(3)


    def go_to_cart(self):
        """This will return the object for cart page."""
        """Take you to the Cart Page."""            # This is an action that's why i have created a new function for this.
        self.driver.find_element(*self.checkout_button).click()  # Cart Icon/Check out icon on shop page.
        final_page = CheckoutConfirmation(self.driver)
        return final_page
