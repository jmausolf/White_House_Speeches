##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

import sys, csv, time 
sys.path.append('../Python_Scripts/')

from getparentURL import *
from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *

if __name__ == '__main__':
	Dates = sys.argv[1:]

	print "Dates are: ", Dates
	print len(Dates)

	#Input Error Checking
	assert Dates, "Error: Please provide two dates in the form 'YYYY/MM' 'YYYY/MM' ."
	if len(Dates) == 1:
		assert not Dates, "Error: Only one date provided, pleave provide two dates. Format: 'YYYY/MM' 'YYYY/MM'" 
	if len(Dates) > 2:
		assert not Dates, "Error: Greater than two dates provided, pleave provide two dates. Format: 'YYYY/MM' 'YYYY/MM'" 

	#Generate Parent URLs CSV
	getparentURLs()
	
	#Define initial parent URLs in Specified Date Range
	parent_urls = req_URLs(Dates[0], Dates[1])

	print "___"*20

	#Get Number of Lines of Requested URLs
	with open('requested_parentURLs.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XR = len(lines)
		print "Total requested urls:", XR
		
	# Create CSV of Subpage URLS 
	for URL in range(0, XR):
		rURL = '\n'.join(map(str, read_reqURLs(URL)))
		time.sleep(0.5)
		sub_pages_URLs(rURL)

	#Get Number of Lines of Subpages URLs
	with open('subpages.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XS = len(lines)
		print "Total requested subpages:", XS

	# Create CSV of Speech URLS
	for URL in range(0, XS):
		subURL = '\n'.join(map(str, read_subURLs(URL)))
		time.sleep(0.5)
		speech_urls(subURL)




