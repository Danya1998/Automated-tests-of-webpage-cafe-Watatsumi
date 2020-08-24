from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators.pizzapage_locator import PizzaPageLocators


class PizzaPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Pizza' page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.product_list = []

    def go_to_pizza_page(self) -> WebElement:
        """Method which go to Pizza page.

        :return:WebElement
        """
        return self._driver.get("https://watatsumi.com.ua/product-category/pizza/")

    def generate_product_list(self) -> list:
        """Fills product_list with PropertyOfProduct class instances.
        This method must be called before you start working with product methods.

        :return: list of PropertyOfProduct class instances
        """
        products = self._driver.find_elements(*PizzaPageLocators.LOCATOR_PRODUCTS)
        for product in products:
            self.product_list.append(PropertyOfProduct(product))
        return self.product_list

    def get_products_name_list(self) -> list:
        """Method which returns list with name of product.

        :return: list
        """
        products_name_list = []
        for product in self.product_list:
            products_name_list.append(product.get_name())
        return products_name_list

    def add_product_to_shopping_cart(self, product_name: str) -> None:
        """Method which add appointed product to the cart.

         :param: string
         :return: None
         """
        for product in self.product_list:
            if product.get_name() == product_name:
                product.click_add_to_cart()

    def catch_message(self) -> str:
        """Method which catch message when added product to shopping cart.

        :return: string
        """
        message = WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable
                                                        (PizzaPageLocators.LOCATOR_MESSAGE_ADD_TO_CART))
        return message.text


class PropertyOfProduct:
    def __init__(self, product: WebElement) -> None:
        """Initialise the property of a product.

        :param product: WebElement
        """
        self._product = product

    def get_name(self) -> str:
        """Method which get product name.

        :return: string
        """
        return self._product.find_element(*PizzaPageLocators.LOCATOR_PRODUCT_NAME).text

    def click_add_to_cart(self) -> None:
        """Method which add item to the cart.

        :return:None
        """
        self._product.find_element(*PizzaPageLocators.LOCATOR_ADD_TO_CART).click()
