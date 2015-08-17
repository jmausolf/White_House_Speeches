##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

sys.path.append('../Python_Scripts/')
from speech_urls import *

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.whitehouse.gov/briefing-room/speeches-and-remarks"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1, 100):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print "conducting infinite scroll scrape..."
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        try:
            f=open('whitehouse_current.html', 'w')
            print "writing infinite scroll html data..."
            f.write(data)
        finally:
            f.close()
        driver.close()

        speech_urls_current_data("whitehouse_current.html")


if __name__ == "__main__":
    unittest.main()

