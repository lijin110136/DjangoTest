# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponseRedirect
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
    results = Student.objects.distinct().order_by('id')
    return render_to_response("student/list.html", {"lists" : results},
                               context_instance=RequestContext(request))

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect('/myapp/student/list')
