from selenium.webdriver.common.by import By
from base_page import BasePage
import allure
from constants import Constants


class SenderReceiverScreen(BasePage):
    # Locators and constants
    FOR_BUTTON = (By.XPATH, '//div[@gtm="למישהו אחר"]')
    RECEIVER_NAME_INPUT = (By.CSS_SELECTOR, f'input[aria-label*="שם מקבל"]')
    EVENT_COMBOBOX = (By.CSS_SELECTOR, f'span[title*="אירוע"]')
    BIRTHDAY_EVENT = (By.CSS_SELECTOR, f'li[value="10"]')  # By value of birthday option
    BLESSING_INPUT = (By.CSS_SELECTOR, 'textarea[data-parsley-group="voucher-greeting"]')
    PICTURE_BUTTON = (By.CSS_SELECTOR, 'label[aria-label="העלה מדיה"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, f'button[gtm^="המשך"]')
    SMS_BUTTON = (By.CSS_SELECTOR, '[role="checkbox"][aria-label*="SMS"]')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder^="נייד"]')
    SENDER_INPUT = (By.CSS_SELECTOR, 'input[placeholder*="שולח"]')
    BACK_BUTTON = (By.CSS_SELECTOR, 'span.text-link.theme[role="link"][tabindex="0"]')

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
    def upload_picture(self):
        self.click_element(self.PICTURE_BUTTON)

    @allure.step("Press continue")
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Press now button")
    def select_now(self):
        check_elements = self.driver.find_elements(By.CSS_SELECTOR, '.fill')
        # Select the first element from the list
        if check_elements:
            first_check_element = check_elements[0]
            # Click the circle element to toggle its state
            first_check_element.click()
        else:
            self.element_not_found_screenshot()

    @allure.step("Pick SMS")
    def pick_sms(self):
        self.click_element(self.SMS_BUTTON)

    @allure.step("Enter phone number")
    def enter_phone_number(self, number):
        self.enter_text(self.PHONE_INPUT, number)

    @allure.step("Enter sender name")
    def enter_sender(self, sender):
        element = self.wait_for_element(self.SENDER_INPUT)
        element.clear()
        self.enter_text(self.SENDER_INPUT, sender)

    @allure.step("Click back to reach receiver name")
    def click_back(self):
        self.click_element(self.BACK_BUTTON)

    @allure.step("Assert receiver name")
    def assert_receiver(self):
        receiver_value = self.get_value(self.RECEIVER_NAME_INPUT)
        assert receiver_value == Constants.RECEIVER
