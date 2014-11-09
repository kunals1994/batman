from django.shortcuts import render
import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from crime_stats import news_analyzer

# Create your views here.
def home(request):
	return HttpResponse(open("assets/html/index.html").read())

def crime(request):
	city_name = request.GET.get("city")
	score, html = news_analyzer.getNews(city_name.replace(' ', '%20') + "%20crime")

	template = open("assets/html/crime.html").read()

	params = {}

	params["news_html"] = html
	params["city_name"] = city_name
	params["city_violent_crime"] = []
	params["city_property_crime"] = []
	params["national_violent_crime"] = [471.8 * 1.3, 458.6 * 1.3, 431.9 * 1.3, 404.5 * 1.3, 387.1 * 1.3, 386.9 * 1.3]
	params["national_property_crime"] = [3276.4 * 1.2, 3214.6 * 1.2, 3041.3 * 1.2, 2945.9 * 1.2, 2905.4 * 1.2, 2859.2 * 1.2]
	params["url"] = "http://www.google.com/search?&sourceid=navclient&btnI=I&q=" + city_name.replace('_','%%20') + "%%20Police%%20Department"

	f_in = "assets/datasets/large_local/"

	for filename in os.listdir("assets/datasets/large_local"):
		if city_name.lower() in filename.lower():
			f_in += filename
			break

	f_in = open(f_in, 'r')
	first = True
	for line in f_in:
		if(first):
			first = False
			continue

		line_arr = line.split(",")
		if ("2007" in line or "2008" in line or "2009" in line or "2010" in line or "2011" in line or "2012" in line):
			params["city_violent_crime"].append(float(line_arr[13]))
			params["city_property_crime"].append(float(line_arr[18]))


	params["score"] = str(int(((score * 10) + 10)/2))


	return HttpResponse(template % params)

def assets(request):
    rel_path = request.path
    abspath = "." + rel_path

    response = HttpResponse()
    response['Content-Type'] = 'text'

    if(".css" in rel_path):
        myfile = open(abspath, 'r')
        response = HttpResponse(FileWrapper(myfile), content_type='text/css')

    elif(".js" in rel_path):
        myfile = open(abspath, 'r')
        response = HttpResponse(FileWrapper(myfile), content_type='text/css')

    elif(".png" in rel_path or ".jpg" in rel_path or ".jpeg" in rel_path or ".ico" in rel_path):
        myfile = open(abspath, 'r')
        response = HttpResponse(FileWrapper(myfile), content_type='image')
        response['Content-Length'] = os.path.getsize(abspath)
        response['Content-Disposition'] = "attachment; filename=%s" % rel_path[rel_path.rfind('/')+1:]
        return response

    try:
        response.content = open(abspath, 'r').read()
    except:
        return HttpResponse("")

    return response
