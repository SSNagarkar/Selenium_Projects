from selenium.webdriver.common.by import By


class Account:

    def __init__(self, driver):
        self.driver = driver

    create_account = (By.LINK_TEXT, "Create an Account")
    first_name = (By.ID, "firstname")
    last_name = (By.ID, "lastname")
    email = (By.CSS_SELECTOR, "#email_address")
    password = (By.CSS_SELECTOR, "#password")
    confirm_password = (By.CSS_SELECTOR, "#password-confirmation")
    submit_button = (By.XPATH, "//button[@class= 'action submit primary']/span")

    def accountCreation(self):
        return self.driver.find_element(*Account.create_account)

    def getFirstName(self):
        return self.driver.find_element(*Account.first_name)

    def getLastName(self):
        return self.driver.find_element(*Account.last_name)

    def getEmail(self):
        return self.driver.find_element(*Account.email)

    def getPassword(self):
        return self.driver.find_element(*Account.password)

    def getConfirmPassword(self):
        return self.driver.find_element(*Account.confirm_password)

    def submitAccount(self):
        return self.driver.find_element(*Account.submit_button)
