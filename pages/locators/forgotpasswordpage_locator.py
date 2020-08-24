from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    """Locators for Forgot Password Page."""

    LOCATOR_USERNAME = (By.NAME, "user_login")
    LOCATOR_FORGOT_PASSWORD_BUTTON = (By.CLASS_NAME, "woocommerce-Button")
    LOCATOR_MESSAGE_SUCCESS = (By.CLASS_NAME, "woocommerce-message")
    LOCATOR_MESSAGE_FAIL = (By.CLASS_NAME, "woocommerce-error")
