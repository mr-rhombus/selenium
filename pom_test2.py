from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage

# Test setup
driver = webdriver.Chrome()
test_value = 'It worked!'

# Test
training_page = TrainingGroundPage(driver)
training_page.go()

# Proper test. Very Readable!
assert training_page.button1.text == 'Button1'

# Test that you can click button1
# training_page.button1.click()

driver.close()