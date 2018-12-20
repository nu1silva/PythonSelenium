from webdriver_manager.chrome import ChromeDriverManager

import unittest
import datetime
from selenium import webdriver


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Execution starting at :" + str(datetime.datetime.now()))
        print("Setting up environment")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver != None):
            print("------------------------------------------------------------------")
            print("Cleaning up environment")
            print("Execution Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
