##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def filterSpeechURL():
	import csv 
	with open('speechurls.csv', 'rU') as f:
		for row in csv.reader(f):

			#Filter President Obama
			if 'remarks-president' in row[0] or 'marks-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'weekly-address' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'statement-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'statements-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'statements' in row[0] and 'president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif '/letter' in row[0] or 'letter-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif '/message' in row[0] or 'message-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'declaraciones-del-president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'press-conference-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'news-conference-president' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif '/president-barack-obamas' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif '/president-obama' in row[0] and 'greeting' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif '/president-obama' in row[0] and 'speak' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'op-ed-president-barack-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'op-ed-president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'transcript-president-obamas' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'transcript-president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'press-availability-president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'press-availability' in row[0] and 'president-obama' in row[0]:
				with open('__president_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter First Lady
			elif 'remarks-first-lady' in row[0]:
				with open('__first-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter VP
			elif 'vice-president' in row[0]:
				with open('__vice_president_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Jill Biden
			elif 'jill' in row[0]:
				with open('__second-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'dr-biden' in row[0]:
				with open('__second-lady_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Other Documents Not by President to Others:
			elif 'obama-nominates' in row[0] or 'obama-nominate' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'obama-names' in row[0] or 'obama-name' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'obama-signs' in row[0] or 'obama-sign' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'obama-announces' in row[0] or 'obama-announce' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'obama-amends' in row[0] or 'obama-amend' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'fact-sheet-president' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'president-obama-deliver' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'president-obama-award' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'readout-president-obama' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'president-obama-travel' in row[0]:
				with open('__other_urls.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter Everthing Else
			else:
				with open('__other_urls.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


filterSpeechURL()
