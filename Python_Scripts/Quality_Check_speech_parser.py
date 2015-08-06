    ##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def speech_parser_QC(url, paragraph_body, release=None):

    if len(paragraph_body) < 200:
        try:
            f=open('QC_Check_Paragraph_speechurls.csv', 'a')
            f.write(u'%s\n' % (url))
        finally:
            print "WARNING SHORT PARGRAPH PARSED. NEEDS INVESTIGATION"
            print "Writing suspect speech url to csv..."
            f.close()
    elif release==None:
        pass

    elif release != None:
        if len(release) < 25:
            try:
                f=open('QC_Check_Release_speechurls.csv', 'a')
                f.write(u'%s\n' % (url))
            finally:
                print "WARNING SHORT RELEASE PARSED. NEEDS INVESTIGATION"
                print "Writing suspect speech url to csv..."
                f.close()   


def speech_parser_two_para_QC(url, paragraph_body1, paragraph_body2):

    if len(paragraph_body1) < 200 and len(paragraph_body2) < 200:
        try:
            f=open('QC_Check_Paragraph_speechurls.csv', 'a')
            f.write(u'%s\n' % (url))
        finally:
            print "WARNING SHORT PARGRAPH PARSED. NEEDS INVESTIGATION"
            print "Writing suspect speech url to csv..."
            f.close()


def speech_parser_skip_QC(url):
    try:
        f=open('QC_no_parse_speechurls.csv', 'a')
        f.write(u'%s\n' % (url))
        f.close()
    except:
        print "url not added to exception list"
        pass


url = "http://www.whitehouse.gov/the-press-office/2012/10/28/remarks-president-hurricane-sandy"
#speech_parser_skip_QC(url)
