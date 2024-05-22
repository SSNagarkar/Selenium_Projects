import pytest

from pom.test_Account import Account
from utilities.base_file import BaseClass


# @pytest.mark.skip
class TestAccountCreation(BaseClass):

    def test_createAccount(self):
        logs = self.getLogger()

        # Account Creation Page Tests
        AccountPage = Account(self.driver)
        AccountPage.accountCreation().click()
        first_name = AccountPage.getFirstName().send_keys("Tina")
        last_name = AccountPage.getLastName().send_keys("Mat")
        email_id = AccountPage.getEmail().send_keys("tina@gmail.com")
        password = AccountPage.getPassword().send_keys("tinaa@123")
        confirm_password = AccountPage.getConfirmPassword().send_keys("tinaa@123")
        AccountPage.submitAccount().click()
        logs.info("Account created successfully")
