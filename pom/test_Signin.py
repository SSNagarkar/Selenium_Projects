from selenium.webdriver.common.by import By


class SignIn:
    def __init__(self, driver):
        self.driver = driver

    signin = (By.XPATH, "//ul[@class= 'header links']/li[2]/a")
    email = (By.ID, "email")
    password = (By.ID, "pass")
    login = (By.CSS_SELECTOR, "button[class='action login primary'] span")
    yoga_button = (By.CSS_SELECTOR, "span[class= 'action more button']")

    def signInAccount(self):
        return self.driver.find_element(*SignIn.signin)

    def enterEmail(self):
        return self.driver.find_element(*SignIn.email)

    def enterPassword(self):
        return self.driver.find_element(*SignIn.password)

    def clickLogin(self):
        return self.driver.find_element(*SignIn.login)

    def clickYogaButton(self):
        return self.driver.find_element(*SignIn.yoga_button)

