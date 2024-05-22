import time

import pytest
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from data.test_dataLoad import DataLoader
from pom.test_Account import Account
from pom.test_Products import Products
from pom.test_ShippingDetails import Shipping_Details
from pom.test_Signin import SignIn
from utilities.base_file import BaseClass


class TestLogin(BaseClass):
    def test_login(self, loadTestData):

        # SignIn Page Tests
        SigninPage = SignIn(self.driver)

        SigninPage.signInAccount().click()
        SigninPage.enterEmail().send_keys(loadTestData["email"])
        SigninPage.enterPassword().send_keys(loadTestData["password"])
        SigninPage.clickLogin().click()
        SigninPage.clickYogaButton().click()

        # Display Item Page Tests
        ProductPage = Products(self.driver)

        products = ProductPage.getProductDetails()

        for product in products:
            product_name = ProductPage.getProductName(product).text
            if product_name == loadTestData["product_name"]:
                ProductPage.getProductName(product).click()
                ProductPage.getProductSize().click()
                ProductPage.getProductColor().click()
                ProductPage.addToCart().click()
                break
        wait = WebDriverWait(self.driver, 10)

        self.driver.execute_script("window.scrollTo(0, 0)")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'messages']/div/div")))
        ProductPage.getCartDetails().click()
        message = ProductPage.getMessage()
        message_text = message.text

        assert "Juliana Short-Sleeve Tee" in message_text
        ProductPage.checkoutCart().click()

        # Shipping Page
        ShippingPage = Shipping_Details(self.driver)

        old_address = ShippingPage.getOldAddress()
        if old_address:
            ShippingPage.getOldAddressShippingMethod().click()
            ShippingPage.clickNext().click()

            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text("
                                                                              ")='Place Order']")))
            self.driver.save_screenshot('screenshot.png')
            ShippingPage.placeOrder().click()


            order_details = ShippingPage.getOrderDetails().text
            print(order_details)

            success = ShippingPage.getSuccessMsg().text

            assert "Thank you for your purchase" in success

            order_details = ShippingPage.getOrderDetails().text
            print(order_details)

    @pytest.fixture(params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param





















