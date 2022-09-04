# Consolidated version of page_object_model.py, updated by implementing base_element.py (and BaseElement class)

from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground'

    @property
    def button1(self):
        locator = Locator(by=By.CSS_SELECTOR, value = 'button#b1')        
        return BaseElement(driver=self.driver, locator=locator)