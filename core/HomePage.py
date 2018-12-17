from selenium.webdriver.common.by import By
from core.ElementLocator import ElementLocator


class HomPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.home_page_title = driver.find_element(By.XPATH, ElementLocator.home_page_title)
        self.home_page_txt_search = driver.find_element(By.XPATH, ElementLocator.home_page_txt_search)
        self.home_page_btn_filter = driver.find_element(By.XPATH, ElementLocator.home_page_btn_filter)
        self.home_page_btn_add = driver.find_element(By.XPATH, ElementLocator.home_page_btn_add)

    def get_btn_add_computer(self):
        return self.home_page_btn_add

    def get_page_header_title(self):
        return self.home_page_title

    def get_txt_search(self):
        return self.home_page_txt_search

    def get_btn_search(self):
        return self.home_page_btn_filter
