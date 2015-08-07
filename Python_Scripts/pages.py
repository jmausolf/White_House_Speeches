##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def pages(url):
    """Returns the number of additional pages for a given parent URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(url).read())
	
    #Page Counter
    page_counter = soup.find("div", {"class":"item-list"})
    try:
        paragraph = ["".join(x.findAll(text=True)) for x in page_counter.findAll("li", {"class":"pager-item"})]
        return len(paragraph)
    except:
        return 0

def pages_current(url):
    """Returns the number of additional pages for a given parent URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    
    #Page Counter
    page_counter = soup.find("div", {"class":"item-list"})
    try:
        paragraph = ["".join(x.findAll(text=True)) for x in page_counter.findAll("li", {"class":"pager-current"})]
        return len(paragraph)
    except:
        return 0


def sub_pages_URLs(parent_url):
    """The function creates a list of subpages given a parent URL.
    It makes use of the pages(url) function."""

    base_url = parent_url+"?page="

	# Number of Pages
    total_pages = pages(parent_url)
    try:
        f=open('subpages.csv', 'a')
        for i in range(0, total_pages+1):
            sub_page_url = base_url+str(i)
            f.write(u'%s\n' % (sub_page_url))
    finally:
        f.close()

def sub_pages_URLs_current(parent_url):
    """The function creates a list of subpages given a parent URL.
    It makes use of the pages(url) function."""

    base_url = parent_url+"?page="

    # Number of Pages
    total_pages = pages_current(parent_url)
    try:
        f=open('subpages.csv', 'a')
        for i in range(0, total_pages+1):
            sub_page_url = base_url+str(i)
            f.write(u'%s\n' % (sub_page_url))
    finally:
        f.close()

#sub_pages_URLs_current("https://www.whitehouse.gov/briefing-room/Speeches-and-Remarks")




