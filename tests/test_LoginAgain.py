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


@pytest.mark.usefixtures("signIn")
class TestLogin(BaseClass):
    def test_login(self, loadTestData):
        ProductPage = Products(self.driver)
        wait = WebDriverWait(self.driver, 10)
        ProductPage.getCartDetails().click()

        ProductPage.checkoutCart().click()

        # Shipping Page
        ShippingPage = Shipping_Details(self.driver)

        old_address = ShippingPage.getOldAddress()
        if old_address:
            ShippingPage.getOldAddressShippingMethod().click()
            ShippingPage.clickNext().click()

            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text("
                                                                              ")='Place Order']")))

            ShippingPage.placeOrder().click()


            order_details = ShippingPage.getOrderDetails().text
            print(order_details)

            success = ShippingPage.getSuccessMsg().text

            assert "Thank you for your purchase" in success

            order_details = ShippingPage.getOrderDetails().text
            print(order_details)

    @pytest.fixture(scope="class", params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param





















