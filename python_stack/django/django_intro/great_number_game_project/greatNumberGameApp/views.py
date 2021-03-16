from django.shortcuts import render, redirect
import random

def index(request):
    if 'rNumber' not in request.session:
        request.session['rNumber'] = random.randint(1, 100)
    print(request.session['rNumber'])
    return render(request, 'index.html')

def guess(request):
    request.session['guess'] = request.POST['guess']
    if 'guessCount' in request.session:
        request.session['guessCount'] += 1
    else:
        request.session['guessCount'] = 1
    request.session['guess'] = int(request.session['guess'])        
    print(request.POST)
    return redirect('/')

def playAgain(request):
    request.session.clear()
    return redirect('/')

