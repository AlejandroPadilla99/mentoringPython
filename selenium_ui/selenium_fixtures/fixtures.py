#lib
import pytest

#local
from selenium_ui.pages.base_page import BasePage
from selenium_ui.pages.main_page import MainPage
from selenium_ui.pages.sign_up import SingUpPage
from selenium_ui.pages.register_page import RegisterPage
from selenium_ui.pages.shopping_cart_page import ShoppingCartPage
from selenium_ui.pages.payment_details_page import PaymentDetailsPages
from selenium_ui.pages.order_page import OderPage
from selenium_ui.pages.user_information_page import UserInformation

from selenium_ui.utilities_selenium.user_utilities_se import User


@pytest.fixture
def base():
    return  BasePage()

@pytest.fixture
def main():
    return MainPage()

@pytest.fixture
def sign_up():
    return SingUpPage()

@pytest.fixture
def register():
    return RegisterPage()

@pytest.fixture
def shopping_cart():
    return ShoppingCartPage()

@pytest.fixture
def payment_details():
    return  PaymentDetailsPages()

@pytest.fixture
def order_page():
    return OderPage()

@pytest.fixture
def user_information():
    return UserInformation()

@pytest.fixture
def session():
    user = User()

    base = BasePage()
    main = MainPage()
    sign_up = SingUpPage()
    register = RegisterPage()

    base.logout_session() 
    base.return_to_base_page()
    main.sign_in().click()
    sign_up.register().click()
    register.user_id().send_keys(data=user.user_credentials.get('id'), clear=True)
    register.new_password().send_keys(data=user.user_credentials.get('password'), clear=True)
    register.repeat_password().send_keys(data=user.user_credentials.get('password'), clear=True)
    register.first_name().send_keys(data=user.account_data.get('first_name'), clear=True)
    register.last_name().send_keys(data=user.account_data.get('second_name'), clear=True)
    register.email().send_keys(data=user.account_data.get('email'), clear=True)
    register.phone().send_keys(data=user.account_data.get('phone'), clear=True)
    register.address1().send_keys(data=user.account_data.get('address1'), clear=True)
    register.address2().send_keys(data=user.account_data.get('address2'), clear=True)
    register.city().send_keys(data=user.account_data.get('city'), clear=True)
    register.state().send_keys(data=user.account_data.get('state'), clear=True)
    register.zip().send_keys(data=user.account_data.get('zip'), clear=True)
    register.country().send_keys(data=user.account_data.get('country'), clear=True)
    register.language_preference().select_by_value(data=user.profile_data.get('language_preference'))
    register.favourite_category().select_by_value(data=user.profile_data.get('favorite_category'))
    register.mylist().click()
    register.mybanner().click()
    register.save_account().click()
    main.sign_in().click()
    sign_up.username().send_keys(data=user.user_credentials.get('id'), clear=True)
    sign_up.password().clean_text()
    sign_up.password().send_keys(data=user.user_credentials.get('password'), clear=True)
    sign_up.login().click()

    return user
