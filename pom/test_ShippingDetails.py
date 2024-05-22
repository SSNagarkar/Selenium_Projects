from selenium.webdriver.common.by import By
class Shipping_Details:

    def __init__(self,driver):
        self.driver = driver

    street_address = (By.CSS_SELECTOR, "input[name='street[0]']")
    city = (By.XPATH, '//input[@name = "city"]')
    region = (By.CSS_SELECTOR, 'select[name="region_id"]')
    postcode = (By.CSS_SELECTOR, "input[name = 'postcode']")
    telephone = (By.CSS_SELECTOR, "input[name='telephone']")
    shipping_method = (By.XPATH, "//input[@name='ko_unique_3']")
    next_button = (By.XPATH, "//button[@class='button action continue primary']")
    place_order = (By.XPATH, "//div[@class = 'actions-toolbar']/div/button/span[text() = 'Place Order']")
    success_msg = (By.CSS_SELECTOR, "div[class='page-title-wrapper'] h1 span")
    order_details = (By.XPATH, "//div[@class='checkout-success']/p[1]")
    old_address_shipping = (By.XPATH, "//input[@name='ko_unique_1']")
    old_address = (By.XPATH, "//div[@class= 'shipping-address-item selected-item']")

    def getStreetAddress(self):
        return self.driver.find_element(*Shipping_Details.street_address)

    def getCity(self):
        return self.driver.find_element(*Shipping_Details.city)

    def getRegion(self):
        return self.driver.find_element(*Shipping_Details.region)

    def getPostCode(self):
        return self.driver.find_element(*Shipping_Details.postcode)

    def getPhone(self):
        return self.driver.find_element(*Shipping_Details.telephone)

    def getShippingMethod(self):
        return self.driver.find_element(*Shipping_Details.shipping_method)

    def clickNext(self):
        return self.driver.find_element(*Shipping_Details.next_button)

    def placeOrder(self):
        return self.driver.find_element(*Shipping_Details.place_order)

    def getSuccessMsg(self):
        return self.driver.find_element(*Shipping_Details.success_msg)

    def getOrderDetails(self):
        return self.driver.find_element(*Shipping_Details.order_details)

    def getOldAddressShippingMethod(self):
        return self.driver.find_element(*Shipping_Details.old_address_shipping)

    def getOldAddress(self):
        return self.driver.find_element(*Shipping_Details.old_address)

