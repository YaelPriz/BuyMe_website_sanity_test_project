from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class HomeScreen(BasePage):
    # Locators
    PRICE_COMBOBOX = (By.CSS_SELECTOR, 'span[title="סכום"]')
    REGION_COMBOBOX = (By.CSS_SELECTOR, 'span[title="אזור"]')
    CATEGORY_COMBOBOX = (By.CSS_SELECTOR, 'span[title="קטגוריה"]')
    FIND_PRESENT_BUTTON = (By.CSS_SELECTOR, f'a[href^="https://buyme.co.il/search"]')
    MAIL_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="מייל"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="סיסמה"]')
    ENTER_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PRICE_POINT = (By.CSS_SELECTOR, f'li[value="1"]')  # By value of first option
    REGION = (By.CSS_SELECTOR, f'li[value="11"]')  # By value of first option
    CATEGORY = (By.CSS_SELECTOR, f'li[value="438"]')  # By value of first option

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login")
    def login(self, mail, password):
        self.enter_text(self.MAIL_INPUT, mail)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.ENTER_BUTTON)

    @allure.step("Step 1: Pick price point")
    def pick_price_point(self):
        # Click to open the price dropdown
        self.click_element(self.PRICE_COMBOBOX)
        # click to select the specific option in the dropdown by its value
        self.click_element(self.PRICE_POINT)

    @allure.step("Step 2: Pick region")
    def pick_region(self):
        # Click to open the region dropdown
        self.click_element(self.REGION_COMBOBOX)
        # click to select the specific option in the dropdown by its value
        self.click_element(self.REGION)

    @allure.step("Step 3: Pick category")
    def pick_category(self):
        # Click to open the category dropdown
        self.click_element(self.CATEGORY_COMBOBOX)
        # click to select the specific option in the dropdown by its value
        self.click_element(self.CATEGORY)

    @allure.step("Step 4: Click Find Me a Present")
    def click_find_present(self):
        self.click_element(self.FIND_PRESENT_BUTTON)
