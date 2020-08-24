from selenium.webdriver.common.by import By


class RegistrationAuthorizationPageLocators:
    """Locators for Registration-Authorization Page."""

    LOCATOR_USERNAME = (By.NAME, "username")
    LOCATOR_PASSWORD = (By.NAME, "password")
    LOCATOR_SUBMIT_BUTTON = (By.NAME, "login")
    LOCATOR_AUTHORIZED_USER = (By.XPATH, "//div[@class='myaccount_user']/p[@class='h5']/strong")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='myaccount_user']/p[@class='h5']/a")
    LOCATOR_REGISTRATION_PASSWORD = (By.ID, "reg_password")
    LOCATOR_EMAIL = (By.ID, "reg_email")
    LOCATOR_REGISTRATION_BUTTON = (By.NAME, "register")
