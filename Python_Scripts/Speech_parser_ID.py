##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def Parser_ID(url):
    """Identifies correct parser for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys, random
    import os
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    #Content Types
    content1 = soup.find("div", {"class":"date"})
    content2 = soup.find("div", {"class":"information"})
    content3 = soup.find("div", {"class":"legacy-content"})
    content4 = soup.find("div", {"class":"legacy-para"})
    

    try:
        if content1 is not None:
            #Perform Test 2:
            #print "Use WHT1"
            return 1
        elif content1 is None:
            #print "Don't Use WHT1"
            if content2 is not None:
                #print "Use WHT2"
                return 2
            elif content2 is None:
                if content3 is not None:
                    if content4 is None:
                        #print "Use WHT2"
                        return 2
                    elif content4 is not None:
                        #print "Use WHT3"
                        return 3
            else:
                #print "else pass"
                pass

    except:
        #print "except pass"
        pass

