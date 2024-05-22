import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.test_dataLoad import DataLoader
from pom.test_Products import Products
from pom.test_Signin import SignIn
from utilities.base_file import BaseClass


# @pytest.mark.skip
class TestWishList(BaseClass):
    def test_wishListFeature(self, loadTestData):
        # SignIn Page Tests
        SigninPage = SignIn(self.driver)

        SigninPage.signInAccount().click()
        SigninPage.enterEmail().send_keys(loadTestData["email"])
        SigninPage.enterPassword().send_keys(loadTestData["password"])
        SigninPage.clickLogin().click()
        # logs.info("LoggedIn successfully")
        # logs.info("Email Id entered : " + loadTestData["email"])
        # logs.info("Password  entered : " + loadTestData["password"])
        SigninPage.clickYogaButton().click()

        # Display Item Page Tests
        ProductPage = Products(self.driver)

        products = ProductPage.getProductDetails()

        for product in products:
            product_name = ProductPage.getProductName(product).text
            if product_name == loadTestData["product_name"]:
                # logs.info("Product selected : " + loadTestData["product_name"])
                ProductPage.getProductName(product).click()
                ProductPage.getProductSize().click()
                ProductPage.getProductColor().click()
                ProductPage.addToCart().click()
                # logs.critical("Product added to cart")
                break
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "ol[class = 'products list "
                                                                                       "items product-items'] li")))
        self.driver.execute_script("window.scrollTo(0, 0)")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'messages']/div/div")))
        ProductPage.getCartDetails().click()
        message = ProductPage.getMessage()
        message_text = message.text

        assert "Fiona Fitness Short" in message_text

        ProductPage.addToWishList().click()
        wishlist_msg = ProductPage.getWishListMsg().text

        assert "Fiona Fitness Short has been added to your Wish List" in wishlist_msg

        ProductPage.shareWishList().click()
        ProductPage.shareToEmail().send_keys("samy@gmail.com")
        ProductPage.shareToMsg().send_keys("This can be a gift for you")
        ProductPage.clickShareButton().click()
        share_success_msg = ProductPage.shareSuccessMsg().text

        assert "our wish list has been shared" in share_success_msg

    @pytest.fixture(params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param
