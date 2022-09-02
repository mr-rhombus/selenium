# Setup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up browser object
browser = webdriver.Chrome(ChromeDriverManager().install())

# Open browser and navigate to URL
browser.get('https://techstepacademy.com/training-ground')

# Find element using CSS Selector
from selenium.webdriver.common.by import By
# Define CSS Selector
# Play around in the "Console" on a web page to build "surgical" selectors!
# $$("input[id='ipt1']") will do the trick
input1_css_selector = "input[id='ipt1']"
# This is an input element
input1_element = browser.find_element(By.CSS_SELECTOR, input1_css_selector)
# Type in the input box
input1_element.send_keys('I am cool')

# Find element using XPATH
# $x("//button[@name='butn1']") will do the trick
button1_xpath_selector = "//button[@name='butn1']"

# Walk up and down the tree
product1_xpath = "//b[contains(text(), 'Product 1')]"  # Finds the <b>Product 1</b> element
product1_element = browser.find_element(By.XPATH, product1_xpath)
# We want the parent <div> element containing this <b> element, however
div_product1_xpath = product1_xpath + '/../..'
# If we want to walk back down to the <b> element...
back_to_b = div_product1_xpath + '/span/b'  # since the nesting is <div><span><b>Product 1</b></span></div>