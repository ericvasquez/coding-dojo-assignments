from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    print("request.POST info.........")
    print(request.POST)
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    languages_from_form = request.POST.getlist('languages')
    comment_from_form = request.POST['comment']
    context = {
        'name_on_result' : name_from_form,
        'location_on_result' : location_from_form,
        'languages_on_result' : languages_from_form,
        'comment_on_result' : comment_from_form
    }
    return render(request, 'result.html', context)
