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
    try:
        content = soup.find("div", {"class":"view-content"})
        speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    except:
        print "no speech urls found for this subpage..."
        pass
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speechurls.csv', 'a')
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


