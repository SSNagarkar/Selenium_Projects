import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.test_dataLoad import DataLoader
from pom.test_Products import Products
from pom.test_Signin import SignIn
from utilities.base_file import BaseClass


@pytest.mark.usefixtures("signIn")
class TestWishList(BaseClass):
    def test_wishListFeature(self, loadTestData):
        ProductPage = Products(self.driver)
        ProductPage.addToWishList().click()
        wishlist_msg = ProductPage.getWishListMsg().text

        assert "Juliana Short-Sleeve Tee has been added to your Wish List" in wishlist_msg

        ProductPage.shareWishList().click()
        ProductPage.shareToEmail().send_keys("samy@gmail.com")
        ProductPage.shareToMsg().send_keys("This can be a gift for you")
        ProductPage.clickShareButton().click()
        share_success_msg = ProductPage.shareSuccessMsg().text

        assert "our wish list has been shared" in share_success_msg

    @pytest.fixture(scope="class",params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param
