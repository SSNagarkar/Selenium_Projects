import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.test_dataLoad import DataLoader
from pom.test_Products import Products
from pom.test_Signin import SignIn
from utilities.base_file import BaseClass


# @pytest.mark.skip
@pytest.mark.usefixtures("signIn")
class TestCompareProducts(BaseClass):
    def test_compareFeature(self, loadTestData):
        ProductPage = Products(self.driver)

        ProductPage.addToCompare().click()
        compare_msg = ProductPage.getCompareMsg().text

        assert "You added product Juliana Short-Sleeve Tee to the comparison list" in compare_msg

        ProductPage.goToComparisonList().click()
        item_name = ProductPage.getComparedProductItemName().text

        assert "Juliana Short-Sleeve" in item_name

    @pytest.fixture(scope="class", params=DataLoader.test_data)
    def loadTestData(self, request):
        return request.param
