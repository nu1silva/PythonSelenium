import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.HomePage import HomPage
from core.Configurations import Constants


class ComputersTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_computers_home(self):
        driver = self.driver
        driver.set_page_load_timeout(20)
        driver.get(Constants.application_url)

        home_page = HomPage(driver)

        self.assertIn("computers found", home_page.get_page_header_title().text)

        home_page.get_txt_search().clear()
        home_page.get_txt_search().send_keys("test")
        home_page.get_btn_search().click()

        self.assertIn("http://computer-database.herokuapp.com/computers?f=test", driver.current_url)
        self.assertIn("ChipTest", driver.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[1]/td[1]').text)
        self.assertIn("Test", driver.find_element_by_xpath('//*[@id="main"]/table/tbody/tr[3]/td[1]').text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
