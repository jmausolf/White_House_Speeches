##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


def remove_duplicatesSpeechURL(merged_speech_urls_csv, no_duplicates_speech_csv):
	import csv
	with open(merged_speech_urls_csv, 'rU') as f:

		urls = set()
		for row in csv.reader(f):
			key = row[0]
			if key not in urls:
				urls.add(key)
				with open(no_duplicates_speech_csv, 'a') as f1: f1.write("{}\n".format(row[0]))
		print "removing duplicates in merged speech url file"
		print "writing new speech_url file -->", no_duplicates_speech_csv, "..."


#remove_duplicatesSpeechURL("speechurls_merged_with_duplicates.csv", "cleaned_urls.csv")
#remove_duplicatesSpeechURL("speechurls_test.csv", "cleaned_urls2.csv")
#remove_duplicatesSpeechURL("speechurls_new.csv", "cleaned_urls2_new.csv")

remove_duplicatesSpeechURL("speech_urls_current_data.csv", "speechurls.csv")
