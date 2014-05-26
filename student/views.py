# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from models import Student
# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    #print query
    if query:
        qset = (Q(sname=query))
        results = Student.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search/search.html', {"results": results, "query": query})
def list(request):
    results = Student.objects.distinct()
    return render_to_response("")
