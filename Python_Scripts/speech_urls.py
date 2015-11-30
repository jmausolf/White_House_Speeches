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


def speech_urls_current_data_old(current_pages_data):
    """This function opens and reads a saved html file.
    It generates a list of speech urls from this saved html file."""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    html_data = open(current_pages_data,'r').read()
    #Base Page
    soup = BeautifulSoup(html_data)
    
    #Speech URLs
    content = soup.find("div", {"class":"view-content"})
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speech_urls_current_data.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            f.write(u'%s\n' % (speech_url))
    finally:
        f.close()

def speech_urls_current_data(current_pages_data):
    """This function opens and reads a saved html file.
    It generates a list of speech urls from this saved html file."""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    html_data = open(current_pages_data,'r').read()
    #Base Page
    try:
        soup = BeautifulSoup(html_data, 'html5lib')
    #print soup
    except:
        soup = BeautifulSoup(html_data)
        print "EXCEPTION: Please <pip install html5lib> from your terminal."
        print "html5lib is critical. Otherwise you will experience suboptimal parsing..."
    #Speech URLs
    content = soup.find("div", {"class":"view-content"})
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speech_urls_current_data.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            f.write(u'%s\n' % (speech_url))
    finally:
        f.close()

#speech_urls("file:///Users/Joshua/Documents/COMPUTING/White_House_Speech_Crawler_PKG/Shell_Command/whitehouse_current.html")
#speech_urls_current_data2("whitehouse_current_edit.html")
#speech_urls_current_data("whitehouse_current.html")

#outfile = "whitehouse_current_speechs_remarks.html"

#outfile = "whitehouse_current_weekly_address.html"
#speech_urls_current_data(outfile)






def speech_urls_current_data_wa(current_pages_data):
    """This function opens and reads a saved html file.
    It generates a list of speech urls from this saved html file."""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    html_data = open(current_pages_data,'r').read()
    #Base Page
    try:
        soup = BeautifulSoup(html_data, 'html5lib')
    #print soup
    except:
        soup = BeautifulSoup(html_data)
        print "EXCEPTION: Please <pip install html5lib> from your terminal."
        print "html5lib is critical. Otherwise you will experience suboptimal parsing..."
    
    #Speech URLs
    content = soup.find("div", {"class":"panel-pane pane-views-panes pane-press-office-listings-panel-pane-5"})

    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speech_urls_current_data.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            
            if "#" in speech_url:
                discard = speech_url
            elif "mp3" in speech_url:
                discard = speech_url
            elif "mp4" in speech_url:
                discard = speech_url
            elif "https:" in speech_url:
                discard = speech_url
            elif "?page=" in speech_url:
                discard = speech_url
            elif "weekly-address-" not in speech_url:
                discard = speech_url              
            else:
                write_speech_url = speech_url
            
            f.write(u'%s\n' % (write_speech_url))
    finally:
        f.close()

#outfile = "whitehouse_current_weekly_address.html"
#speech_urls_current_data_wa(outfile)
