import urllib
import urllib2
import os

url = "http://www.ucrdatatool.gov/Search/Crime/Local/DownCrimeOneYearofDataLarge.cfm/LocalCrimeOneYearofData.csv"

values = {
	"CrimeCrossId" : 
	"40,47,53"
	,
	"YearStart" : "2012",
	"YearEnd" : "2012", 
	"DataType" : "1,2,3,4"
}

def get_data(year):

	values["YearStart"] = year
	values["YearEnd"] = year

	data = urllib.urlencode(values)

	req = urllib2.Request(url, data)
	req.add_header('Host', 'www.ucrdatatool.gov')
	req.add_header('Cache-Control', 'max-age=0')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
	req.add_header('Origin', 'http://www.ucrdatatool.gov')
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36')
	req.add_header('Content-Type', 'application/x-www-form-urlencoded')
	req.add_header('Referer', 'http://www.ucrdatatool.gov/Search/Crime/Local/RunCrimeOneYearofDataLarge.cfm')
	req.add_header('Accept-Encoding', 'gzip,deflate')
	req.add_header('Accept-Language', 'en-US,en;q=0.8')
	req.add_header('Cookie', 'topItem=-1c; CFID=58464003; CFTOKEN=8763b89c94d72ce6-A3996A1D-B70C-976D-8208D06DE0B7074F')

	response = urllib2.urlopen(req)

	f_out = open(year+".csv", 'w')

	for line in response:
		if (len(line.split(",")) >= 4):
			f_out.write(line)

	f_out.close()


year = 2014
while(True):
	try:
		get_data(str(year))
		year -=1
		print str(year) + " found"
	except:
		print str(year) + " caused exception"
		year -=1