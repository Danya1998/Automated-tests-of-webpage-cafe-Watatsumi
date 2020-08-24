from pages.base_page import BasePage
from pages.locators.registrationauthorization_locator import RegistrationAuthorizationPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class RegistrationAuthorizationPage(BasePage):
    def __init__(self, driver):
        """Initialize driver and objects to works with 'Registration-Authorization' page.

        :param driver: Remote
        """
        super().__init__(driver)

    def go_to_registration_page(self) -> WebElement:
        """Method which go to Rolls page.

        :return:WebElement
        """
        return self._driver.get("https://watatsumi.com.ua/my-account/")

    def authorization_form(self, login: str, password: str) -> None:
        """Method which fill authorization form

        :param: string
        :param: string
        :return:None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_USERNAME).send_keys(
            login)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_PASSWORD).send_keys(
            password)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_SUBMIT_BUTTON).click()

    def get_authorize_user_name(self) -> str:
        """Method which get name of user which authorized on website.

        :return: string
        """
        user = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located
                                                    (RegistrationAuthorizationPageLocators.LOCATOR_AUTHORIZED_USER))
        return user.text

    def registration_form(self, email, password) -> None:
        """Method which fill registration form.

        :return: None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_EMAIL).send_keys(email)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_REGISTRATION_PASSWORD).send_keys(
            password)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_REGISTRATION_BUTTON)

    def log_out_from_account(self) -> None:
        """Method which log out from user account.

        :return: None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_LOG_OUT).click()


