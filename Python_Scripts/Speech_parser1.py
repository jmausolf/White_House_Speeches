##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

from Quality_Check_speech_parser import *

def WHT(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys, random
    import os
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # Get URL
    url2 = "Cite: \n"+url

    # Get Release
    Release = soup.find("div", {"class":"panel-pane pane-custom pane-1"})
    raw_release = Release.get_text()
    release = raw_release

    # Get Title
    Title = soup.find("div", {"class":"panel-pane pane-node-title"})
    title = Title.get_text()
    
    #Define Content
    content = soup.find("div", {"class":"field-items"})
    content2 = soup.find("div", {"class":"field-item even"})

    #Get Paragraph1p
    paragraph1p = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph_body1p = "\n\n%s" % ("\n\n".join(paragraph1p))

    #Get Paragraph1div
    paragraph1div = ["".join(x.findAll(text=True)) for x in content.findAll("div")]
    paragraph_body1div = "\n\n%s" % ("\n\n".join(paragraph1div))

    # Test ID - 1p
    test_1p = paragraph_body1p.replace(' ', '').replace('\n', '')

    # Test ID - 1div
    test_1div = paragraph_body1div.replace(' ', '').replace('\n', '')

    # Get Paragraph Body
    paragraph = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph2p = ["".join(x.findAll(text=True)) for x in content2.findAll("p")]
    paragraph2div = ["".join(x.findAll(text=True)) for x in content2.findAll("div")]

    if len(paragraph) < 1:
        if test_1p == '':
            if test_1div != '':
                print "test_1div not empty"
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
                paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph1p))
            else:
                print "paragraph_body1p and paragraph_body1div empty"
                content2 = soup.find("div", {"class":"field-item even"})
                paragraph2 = ["".join(x.findAll(text=True)) for x in content2.findAll("div")]
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph2))
                paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph1p))

    elif len(paragraph) >= 1:
        if len(content2) >=1:
            paragraph2p_all = ["".join(x.findAll(text=True)) for x in soup.findAll("div", {"class":"field-items"})]
            paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph2p_all))
            paragraph_body2 = " "
        else:
            if len(test_1p) <400:
                print "paragraph body 1p not correct, using paragraph1div"
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
                paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph1p))

            elif len(test_1p) >=400:
                if test_1div != '':
                    print "test_1div not empty"
                    paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1div))
                    paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph1p))
                else:
                    paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1p))
                    paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph1div))
            
            else:
                paragraph2p_all = ["".join(x.findAll(text=True)) for x in soup.findAll("div", {"class":"field-items"})]
                paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph2p_all))
                paragraph_body2 = " "


    # Perform Quality Check on Parsed Speech
    speech_parser_two_para_QC(url, paragraph_body1, paragraph_body2, release)

    #Get File ID - Date & Time
    #Date
    year_id = url[43:47]
    month_id = url[48:50]
    day_id = url[51:53]
    date_id = year_id+'-'+month_id+'-'+day_id
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
            f.write(release.encode('utf-8'))
            f.write(title.encode('utf-8'))
            f.write(paragraph_body1.encode('utf-8'))
            f.write(paragraph_body2.encode('utf-8'))
            f.close
            return

        elif os.path.isfile(path1) == True:
            if os.path.isfile(path2) == False:
                print "found ID1, no file ID2 found, make ID2"
                f = open(date_id+"_"+"ID2"+".txt", 'w')
                f.write(url2.encode('utf-8'))
                f.write(release.encode('utf-8'))
                f.write(title.encode('utf-8'))
                f.write(paragraph_body1.encode('utf-8'))
                f.write(paragraph_body2.encode('utf-8'))
                f.close
                return
            elif os.path.isfile(path2) == True:
                if os.path.isfile(path3) == False:
                    print "found IDs 1-2, no file ID3 found, make ID3"
                    f = open(date_id+"_"+"ID3"+".txt", 'w')
                    f.write(url2.encode('utf-8'))
                    f.write(release.encode('utf-8'))
                    f.write(title.encode('utf-8'))
                    f.write(paragraph_body1.encode('utf-8'))
                    f.write(paragraph_body2.encode('utf-8'))
                    f.close
                    return
                elif os.path.isfile(path3) == True:
                    if os.path.isfile(path4) == False:
                        print "found IDs 1-3, no file ID4 found, make ID4"
                        f = open(date_id+"_"+"ID4"+".txt", 'w')
                        f.write(url2.encode('utf-8'))
                        f.write(release.encode('utf-8'))
                        f.write(title.encode('utf-8'))
                        f.write(paragraph_body1.encode('utf-8'))
                        f.write(paragraph_body2.encode('utf-8'))
                        f.close
                        return
                    elif os.path.isfile(path4) == True:
                        if os.path.isfile(path5) == False:
                            print "found IDs 1-4, no file ID5 found, make ID5"
                            f = open(date_id+"_"+"ID5"+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(release.encode('utf-8'))
                            f.write(title.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return
                        elif os.path.isfile(path5) == True:
                            print "found IDs 1-5, create random ID"
                            f = open(date_id+"_"+"ID"+randID1+"-"+randID2+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(release.encode('utf-8'))
                            f.write(title.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return 

        
    finally:
        pass



    

##Test URLS
#2014


#urls = ["http://www.whitehouse.gov/the-press-office/2014/01/22/remarks-president-meeting-presidential-commission-election-administratio", "http://www.whitehouse.gov/the-press-office/2014/01/31/remarks-president-long-term", "http://www.whitehouse.gov/the-press-office/2015/06/06/remarks-president-eulogy-honor-beau-biden", "http://www.whitehouse.gov/the-press-office/2012/08/21/remarks-president-campaign-event-reno-nv"]

#2013 urls
#urls = ["http://www.whitehouse.gov/the-press-office/2013/01/25/weekly-address-two-nominees-who-will-fight-american-people", "http://www.whitehouse.gov/the-press-office/2013/01/12/weekly-address-ending-war-afghanistan-and-rebuilding-america", "http://www.whitehouse.gov/the-press-office/2013/02/23/weekly-address-congress-must-act-now-stop-sequester", "http://www.whitehouse.gov/the-press-office/2013/02/02/weekly-address-balanced-approach-growing-economy-2013", "http://www.whitehouse.gov/the-press-office/2013/04/06/weekly-address-president-s-plan-create-jobs-and-cut-deficit", "http://www.whitehouse.gov/the-press-office/2013/06/15/weekly-address-celebrating-fathers-day-weekend"]

#url = "http://www.whitehouse.gov/the-press-office/2013/01/25/weekly-address-two-nominees-who-will-fight-american-people"

#WHT(url)

#for url in urls:
#    WHT(url)






