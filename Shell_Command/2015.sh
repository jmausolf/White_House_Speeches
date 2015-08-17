##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

## ____________ FIRST_STAGE - Make New Directories ____________ ##

#Make New Directories -- CSVs 
mkdir bash_CSVs
cd bash_CSVs
mkdir Auxiliary_CSVs
mkdir Master_Speech_CSV
mkdir Filtered_Speech_CSVs
cd ..


#Make New Directories -- Speeches
mkdir bash_Speech
cd bash_Speech
mkdir Speech_President
mkdir Speech_Vice_President
mkdir Speech_First_Lady
mkdir Speech_Second_Lady
mkdir Speech_Other
cd ..


## ____________ SECOND_STAGE - Collect URLs ___________________ ##

#Run main_speechesurls.py to generate CSV's
python __main_speech_urls_bearer.py "2015/01" "2015/06"
python __current_speeches.py
#rm whitehouse_current.html

## ____________ THIRD_STAGE - Filter and Merge URLs ____________ ##

#Merge Speech URLs
python __main_speech_urls_merge.py
mv speechurls.csv pre_merge_speechurls.csv

#Remove Speech URL Duplicates (If Any)
python __main_speech_urls_remove_duplicates.py


#Filter Speech URLs
python __main_speech_urls_filter.py 


## ____________ FOURTH_STAGE - Sort Filtered URLs _____________ ##


#Move Auxiliary CSVs
mv requested_parentURLs.csv bash_CSVs/Auxiliary_CSVs
mv subpages.csv bash_CSVs/Auxiliary_CSVs
mv parentURLs.csv bash_CSVs/Auxiliary_CSVs
mv pre_merge_speechurls.csv bash_CSVs/Auxiliary_CSVs
mv speech_urls_current_data.csv bash_CSVs/Auxiliary_CSVs

#Copy All Speech CSVs to Speech Folders

cp whitehouse_current.html bash_Speech
cp speechurls.csv bash_Speech
cp __president_urls.csv bash_Speech/Speech_President
cp __vice_president_urls.csv bash_Speech/Speech_Vice_President
cp __first-lady_urls.csv bash_Speech/Speech_First_Lady
cp __second-lady_urls.csv bash_Speech/Speech_Second_Lady
cp __other_urls.csv bash_Speech/Speech_Other


#Move All CSVs
mv whitehouse_current.html bash_CSVs/Auxiliary_CSVs
mv speechurls.csv bash_CSVs/Master_Speech_CSV
mv __president_urls.csv bash_CSVs/Filtered_Speech_CSVs
mv __vice_president_urls.csv bash_CSVs/Filtered_Speech_CSVs
mv __first-lady_urls.csv bash_CSVs/Filtered_Speech_CSVs
mv __second-lady_urls.csv bash_CSVs/Filtered_Speech_CSVs
mv __other_urls.csv bash_CSVs/Filtered_Speech_CSVs



## ____________ FIFTH_STAGE - Parse All URLs __________________ ##


#Generate Text Files for Given Speech URLS
python __main_speech_parser.py 


## ____________ SIXTH_STAGE - Rename Bash Folders __________________ ##

mv bash_CSVs 2015_CSVs
mv bash_Speech 2015_Speeches



