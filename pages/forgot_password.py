from pages.base_page import BasePage
from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.forgotpasswordpage_locator import ForgotPasswordLocators
from selenium.webdriver.remote.webelement import WebElement


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Forgot Password' page.

        :param driver: Remote
        """
        super().__init__(driver)

    def go_to_forgot_password_page(self) -> WebElement:
        """Method which go to Forgot Password page.

        :return:WebElement
        """
        self._driver.get("https://watatsumi.com.ua/my-account/lost-password/")

    def forgot_password_form(self, data: str) -> None:
        """Method which fills the form to Forgot Password Page.

        :param: string
        :return: None
        """
        self._driver.find_element(*ForgotPasswordLocators.LOCATOR_USERNAME).send_keys(data)
        self._driver.find_element(*ForgotPasswordLocators.LOCATOR_FORGOT_PASSWORD_BUTTON).click()

    def catch_message_success(self) -> str:
        """Method which catch successful message about sending message to email.

        :return:string
        """
        message = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located
                                                       (ForgotPasswordLocators.LOCATOR_MESSAGE_SUCCESS))
        return message.text

    def catch_message_fail(self) -> str:
        """Method which catch unsuccessful message about sending message to email.

        :return:string
        """
        message = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located
                                                       (ForgotPasswordLocators.LOCATOR_MESSAGE_FAIL))
        return message.text

