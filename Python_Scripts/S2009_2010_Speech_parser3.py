##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

from Quality_Check_speech_parser import *
from month import *
from dateutil.parser import parse

def pre_WHT3(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys, random
    import os
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # Get URL
    url2 = "Cite: \n"+url+"\n"

    # Get Date
    Date = soup.find("meta", {"property":"article:published_time"})
    raw_date = str(Date).split('"', 2)[1][0:10]
    date = '\n'+raw_date+'\n'
    date_reform = parse(str(date)).strftime('%B %d, %Y')
    date_reformat = '\n'+date_reform+'\n'


    # Get Release
    Release = soup.find("meta", {"property":"og:title"})
    raw_release = str(Release)
    release = '\n'+'The White House''\n''Office of the Press Secretary'+'\n'+'\n'+'For Immediate Release'+date_reformat

    # Get Title
    Title = soup.find("meta", {"property":"og:title"})
    raw_title = str(Title).split('"', 2)[1]
    title = '\n'+raw_title+'\n'

    #Get File ID - Date & Time
    #Date - RAW
    date_split = date.split('-')
    month_raw = date_split[1]
    day_raw = date_split[2]
    year_raw = date_split[0]

    #MonthID
    month_clean1 = month_raw.replace(' ', '')
    month_clean2 = month_clean1.replace('\n', '')
    try:
        month_id = month(month_clean2)
    except:
        month_id = month_clean2

    #DayID
    day_clean1 = day_raw.replace(',', '')
    day_clean2 = day_clean1.replace(' ', '')
    day_clean3 = day_clean2.replace('\n', '')
    day_id = day_clean3

    #YearID
    year_clean1 = year_raw.replace(' ', '')
    year_clean2 = year_clean1.replace('\n', '')
    year_id = year_clean2

    #Final DateID
    date_id = year_id+'-'+month_id+'-'+day_id
    print date_id

    try:
        # Get Paragraph2
        content2 = soup.find("div", {"class":"field-items"})
        paragraph2 = ["".join(x.findAll(text=True)) for x in content2.findAll("div", {"class":"legacy-para"})]

        #Pargraph Body2
        paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2))

        # Test ID
        test_raw = paragraph_body2
        test1 = test_raw.replace(' ', '')
        test_id = test1.replace('\n', '')

        if test_id == '':
            print "paragraph body 2 empty"
            content1 = soup.find("div", {"class":"field-items"})
            paragraph1 = ["".join(x.findAll(text=True)) for x in content1.findAll("p")]
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1))

        elif len(test_id) < 400:
            print "paragraph body 2 not correct"
            content1 = soup.find("div", {"class":"field-items"})
            paragraph1 = ["".join(x.findAll(text=True)) for x in content1.findAll("p")]
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1))

        else:
            print "else"
            paragraph_body1 = ' '

    except:
        # Get Paragraph1
        content1 = soup.find("div", {"class":"field-items"})
        paragraph1 = ["".join(x.findAll(text=True)) for x in content1.findAll("p")]

        # Get Paragraph Body1
        paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1))

        # Test ID
        test_raw = paragraph_body1
        test1 = test_raw.replace(' ', '')
        test_id = test1.replace('\n', '')


        if test_id == '':
            content2 = soup.find("div", {"class":"field-items"})
            paragraph2 = ["".join(x.findAll(text=True)) for x in content2.findAll("div", {"class":"legacy-para"})]   
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2))
        elif len(test_id) < 400:
            content2 = soup.find("div", {"class":"field-items"})
            paragraph2 = ["".join(x.findAll(text=True)) for x in content2.findAll("div", {"class":"legacy-para"})]
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2))
        else:
            paragraph_body2 = ' '



    # Perform Quality Check on Parsed Speech
    speech_parser_two_para_QC(url, paragraph_body1, paragraph_body2)

    #Random ID
    randID1 = str(random.randrange(6, 10000, 1))
    randID2 = str(random.randrange(6, 10000, 1))



    try:
        path1 = date_id+"_"+"ID1"+".txt"
        path2 = date_id+"_"+"ID2"+".txt"
        path3 = date_id+"_"+"ID3"+".txt"
        path4 = date_id+"_"+"ID4"+".txt"
        path5 = date_id+"_"+"ID5"+".txt"
        if os.path.isfile(path1) == False:
            #print "no file ID1 found, create ID1"
            f = open(date_id+"_"+"ID1"+".txt", 'w')
            f.write(url2.encode('utf-8'))
            f.write(paragraph_body1.encode('utf-8'))
            f.write(paragraph_body2.encode('utf-8'))
            f.close
            return

        elif os.path.isfile(path1) == True:
            #print "found file ID1, check for ID2"
            if os.path.isfile(path2) == False:
                print "found ID1, no file ID2 found, make ID2"
                f = open(date_id+"_"+"ID2"+".txt", 'w')
                f.write(url2.encode('utf-8'))
                f.write(paragraph_body1.encode('utf-8'))
                f.write(paragraph_body2.encode('utf-8'))
                f.close
                return
            elif os.path.isfile(path2) == True:
                #print "found file ID2, check for ID3"
                if os.path.isfile(path3) == False:
                    print "found IDs 1-2, no file ID3 found, make ID3"
                    f = open(date_id+"_"+"ID3"+".txt", 'w')
                    f.write(url2.encode('utf-8'))
                    f.write(paragraph_body1.encode('utf-8'))
                    f.write(paragraph_body2.encode('utf-8'))
                    f.close
                    return
                elif os.path.isfile(path3) == True:
                    #print "found file ID3, check for ID4"
                    if os.path.isfile(path4) == False:
                        print "found IDs 1-3, no file ID4 found, make ID4"
                        f = open(date_id+"_"+"ID4"+".txt", 'w')
                        f.write(url2.encode('utf-8'))
                        f.write(paragraph_body1.encode('utf-8'))
                        f.write(paragraph_body2.encode('utf-8'))
                        f.close
                        return
                    elif os.path.isfile(path4) == True:
                        #print "found file ID4, check for ID5"
                        if os.path.isfile(path5) == False:
                            print "found IDs 1-4, no file ID5 found, make ID5"
                            f = open(date_id+"_"+"ID5"+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return
                        elif os.path.isfile(path5) == True:
                            print "found IDs 1-5, create random ID"
                            f = open(date_id+"_"+"ID"+randID1+"-"+randID2+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return 

        
    finally:
        pass




#Test

#Try
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-qa-session-closing-fiscal-responsibility-summit-2-23-09"
#url = "http://www.whitehouse.gov/the-press-office/press-availability-president-obama-and-prime-minister-rudd-australia"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-executive-compensation-with-secretary-geithner"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-welcoming-senior-staff-and-cabinet-secretaries-white-house"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-obama-and-prime-minister-aso-meeting"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-question-and-answer-session-closing-fiscal-responsibility-summit"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-signing-credit-card-accountability-responsibility-and-disclosure-"

#Except
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-senate-passage-health-insurance-reform"

#pre_WHT3(url)




