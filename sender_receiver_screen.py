from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class SenderReceiverScreen(BasePage):
    # Locators and constants
    FOR_BUTTON = (By.XPATH, '//div[@gtm="למישהו אחר"]')
    RECEIVER_NAME_INPUT = (By.CSS_SELECTOR, f'input[aria-label*="שם מקבל"]')
    EVENT_COMBOBOX = (By.CSS_SELECTOR, f'span[title*="אירוע"]')
    BIRTHDAY_EVENT = (By.CSS_SELECTOR, f'li[value="10"]')  # By value of birthday option
    BLESSING_INPUT = (By.CSS_SELECTOR, 'textarea[data-parsley-group="voucher-greeting"]')
    PICTURE_BUTTON = (By.CSS_SELECTOR, 'label[aria-label="העלה מדיה"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, f'button[gtm^="המשך"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Press for someone else button")
    def pick_business(self):
        self.click_element(self.FOR_BUTTON)

    @allure.step("Enter receiver name")
    def enter_receiver(self, receiver):
        self.enter_text(self.RECEIVER_NAME_INPUT, receiver)

    @allure.step("Pick an event")
    def pick_event(self):
        # Click to open the event dropdown
        self.click_element(self.EVENT_COMBOBOX)
        # click to select the specific option in the dropdown by its value
        self.click_element(self.BIRTHDAY_EVENT)

    @allure.step("Enter a blessing")
    def enter_blessing(self, blessing):
        element = self.wait_for_element(self.BLESSING_INPUT)
        element.clear()
        self.enter_text(self.BLESSING_INPUT, blessing)

    @allure.step("Upload a picture")
    def enter_blessing(self):
        self.click_element(self.PICTURE_BUTTON)

    @allure.step("Click continue")
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)
