from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from allure_commons.types import AttachmentType
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Load configuration from config.json
    json_file = open('config.json', 'r')
    data = json.load(json_file)
    browser = data['browserType']
    url = data['websiteURL']
    # Check browser type and create driver instance
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service("C:\Yael\Python\chromedriver-win64\chromedriver.exe"))
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            service=Service('C:\Yael\Python\geckodriver-v0.33.0-win-aarch64\geckodriver.exe'))
    else:
        raise ValueError("Unsupported browser type")

    def element_not_found_screenshot(self):
        timestamp = int(time.time())
        screenshot_path = f"element_not_found_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)

        allure.attach(self.driver.get_screenshot_as_png(), name="Element Not Found Screenshot",
                      attachment_type=AttachmentType.PNG)

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException) as e:
            self.element_not_found_screenshot()
            raise e

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def get_value(self,locator):
        element = self.wait_for_element(locator)
        return element.get_attribute("value")


