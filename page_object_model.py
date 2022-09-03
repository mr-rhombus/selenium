from selenium import webdriver
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


# Testing
# Setup
driver = webdriver.Chrome()
training_page = TrainingGroundPage(driver=driver)
test_text = 'It worked!'

# Test
training_page.go()
training_page.type_into_input(test_text)
# training_page.click_button1()  # Throws error, can be handled by closing the alert with action chain

text_from_input = training_page.get_input_text()
assert text_from_input == test_text, f'Test failed: Input did not match expected "{test_text}"'