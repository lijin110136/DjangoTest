# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime 
def current_datetime(request):
	return render_to_response('index.html', {'title':'我的地盘，我做主了!'})
