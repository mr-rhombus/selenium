from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage


class TrialPage(BasePage):
    
    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def riddle_of_stone_input(self):
        by = By.CSS_SELECTOR
        value = 'input#r1Input'
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def riddle_of_stone_button(self):
        by = By.CSS_SELECTOR
        value = 'button#r1Btn'
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def riddle_of_secrets_input(self):
        by = By.CSS_SELECTOR
        value = 'input#r2Input'
        return BaseElement(driver=self.driver, by=by, value=value)
    
    @property
    def riddle_of_secrets_button(self):
        by = By.CSS_SELECTOR
        value = 'input#r2Butn'
        return BaseElement(driver=self.driver, by=by, value=value)