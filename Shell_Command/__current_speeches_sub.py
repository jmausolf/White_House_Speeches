##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################




import unittest, time, re, sys

sys.path.append('../Python_Scripts/')
from speech_urls import *


#Run on Previously Collected HTML Files
speech_urls_current_data("whitehouse_current_speechs_remarks.html")

speech_urls_current_data_wa("whitehouse_current_weekly_address.html")

speech_urls_current_data("whitehouse_current_press_briefings.html")

speech_urls_current_data("whitehouse_current_statements_releases.html")

