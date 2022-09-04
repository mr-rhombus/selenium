from selenium.webdriver.common.by import By

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'
        self.input_selector = "input#ipt1"

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        input = self.driver.find_element(By.CSS_SELECTOR, self.input_selector)
        input.clear()
        input.send_keys(text)

    def get_input_text(self):
        input = self.driver.find_element(By.CSS_SELECTOR, self.input_selector)
        return input.get_attribute('value')

    def click_button1(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button#b1")
        button.click()