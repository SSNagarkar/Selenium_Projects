import time
from logging import getLogger

import pytest
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
class Test(BaseClass):
    def test_e2e(self, loadTestData):
        logs = self.getLogger()

        ProductPage = Products(self.driver)
        wait = WebDriverWait(self.driver, 10)

        # self.driver.execute_script("window.scrollTo(0, 0)")
        # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'messages']/div/div")))
        ProductPage.getCartDetails().click()
        # message = ProductPage.getMessage()
        # message_text = message.text
        #
        # assert "Juliana Short-Sleeve Tee" in message_text

        ProductPage.checkoutCart().click()

        # Shipping Page
        ShippingPage = Shipping_Details(self.driver)

        ShippingPage.getStreetAddress().send_keys(loadTestData["address"])
        ShippingPage.getCity().send_keys(loadTestData["city"])

        region = Select(ShippingPage.getRegion())
        region.select_by_value('12')

        zip = ShippingPage.getPostCode().send_keys(loadTestData["zip"])
        ShippingPage.getPhone().send_keys(loadTestData["phone_number"])
        # logs.info("Entered address as  : " + loadTestData["address"])
        # logs.info("Entered city as  : " + loadTestData["city"])
        # logs.info("Entered zip as  : " + loadTestData["zip"])
        # logs.info("Entered phone number as  : " + loadTestData["phone_number"])
        ShippingPage.getShippingMethod().click()

        ShippingPage.clickNext().click()
        time.sleep(5)

        #wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']/span[text("
             #                                                           ")='Place Order']")))
        self.driver.save_screenshot("screenshot.png")
        ShippingPage.placeOrder().click()

        success = ShippingPage.getSuccessMsg().text

        assert "Thank you for your purchase" in success
        logs.info("Purchased successfully")

        order_details = ShippingPage.getOrderDetails().text
        print(order_details)

    @pytest.fixture(scope="class", params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param





















