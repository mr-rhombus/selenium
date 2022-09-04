from selenium import webdriver

from pages.trial_of_stones import TrialPage

# Test setup
driver = webdriver.Chrome()

# Test
trial_page = TrialPage(driver)
trial_page.go()

trial_page.riddle_of_stone_input.input_text('rock')
trial_page.riddle_of_stone_button.click()