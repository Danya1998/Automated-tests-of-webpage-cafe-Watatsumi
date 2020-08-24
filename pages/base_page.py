from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.

        :param driver: Remote.
        """
        self._driver = driver
        self.base_url = "https://watatsumi.com.ua/"

    def find_element(self, locator: str, time=20) -> WebElement:
        """Method which find elements on page.


        :param:
        :return: WebElement
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: str, time=10) -> WebElement:
        """Method which find elements on page.


        :param: string
        :return: Tuple[WebElements]
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self) -> WebElement:
        """Method which go to the main page.

        :return:WebElement
        """
        return self._driver.get(self.base_url)
