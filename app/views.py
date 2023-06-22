from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn = input('enter tipic name :')
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    return HttpResponse('topic is created')
def insert_webpage(request):
    tn = input('enter topic name :')
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    N = input('enter name :')
    U = input('enter url :')
    WO = Webpage.objects.get_or_create(topic_name= TO,name=N,url=U)[0]
    WO.save()
    return HttpResponse('webpage is created')
def insert_access(request):
    tn = input('enter topic name :')
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    N = input('enter name :')
    U = input('enter url :')
    WO = Webpage.objects.get_or_create(topic_name= TO,name=N,url=U)[0]
    WO.save()
    D = input('enter the date :')
    A = input('enter author :')
    AR = AccessRecord.objects.get_or_create(name=WO,date=D,author = A)
    return HttpResponse('accessRecords is created')


def display_topics(request):
    topics = Topic.objects.all()
    d = {'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages = Webpage.objects.all()
    d = {'webpages':webpages}
    return render(request,'display_webpages.html',d)
def display_access(request):
    access = AccessRecord.objects.all()
    d = {'access':access}
    return render(request,'display_access.html',d)