##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

import sys, csv, time, os, subprocess
sys.path.append('../Python_Scripts/')
sys.path.append('..')

from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *
from S2009_2010_Speech_parser1 import *
from S2009_2010_Speech_parser2 import *
from S2009_2010_Speech_parser3 import *
from Speech_parser_ID import Parser_ID 
from Quality_Check_speech_parser import *

if __name__ == '__main__':

## ____________ President Speeches _____________ ##

	# Get CSV Lines - President
	os.chdir('bash_Speech')
	os.chdir('Speech_President')
	with open('__president_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		Xpotus = len(lines)
		print "Total requested President speech urls:", Xpotus

	# Create Parsed Speeches - President
	for URL in range(0, Xpotus):
		speechURL = '\n'.join(map(str, read_presidentURLs(URL)))
		time.sleep(0.5)
		try:
			pre_WHT3(speechURL)
			print "ran pre_WHT3"
		except:
			try:
				pre_WHT1(speechURL)
				print "ran pre_WHT1"
			except:
				try:
					pre_WHT2(speechURL)
					print "ran pre_WHT2"
				except:
					print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
					speech_parser_skip_QC(speechURL)
					pass


## ____________ Vice-President Speeches _____________ ##

	try:
		# Get CSV Lines - Vice-President
		os.chdir(os.pardir)
		os.chdir('Speech_Vice_President')
		with open('__vice_president_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xvp = len(lines)
			print "Total requested Vice-President speech urls:", Xvp

		# Create Parsed Speeches - Vice-President
		for URL in range(0, Xvp):
			speechURL = '\n'.join(map(str, read_vice_presidentURLs(URL)))
			time.sleep(0.5)
			try:
				pre_WHT1(speechURL)
				print "ran pre_WHT1"
			except:
				try:
					pre_WHT3(speechURL)
					print "ran pre_WHT3"
				except:
					try:
						pre_WHT2(speechURL)
						print "ran pre_WHT2"
					except:
						print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
						speech_parser_skip_QC(speechURL)
						pass
	except:
		print "No Vice-President Speeches Found, Pass."
		pass


## ____________ First-Lady Speeches _____________ ##

	try:
		# Get CSV Lines - First Lady
		os.chdir(os.pardir)
		os.chdir('Speech_First_Lady')
		with open('__first-lady_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xflotus = len(lines)
			print "Total requested First-Lady speech urls:", Xflotus

		# Create Parsed Speeches - First Lady
		for URL in range(0, Xflotus):
			speechURL = '\n'.join(map(str, read_first_ladyURLs(URL)))
			time.sleep(0.5)
			try:
				pre_WHT1(speechURL)
				print "ran pre_WHT1"
			except:
				try:
					pre_WHT3(speechURL)
					print "ran pre_WHT3"
				except:
					try:
						pre_WHT2(speechURL)
						print "ran pre_WHT2"
					except:
						print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
						speech_parser_skip_QC(speechURL)
						pass
	except:
		print "No First-Lady Speeches Found, Pass."
		pass


## ____________ Second-Lady Speeches _____________ ##

	try: 
		# Get CSV Lines - Second Lady
		os.chdir(os.pardir)
		os.chdir('Speech_Second_Lady')
		with open('__second-lady_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xsl = len(lines)
			print "Total requested Second-Lady speech urls:", Xsl

		# Create Parsed Speeches - Second Lady
		for URL in range(0, Xsl):
			speechURL = '\n'.join(map(str, read_second_ladyURLs(URL)))
			time.sleep(0.5)
			try:
				pre_WHT1(speechURL)
				print "ran pre_WHT1"
			except:
				try:
					pre_WHT3(speechURL)
					print "ran pre_WHT3"
				except:
					try:
						pre_WHT2(speechURL)
						print "ran pre_WHT2"
					except:
						print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
						speech_parser_skip_QC(speechURL)
						pass
	except:
		print "No Second-Lady Speeches Found, Pass."
		pass


## ____________ Other Speeches _____________ ##

	try:
		# Get CSV Lines - Other
		os.chdir(os.pardir)
		os.chdir('Speech_Other')
		with open('__other_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xother = len(lines)
			print "Total requested Other speech urls:", Xother

		# Create Parsed Speeches - Other
		for URL in range(0, Xother):
			speechURL = '\n'.join(map(str, read_otherURLs(URL)))
			time.sleep(0.5)
			try:
				pre_WHT1(speechURL)
				print "ran pre_WHT1"
			except:
				try:
					pre_WHT3(speechURL)
					print "ran pre_WHT3"
				except:
					try:
						pre_WHT2(speechURL)
						print "ran pre_WHT2"
					except:
						print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
						speech_parser_skip_QC(speechURL)
						pass
	except:
		print "No Other Speeches Found, Pass."
		pass



