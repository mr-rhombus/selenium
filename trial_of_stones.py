from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome(ChromeDriverManager().install())
# Add "drivers" dir to your PATH to have the Chrome webdriver "pre-loaded"
# See section 1, lecture 6 for a walkthrough
browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# Define a function to solves riddles 1 and 2
def input_and_press_enter(input_selector, input_text, button_selector):
    input = browser.find_element(By.CSS_SELECTOR, input_selector)
    input.send_keys(input_text)
    button = browser.find_element(By.CSS_SELECTOR, button_selector)
    # button.send_keys(Keys.ENTER)
    button.click()


## Riddle of Stone
riddle_of_stone_answer = 'rock'
input1_selector = "input[id='r1Input']"
answer1_selector = "button[id='r1Btn']"
input_and_press_enter(input1_selector, riddle_of_stone_answer, answer1_selector)


## Riddle of Secrets
# Find answer from Riddle of Stone
answer1_text_selector = "//div[@id='passwordBanner']/h4"
password = browser.find_element(By.XPATH, answer1_text_selector).text
# Enter Riddle of Stone answer into Riddle of Secrets
input2_selector = "input[id='r2Input']"
answer2_selector = "button[id='r2Butn']"
input_and_press_enter(input2_selector, password, answer2_selector)


## The Two Merchants
# Find the richest merchant
merchant_div = "//label[contains(text(), 'Total Wealth')]/.."
richest_merchant = ''
richest_wealth = 0
merchants = browser.find_elements(By.XPATH, merchant_div)
for div in merchants:
    # Assume all wealth >= 0
    name = browser.find_element(By.XPATH, merchant_div + '/span/b').text
    wealth = int(browser.find_element(By.XPATH, merchant_div + '/p').text)
    if wealth > richest_wealth:
        richest_merchant = name
        richest_wealth = wealth
# Enter their name and complete the trial
input3_selector = "input[id='r3Input']"
answer3_selector = "button[id='r3Butn']"
input_and_press_enter(input3_selector, richest_merchant, answer3_selector)


## Press "Check Answers"
check_answers_btn = browser.find_element(By.CSS_SELECTOR, "button#checkButn")
check_answers_btn.click()

success_text = browser.find_element(By.CSS_SELECTOR, 'div#trialCompleteBanner > h4').text
assert success_text == 'Trial Complete'

print('First browser automation complete!')
