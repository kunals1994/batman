from django.shortcuts import render
import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


# Create your views here.
def home(request):
	return HttpResponse(open("assets/html/index.html").read())

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
