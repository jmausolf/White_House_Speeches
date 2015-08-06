##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

from date import date
import csv

def read_parentURLs(i):
	"""Reads the URLs from the Parent URLs CSV"""
	with open('parentURLs.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		return URL


def read_reqURLs(i):
	"""Reads the URLs from the Requested Parent URLs CSV"""
	with open('requested_parentURLs.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "generating subpages for base url ", i+1, "..."
		return URL


def read_subURLs(i):
	with open('subpages.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "generating speech urls for subpage ", i+1, "..."
		return URL


def read_speechURLs(i):
	with open('speechurls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for speech url ", i+1, "..."
		return URL


def read_presidentURLs(i):
	with open('__president_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for presidential speech url ", i+1, "..."
		return URL


def read_vice_presidentURLs(i):
	with open('__vice_president_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for vice presidential speech url ", i+1, "..."
		return URL


def read_first_ladyURLs(i):
	with open('__first-lady_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for first lady speech url ", i+1, "..."
		return URL


def read_second_ladyURLs(i):
	with open('__second-lady_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for second lady speech url ", i+1, "..."
		return URL


def read_otherURLs(i):
	with open('__other_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		print "creating file for other speaker speech url ", i+1, "..."
		return URL


