from unittest import TestCase
from intro_screen import IntroScreen
from home_screen import HomeScreen
from constants import Constants
import logging
from base_page import BasePage
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(
                    filename='../logfile.log', # set the output file
                    filemode='a',  # set it to append rather than overwrite
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    # determine the format of the output message
                    datefmt='%H:%M:%S',  # determine the format of the output time
                    level=logging.ERROR)  # determine the minimum message level it will accept


class TestClass(TestCase):
    def test_intro_screen(self):
        intro = IntroScreen(BasePage.driver)  # Create an instance of IntroScreen
        intro.enter_website()
        intro.click_enter_subscribe()
        intro.click_to_subscribe()
        intro.enter_name(Constants.USERNAME)
        intro.enter_email(Constants.EMAIL)
        intro.enter_password(Constants.PASSWORD)
        intro.reenter_password(Constants.PASSWORD)
        intro.click_subscribe()
        name_value = intro.get_name_value()
        assert name_value == Constants.USERNAME
        intro.fill_agree()

    def test_home_screen(self):
        intro = IntroScreen(BasePage.driver)  # Create an instance of IntroScreen
        intro.enter_website()
        intro.click_enter_subscribe()
        home = HomeScreen(BasePage.driver)  # Create an instance of HomeScreen
        time.sleep(2) # Wait for 2 seconds
        home.login(Constants.MAIL, Constants.PASS)
        time.sleep(20) # Wait for 2 seconds
        home.pick_price_point()
        time.sleep(0.5) # Wait for 0.5 seconds
        home.pick_region()
        time.sleep(0.5) # Wait for 0.5 seconds
        home.pick_category()
        home.click_find_present()

    def tearDown(self):
        self.driver.quit()

    # rm -rf allure-report
    # pytest --alluredir=allure-report
    # allure generate allure-report
    # allure serve allure-report
