from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    """Locators for Checkout Page."""
    LOCATOR_PRODUCTS = (By.XPATH, "//table/tbody/tr/td[@class='product-name']")
    ADD_TO_CART = (By.CLASS_NAME, "add_to_cart_button")
    LOCATOR_YOUR_NAME = (By.XPATH, "//input[@id='billing_first_name']")
    LOCATOR_BILLING_PHONE = (By.XPATH, "//input[@id='billing_phone']")
    LOCATOR_EMAIL = (By.XPATH, "//input[@id='email']")
    LOCATOR_STREET = (By.ID, "select2-str-container")
    LOCATOR_CHOOSE_STREET = (By.XPATH, "//ul[@class='select2-results__options']/li[2]")
    LOCATOR_HOUSE = (By.XPATH, "//input[@id='house']")
    LOCATOR_ENTRANCE = (By.XPATH, "//input[@id='entr']")
    LOCATOR_FLOOR = (By.XPATH, "//input[@id='floor']")
    LOCATOR_APARTMENT = (By.XPATH, "//input[@id='apart']")
    LOCATOR_FIELDS_DETAIL_PURCHASE = (By.XPATH, "//div[@class='woocommerce-billing-fields']/div/p/span/input")
