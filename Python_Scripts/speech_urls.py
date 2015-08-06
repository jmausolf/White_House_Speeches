##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def speech_urls(sub_pages_url):
    """Returns all the speech URLs extentions for a given sub-pages URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(sub_pages_url).read())
	
    #Speech URLs
    content = soup.find("div", {"class":"view-content"})
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speechurls.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            f.write(u'%s\n' % (speech_url))
    finally:
        f.close()


def speech_urls_current(sub_pages_url):

    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(sub_pages_url).read())
    
    #Speech URLs
    content = soup.find("div", {"class":"view-content"})
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speech_urls_current.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            f.write(u'%s\n' % (speech_url))
    finally:
        f.close()

#Ok, so this worked, but is a lame work around. 
#speech_urls_current("https://www.whitehouse.gov/briefing-room/Speeches-and-Remarks")
speech_urls_current("file:///Users/Josh/Google%20Drive/SOCIOLOGY/COMPUTING/White_House_Speech_Crawler/Python_Scripts/test_current.html")


