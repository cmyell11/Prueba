from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('mytemplate.html', locals())

def hours_ahead(request, offset):
	hour_offset = int(offset)
	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	
	return render_to_response('hours_ahead.html', locals())

def index(request):
	html = "<h1>welcome</h1>"
	return HttpResponse(html)




