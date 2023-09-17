from typing import Collection
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# from database.database import post_db
# Create your views here.
from con_func.function import query_by_id, post_db, get_db_browse, post_mongodb_registered
from con_func.emails import email_send


def homepage(request):
    he = {1: "coming from backend"}
    # NO backend code required here
    return render(request, 'home.html', {'hel': he})


def postEvent(request):
    return render(request, 'hosting.html')


def hostDone(request):
    # DATABASE CONNECTION MONGODB
    # collection = mongoConnection_collection()
    if request.method == 'POST':
        print(request.POST.get('event_name'))
        post_db({
            'your_name': request.POST.get('your_name'),
            'email': request.POST.get('email'),
            'mobile_no': request.POST.get('mobile_no'),
            'event_name': request.POST.get('event_name'),
            'event_date': request.POST.get('event_date'),
            'event_time': request.POST.get('event_time'),
            'event_location': request.POST.get('event_location'),
            'event_detail': request.POST.get('event_detail')
        })
    # POST
    return render(request, 'host_done.html')


def browseEvents(request):
    # DATABASE CONNECTION MONGODB
    if request.method == "GET":

        query = get_db_browse(request)
    return render(request, 'browsing.html', {'query': query})


def regDone(request, id):

    if request.method == "POST":
        name = request.POST.get('your_name')
        email = request.POST.get('email')
        query = query_by_id(id)
        event_name = query[0].get('event_name')
        event_date = query[0].get('event_date')
        event_time = query[0].get('event_time')
        event_location = query[0].get('event_location')
        event_detail = query[0].get('event_detail')
        organiser_contact = query[0].get('email')

        email_send(name, email, event_name, event_date, event_time, event_location, event_detail, organiser_contact)
        post_mongodb_registered(name, email, event_name)

        print(id)
    # No Backend Code Needed
    # Button to redirect to the homepage
    # get data to register for the event
    return render(request, 'reg_done.html')




def register(request, id):
    if request.method == "GET":
        query, id = query_by_id(id)
    return render(request, 'register.html', {'query': query, 'id': id})
