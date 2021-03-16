from django.shortcuts import render, redirect

# this is the route that shows the form
def index(request):
    return render(request, "index.html")

def create_user(request):
    # this is the route that processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        'name_on_template': name_from_form,
        'email_on_template' : email_from_form
    }
    return redirect('/success')
# this is the success route
def success(request):
    return render(request, 'success.html')