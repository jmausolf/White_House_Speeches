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

    #Define Content
    content = soup.find("div", {"class":"field-items"})

    #Get Paragraph1p
    paragraph1p = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph_body1p = "\n\n%s" % ("\n\n".join(paragraph1p))

    #Get Paragraph1div
    paragraph1div = ["".join(x.findAll(text=True)) for x in content.findAll("div")]
    paragraph_body1div = "\n\n%s" % ("\n\n".join(paragraph1div))

    # Get Paragraph2
    paragraph2 = ["".join(x.findAll(text=True)) for x in content.findAll("div", {"class":"legacy-para"})]
    paragraph_body2lp = "\n\n%s" % ("\n\n".join(paragraph2))

    
    #ADD P2-P
    # Get Paragraph2p
    paragraph2p = ["".join(x.findAll(text=True)) for x in content.findAll("p")]


    # Test ID - Div - Legacy Para
    test_2 = paragraph_body2lp.replace(' ', '').replace('\n', '')

    # Test ID - 1p
    test_1p = paragraph_body1p.replace(' ', '').replace('\n', '')

    # Test ID - 1div
    test_1div = paragraph_body1div.replace(' ', '').replace('\n', '')

    try:
"""
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

"""


        if test_2 !='':
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2))
            paragraph_body1 = ' '


        elif test_2 == '':
            
            print "paragraph body 2 empty"
            paragraph2p = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))

            if test_1p == '':
                if test_1div != '':
                    paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
                    paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))
            elif test_1p != '':
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1p))
                paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))

        elif len(test_2) < 400:
            print "paragraph body 2 not correct"
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))

        else:
            print "else"
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
            paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))

    except:
        print "except"
        paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2p))

        # Get Paragraph_Body1
        if test_1p == '':
            if test_1div != '':
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
            else:
                print "paragraph_body1p and paragraph_body1div empty"
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
        elif test_1p != '':
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1p))
        else:
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
            print "paragraph_body1 empty"





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
            f = open(date_id+"_"+"ID1"+".txt", 'w')
            f.write(url2.encode('utf-8'))
            f.write(paragraph_body1.encode('utf-8'))
            f.write(paragraph_body2.encode('utf-8'))
            f.close
            return

        elif os.path.isfile(path1) == True:
            if os.path.isfile(path2) == False:
                print "found ID1, no file ID2 found, make ID2"
                f = open(date_id+"_"+"ID2"+".txt", 'w')
                f.write(url2.encode('utf-8'))
                f.write(paragraph_body1.encode('utf-8'))
                f.write(paragraph_body2.encode('utf-8'))
                f.close
                return
            elif os.path.isfile(path2) == True:
                if os.path.isfile(path3) == False:
                    print "found IDs 1-2, no file ID3 found, make ID3"
                    f = open(date_id+"_"+"ID3"+".txt", 'w')
                    f.write(url2.encode('utf-8'))
                    f.write(paragraph_body1.encode('utf-8'))
                    f.write(paragraph_body2.encode('utf-8'))
                    f.close
                    return
                elif os.path.isfile(path3) == True:
                    if os.path.isfile(path4) == False:
                        print "found IDs 1-3, no file ID4 found, make ID4"
                        f = open(date_id+"_"+"ID4"+".txt", 'w')
                        f.write(url2.encode('utf-8'))
                        f.write(paragraph_body1.encode('utf-8'))
                        f.write(paragraph_body2.encode('utf-8'))
                        f.close
                        return
                    elif os.path.isfile(path4) == True:
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

#url = "http://www.whitehouse.gov/the-press-office/remarks-president-qa-session-closing-fiscal-responsibility-summit-2-23-09"
#url = "http://www.whitehouse.gov/the-press-office/press-availability-president-obama-and-prime-minister-rudd-australia"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-executive-compensation-with-secretary-geithner"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-welcoming-senior-staff-and-cabinet-secretaries-white-house"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-obama-and-prime-minister-aso-meeting"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-question-and-answer-session-closing-fiscal-responsibility-summit"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-signing-credit-card-accountability-responsibility-and-disclosure-"

#Except
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-senate-passage-health-insurance-reform"

#url = "http://www.whitehouse.gov/the-press-office/remarks-president-and-vice-president-meeting-with-nations-mayors"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-costa-mesa-town-hall"

#url = "https://www.whitehouse.gov/the-press-office/2010/09/28/remarks-president-dnc-rally-madison-wisconsin"

#pre_WHT3(url)




