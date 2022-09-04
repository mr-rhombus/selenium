# Define all basic elements that a "page" should be able to do -> ex. go to page, back, forward, ...

class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)