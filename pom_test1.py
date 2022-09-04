from selenium import webdriver

from page_object_model import TrainingGroundPage


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