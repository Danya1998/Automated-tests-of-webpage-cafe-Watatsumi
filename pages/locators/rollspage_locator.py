from selenium.webdriver.common.by import By


class RollsPageLocators:
    """Locators for Rolls Page."""

    LOCATOR_PRODUCTS = (By.XPATH, "//div[@class='container']/ul/li")
    LOCATOR_PRODUCT_NAME = (By.XPATH, "div/div/h3/a")
    LOCATOR_ADD_TO_CART = (By.XPATH, "div/div/div[@class='recentCart']/a")
    LOCATOR_MESSAGE_ADD_TO_CART = (By.CLASS_NAME, "message_cart")
