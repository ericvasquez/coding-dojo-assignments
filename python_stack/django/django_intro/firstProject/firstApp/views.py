from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")
# def index(request):
#     return render(request, "index.html")

#With Django, we are able to pass data to the template via the render method.  We do this by passing a single dictionary whose keys will be the variable names available on the template. For example:
    
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
