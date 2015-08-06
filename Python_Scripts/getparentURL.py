##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

def getURL(year, month):

	base_url = "http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/"+year+"/"+month
	print base_url


def getyrURL(year):
	base_url = "http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/"+year+"/"
	return base_url


def getparentURLs(yr1=2009, yr2=2016, month1=1, month2=12):

	import itertools

	years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	index_yr1 = yr1-2009
	index_yr2 = yr2-2009
	index_mo1 = month1-1
	index_mo2 = month2-1


	req_years = years[index_yr1:index_yr2+1]
	req_months = months[index_mo1:index_mo2+1]

	x = (list(itertools.product(req_years, req_months)))


	f = open('parentURLs.csv', 'w')
	try:
		f.write(u'PARENT_URLS\n')
		for year in req_years:
			urls = getyrURL(year)
			for month in req_months:
				full_url = urls+month
				f.write(u'%s\n' % (full_url))
	finally:
		f.close()








