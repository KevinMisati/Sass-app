import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):
    path = request.path
    queryset = PageVisit.objects.filter(path = request.path)
    context = {"name":"Kevin","page_visit_count":queryset.count()}
    PageVisit.objects.create(path=request.path)
    return render(request,"home.html",context)