from behave_webdriver.steps import *
from pages.registration_authorization import RegistrationAuthorizationPage
from pages.pizza_page import PizzaPage
from pages.checkout_page import CheckoutPage
from pages.rolls_page import RollsPage
from testData.constants import *


@given('website "{url}"')
def step(context, url):
    context.browser.get(url)


@then('I go to user authorization page')
def step(context):
    context.authorization_page = RegistrationAuthorizationPage(context.browser)
    context.authorization_page.go_to_registration_page()


@then('Login with username "{login}" and password "{password}"')
def step(context, login, password):
    context.authorization_page.authorization_form(login, password)


@then('Verify that I registered on website with username "{username}"')
def step(context, username):
    assert context.authorization_page.get_authorize_user_name() == username


@then('Go to pizza page, add "{product}" to shopping cart and check successful message')
def step(context, product):
    context.pizza_page = PizzaPage(context.browser)
    context.pizza_page.go_to_pizza_page()
    context.pizza_page.generate_product_list()
    context.pizza_page.add_product_to_shopping_cart(product)
    assert context.pizza_page.catch_message() == PizzaPageConstants.SUCCESSFUL_MESSAGE_ITEM_1


@then('Go to rolls page, add "{product}" to shopping cart and check successful message')
def step(context, product):
    context.rolls_page = RollsPage(context.browser)
    context.rolls_page.go_to_rolls_page()
    context.rolls_page.generate_product_list()
    context.rolls_page.add_product_to_shopping_cart(product)
    assert context.rolls_page.catch_message() == RollsPageConstants.SUCCESSFUL_MESSAGE_ITEM_2


@then('Go to checkout page and check that first product "{product}" is added to order')
def step(context, product):
    context.checkout_page = CheckoutPage(context.browser)
    context.checkout_page.go_to_checkout_page()
    assert context.checkout_page.your_order.check_product_in_shopping_cart(product) is True


@then('Go to checkout page and check that second product "{product}" is added to order')
def step(context, product):
    context.checkout_page.go_to_checkout_page()
    assert context.checkout_page.your_order.check_product_in_shopping_cart(product) is True


@then('Log out from account')
def step(context):
    context.authorization_page.go_to_registration_page()
    context.authorization_page.log_out_from_account()
