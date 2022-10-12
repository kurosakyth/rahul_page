from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class rahul_radios:
    URL = 'https://rahulshettyacademy.com/AutomationPractice/'
    SEARCH_RADIO_BUTTON = (By.ID,'autocomplete')

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_radio_button = self.browser.find_element(*self.SEARCH_RADIO_BUTTON)
        search_radio_button.send_keys(phrase + Keys.RETURN)