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

print "Running White House Speech Collection"
print "Your Browser Will Open and Close During This Process."
print "Please do not close..."

class Speeches_and_Remarks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.whitehouse.gov/briefing-room/speeches-and-remarks"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        scroll = 0
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1, 400):
            scroll +=1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print "conducting infinite scroll scrape...scroll number "+str(scroll)
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        try:
            outfile = 'whitehouse_current_speechs_remarks.html'
            f=open(outfile, 'w')
            print "writing infinite scroll html data to --> "+str(outfile)+"..."
            f.write(data)
        finally:
            f.close()
        driver.close()

        speech_urls_current_data(outfile)


class Weekly_Addresses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #Might need to fix thix, seems to get other urls that are not speech urls
        self.base_url = "https://www.whitehouse.gov/briefing-room/weekly-address"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        scroll = 0
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1, 150):
            scroll +=1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print "conducting infinite scroll scrape...scroll number "+str(scroll)
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        try:
            outfile = 'whitehouse_current_weekly_address.html'
            f=open(outfile, 'w')
            print "writing infinite scroll html data to --> "+str(outfile)+"..."
            f.write(data)
        finally:
            f.close()
        driver.close()

        speech_urls_current_data_wa(outfile)



class Press_Briefings(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.whitehouse.gov/briefing-room/press-briefings"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        scroll = 0
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1, 400):
            scroll +=1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print "conducting infinite scroll scrape...scroll number "+str(scroll)
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        try:
            outfile = 'whitehouse_current_press_briefings.html'
            f=open(outfile, 'w')
            print "writing infinite scroll html data to --> "+str(outfile)+"..."
            f.write(data)
        finally:
            f.close()
        driver.close()

        speech_urls_current_data(outfile)


class Statements_and_Releases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.whitehouse.gov/briefing-room/statements-and-releases"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        scroll = 0
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        for i in range(1, 700):
            scroll +=1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print "conducting infinite scroll scrape...scroll number "+str(scroll)
            time.sleep(4)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        try:
            outfile = 'whitehouse_current_statements_releases.html'
            f=open(outfile, 'w')
            print "writing infinite scroll html data to --> "+str(outfile)+"..."
            f.write(data)
        finally:
            f.close()
        driver.close()

        speech_urls_current_data(outfile)



if __name__ == "__main__":
    unittest.main()
