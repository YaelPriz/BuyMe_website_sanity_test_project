from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class PickBusinessScreen(BasePage):
    # Locators and constants
    WEBSITE_URL = "https://buyme.co.il/search?budget=1&category=438&region=11"
    BUSINESS = (By.CSS_SELECTOR, 'a[aria-label*="מסעדות בנדיקט"]')
    PRICE_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="סכום"]')
    SELECT_BUTTON = (By.XPATH, '//button[@type="submit" and @gtm="בחירה"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Assert website URL")
    def assert_url(self):
        current_url = BasePage.driver.current_url
        assert current_url == self.WEBSITE_URL

    @allure.step("Pick business")
    def pick_business(self):
        self.click_element(self.BUSINESS)

    @allure.step("Enter price")
    def enter_price(self, price):
        self.enter_text(self.PRICE_INPUT, price)

    @allure.step("Click select")
    def click_select(self):
        self.click_element(self.SELECT_BUTTON)

