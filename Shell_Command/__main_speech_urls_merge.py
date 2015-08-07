##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def mergeSpeechURL(first_csv, second_csv):
	import csv 
	with open(first_csv, 'rU') as csv_1:

		#Add the first CSV to Merged CSV File
		for row in csv.reader(csv_1):
			with open('__merged_speechurls.csv','a') as f1: f1.write("{}\n".format(row[0]))

	with open(second_csv, 'rU') as csv_2:
		#Add the second CSV to Merged CSV File
		for row in csv.reader(csv_2):
			with open('__merged_speechurls.csv','a') as f1: f1.write("{}\n".format(row[0]))

	print "merging speech_urls files..."
	
#mergeSpeechURL("speechurls.csv", "speech_urls_current_data.csv")
mergeSpeechURL("speechurls.csv", "speech_urls_current_data.csv")



