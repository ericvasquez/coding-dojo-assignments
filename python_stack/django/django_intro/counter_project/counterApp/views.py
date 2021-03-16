from django.shortcuts import render, redirect

def index(request):
# If there is a value in counter add +1
    if 'counter' in request.session:
        request.session['counter'] += 1
# If there is no counter, create one and set = 1
    else:
        request.session['counter'] = 1
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    return render(request, "index.html")

def destroy_session(request):
    del request.session['counter']
    return redirect("/")

def destroy_visits(request):
    del request.session['visits']
    return redirect("/")

def plusTwo(request):
    request.session['counter'] += 1
    return redirect("/")

def addNumber(request):
    request.session['number'] = request.POST['number']
    request.session['counter'] += int(request.session['number'])-1
    return redirect("/")