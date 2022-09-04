# Wrap a Selenium web element, then allow it to do some "fancier" things

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, by, value):
        self.driver = driver
        self.value = value
        self.by = by
        # Locator arg in Selenium expects both "By" and "Locator value" in a tuple
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        # Wait up to 10s for the element to be located
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        # self.driver.find_element(self.by, self.locator)  # Unsophisticated way
        self.web_element = element

    def input_text(self, text):
        self.web_element.send_keys(text)

    def click(self):
        # Make sure element (button) is clickable before clicking it
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()

    # Treat this fn like a property, allowing us to get/set values
    @property
    def text(self):
        text = self.web_element.text
        return text