from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime
import datetime
now = datetime.datetime.now()

def root(request):
    return redirect("/time_display")

def index(request):
    context = {
        "date": datetime.datetime.now().strftime('%B %d, %Y'),
        "time": datetime.datetime.now().strftime('%I:%M %p')
    }
    return render(request,'index.html', context)
