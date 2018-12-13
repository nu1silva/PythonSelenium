from selenium.webdriver.common.by import By
from core.ElementLocator import ElementLocator


class HomPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.home_page_title = driver.find_element(By.XPATH, ElementLocator.home_page_title)
        self.home_page_txt_search = driver.find_element(By.XPATH, ElementLocator.home_page_txt_search)
        self.home_page_btn_filter = driver.find_element(By.XPATH, ElementLocator.home_page_btn_filter)
        self.home_page_btn_add = driver.find_element(By.XPATH, ElementLocator.home_page_btn_add)

    def getHomePageTitle(self):
        return self.home_page_title

    def setSearchText(self, input):
        self.home_page_txt_search.clear()
        self.home_page_txt_search.send_keys(input)

    def clickSearchText(self):
        self.home_page_btn_filter.click()

    def clickAddComputer(self):
        self.home_page_btn_add.click()
