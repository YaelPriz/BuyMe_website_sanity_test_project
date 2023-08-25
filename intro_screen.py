from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class IntroScreen(BasePage):
    # Locators
    ENTER_SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="כניסה / הרשמה"]')
    TO_SUBSCRIBE_LINK = (By.CSS_SELECTOR, 'span.text-link[andijvyfh="true"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="שם"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.ID, 'valPass')
    REENTER_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-parsley-equalto="#valPass"]')
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, 'button[type="submittt"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Step 1: Enter website")
    def enter_website(self):
        self.driver.get(self.url)

    @allure.step("Step 2: Click Enter / Subscribe")
    def click_enter_subscribe(self):
        self.click_element(self.ENTER_SUBSCRIBE_BUTTON)

    @allure.step("Step 3: Click to Subscribe link")
    def click_to_subscribe(self):
        self.click_element(self.TO_SUBSCRIBE_LINK)

    @allure.step("Step 4: Enter first name")
    def enter_name(self, username):
        self.enter_text(self.NAME_INPUT, username)

    @allure.step("Step 5: Enter valid email address")
    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    @allure.step("Step 6: Enter password")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    @allure.step("Step 7: RE-Enter password")
    def reenter_password(self, password):
        self.enter_text(self.REENTER_PASSWORD_INPUT, password)

    @allure.step("Step 8: Click subscribe")
    def click_subscribe(self):
        self.click_element(self.SUBSCRIBE_BUTTON)

    @allure.step("Step 9: Assert first name field")
    def get_name_value(self):
        return self.get_value(self.NAME_INPUT)
