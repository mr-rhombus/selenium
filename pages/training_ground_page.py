# Consolidated version of page_object_model.py, updated by implementing base_element.py (and BaseElement class)

from selenium.webdriver.common.by import By

from pages.base_element import BaseElement

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    @property
    def button1(self):
        by = By.CSS_SELECTOR
        value = 'button#b1'
        return BaseElement(driver=self.driver, by=by, value=value)