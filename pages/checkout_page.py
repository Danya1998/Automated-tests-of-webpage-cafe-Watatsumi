from pages.base_page import BasePage
from pages.locators.checkoutpage_locator import CheckoutPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Rolls' page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.payment_detail = PaymentDetailsComponent(self._driver)
        self.your_order = YourOrderComponent(self._driver)

    def go_to_checkout_page(self) -> WebElement:
        """Method which go to Checkout page.

        :return:WebElement
        """
        return self._driver.get("https://watatsumi.com.ua/checkout/")


class YourOrderComponent:
    def __init__(self, driver: Remote) -> None:
        """Initialize your order component.

        :param driver: Remote
        :return: None
        """
        self._driver = driver

    def products_in_shopping_cart(self) -> list:
        """Method which returns list of WebElements to work with each product in shopping cart.

        :return: list.
        """
        products_list = []
        products = self._driver.find_elements(*CheckoutPageLocators.LOCATOR_PRODUCTS)
        for product in products:
            products_list.append(product.text)
        return products_list

    def check_product_in_shopping_cart(self, product_in_cart) -> bool:
        """Method which check product in product cart.

        :return: Boolean
        """
        products = self.products_in_shopping_cart()
        for product in products:
            if product == product_in_cart:
                return True


class PaymentDetailsComponent:
    def __init__(self, driver) -> None:
        """Initialize your Payment Detail component.

        :param driver: Remote
        :return: None
        """
        self._driver = driver

    def details_of_purchase(self, your_name, phone, email, house_number, entrance_number, floor_number,
                            apartment_number) -> None:
        """Method which fills form in Payment Detail.

        :return: None
        """

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_YOUR_NAME).send_keys(your_name)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_BILLING_PHONE).send_keys(Keys.CLEAR + phone)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_EMAIL).send_keys(Keys.CLEAR + email)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_STREET).click()
        self._driver.find_element(*CheckoutPageLocators.LOCATOR_CHOOSE_STREET).click()

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_HOUSE).send_keys(Keys.CLEAR + house_number)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_ENTRANCE).send_keys(Keys.CLEAR + entrance_number)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_FLOOR).send_keys(Keys.CLEAR + floor_number)

        self._driver.find_element(*CheckoutPageLocators.LOCATOR_APARTMENT).send_keys(Keys.CLEAR + apartment_number)


