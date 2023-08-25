from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class HomeScreen(BasePage):
    # Locators
    PRICE_COMBOBOX = (By.CSS_SELECTOR, 'span[title="סכום"]')
    REGION_COMBOBOX = (By.CSS_SELECTOR, 'span[title="אזור"]')
    CATEGORY_COMBOBOX = (By.CSS_SELECTOR, 'span[title="קטגוריה"]')
    FIND_PRESENT_BUTTON = (By.CSS_SELECTOR, 'a[href="https://buyme.co.il/search"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Step 1: Pick price point")
    def pick_price_point(self, value):
        self.select_option_by_value(self.PRICE_COMBOBOX, value)

    @allure.step("Step 2: Pick region")
    def pick_region(self, value):
        self.select_option_by_value(self.REGION_COMBOBOX, value)

    @allure.step("Step 3: Pick category")
    def pick_category(self, value):
        self.select_option_by_value(self.CATEGORY_COMBOBOX, value)

    @allure.step("Step 4: Click Find Me a Present")
    def click_find_present(self):
        self.click_element(self.FIND_PRESENT_BUTTON)
