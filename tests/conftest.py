import pytest
from selenium import webdriver

from data.test_dataLoad import DataLoader
from pom.test_Products import Products
from pom.test_Signin import SignIn

driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def config(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def signIn(request, config, loadTestData):
    # SignIn Page Tests
    SigninPage = SignIn(driver)

    SigninPage.signInAccount().click()
    SigninPage.enterEmail().send_keys(loadTestData["email"])
    SigninPage.enterPassword().send_keys(loadTestData["password"])
    SigninPage.clickLogin().click()
    # logs.info("LoggedIn successfully")
    # logs.info("Email Id entered : " + loadTestData["email"])
    # logs.info("Password  entered : " + loadTestData["password"])
    SigninPage.clickYogaButton().click()

    # Display Item Page Tests
    ProductPage = Products(driver)

    products = ProductPage.getProductDetails()

    for product in products:
        product_name = ProductPage.getProductName(product).text
        if product_name == loadTestData["product_name"]:
            # logs.info("Product selected : " + loadTestData["product_name"])
            ProductPage.getProductName(product).click()
            ProductPage.getProductSize().click()
            ProductPage.getProductColor().click()
            break
    yield


@pytest.fixture(scope="class", params=DataLoader.test_data)
def loadTestData(self, request):
    return request.param