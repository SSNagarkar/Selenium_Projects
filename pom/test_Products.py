from selenium.webdriver.common.by import By


class Products:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//li[@class = 'item product product-item']")
    product_name = (By.XPATH, "div/div/strong")

    # product_name = (By.CSS_SELECTOR, ".product-item-link")
    product_info = (By.XPATH, "//ol[@class='products list items product-items']/li[5]/div")
    product_size = (By.XPATH, "//div[@id='product-options-wrapper']/div/div/div[1]/div/div[2]")
    product_colour = (By.XPATH, "//div[@id='product-options-wrapper']/div/div/div[2]/div/div[2]")
    product_qty = (By.ID, "qty")
    add_button = (By.CSS_SELECTOR, "#product-addtocart-button")
    cart_button = (By.CSS_SELECTOR, "span[class='counter-number']")
    checkout_cart = (By.ID, "top-cart-btn-checkout")
    message = (By.XPATH, "//div[@class = 'messages']/div/div")
    wishlist = (By.XPATH, "//div[@class='product-social-links']/div/a[1]/span")
    wishlist_message = (By.XPATH, "//div[@class= 'messages']/div/div")
    share_wishlist = (By.XPATH, "//button[@name='save_and_share']")
    share_to_email = (By.CSS_SELECTOR, "#email_address")
    share_to_msg = (By.ID, "message")
    share_button = (By.XPATH, "//div[@class='primary']/button/span[text() ='Share Wish List']")
    share_success_msg = (By.XPATH, "//div[@class='messages']/div/div")
    compare = (By.XPATH, "//div[@class='product-social-links']/div/a[2]/span")
    compare_msg = (By.XPATH, "//div[@class='messages']/div/div")
    comparison_list = (By.XPATH, "//div[@class='messages']/div/div/a")
    compare_product_name = (By.LINK_TEXT, "Juliana Short-Sleeve Tee")

    def getProductDetails(self):
        return self.driver.find_elements(*Products.products)

    def getProductName(self, product):
        return product.find_element(*Products.product_name)

    def getProductInfo(self):
        return self.driver.find_element(*Products.product_info)

    def getProductSize(self):
        return self.driver.find_element(*Products.product_size)

    def getProductColor(self):
        return self.driver.find_element(*Products.product_colour)

    def getProductQty(self):
        return self.driver.find_element(*Products.product_qty)

    def addToCart(self):
        return self.driver.find_element(*Products.add_button)

    def getCartDetails(self):
        return self.driver.find_element(*Products.cart_button)

    def checkoutCart(self):
        return self.driver.find_element(*Products.checkout_cart)

    def getMessage(self):
        return self.driver.find_element(*Products.message)

    def addToWishList(self):
        return self.driver.find_element(*Products.wishlist)

    def getWishListMsg(self):
        return self.driver.find_element(*Products.wishlist_message)

    def shareWishList(self):
        return self.driver.find_element(*Products.share_wishlist)

    def shareToEmail(self):
        return self.driver.find_element(*Products.share_to_email)

    def shareToMsg(self):
        return self.driver.find_element(*Products.share_to_msg)

    def clickShareButton(self):
        return self.driver.find_element(*Products.share_button)

    def shareSuccessMsg(self):
        return self.driver.find_element(*Products.share_success_msg)

    def addToCompare(self):
        return self.driver.find_element(*Products.compare)

    def getCompareMsg(self):
        return self.driver.find_element(*Products.compare_msg)

    def goToComparisonList(self):
        return self.driver.find_element(*Products.comparison_list)

    def getComparedProductItemName(self):
        return self.driver.find_element(*Products.compare_product_name)








