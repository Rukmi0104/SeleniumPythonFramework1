from selenium.webdriver.common.by import By
from locators.Locators import Locators

class Homepage():


    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()
