from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('After creating account')
def creatingAccount(context):
    context.driver = webdriver.Chrome()
    context.driver.find_element(By.XPATH, "//ul[@class= 'header links']/li[2]/a")


@when('User enters valid "{email}" and "{password}"')
def enterCredentials(context, email, password):
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "pass").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "button[class='action login primary'] span")

@then('User lands on Products page')
def ProductPage(context):
    pass
