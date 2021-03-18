from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):

    if 'yourGold' not in request.session:
        request.session['yourGold'] = 0

    if 'activity' not in request.session:
        request.session['activity'] = []

    context = {
        'yourGold': request.session['yourGold'],
        'activities': request.session['activity'],
        }
        
    return render(request, 'index.html', context)


def process_money(request):
    now = datetime.now()

    if 'farm' in request.POST:
        place = 'Farm'
        earned = random.randint(10,20)

    if 'cave' in request.POST:
        place = 'Cave'
        earned = random.randint(5, 10)

    if 'house' in request.POST:
        place = 'House'
        earned = random.randint(2, 5)

    if 'casino' in request.POST:
        place = "Casino"
        earned = random.randint(-50, 50)

    request.session['yourGold'] += earned
    if earned < 0:
        message = 'Entered a Casino and lost ' + str(earned*-1) + ' golds.....Ouch ('
        request.session['activity'].append(message + now.strftime('%Y/%m/%d  %-I:%M %p)'))
        request.session.save()        
    else:
        message = 'Earned ' + str(earned) + ' golds from the ' + place + '  ('
        request.session['activity'].append(message + now.strftime('%Y/%m/%d  %-I:%M %p)'))
        request.session.save()

    return redirect('/')     

def reset(request):
    request.session.clear()
    return redirect('/')