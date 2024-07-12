from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.NAME, 'login_submit')
    REG_FORM = (By.NAME, 'registration_submit')
    LOGIN_URL = 'login'
