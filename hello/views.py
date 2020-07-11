from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, Internet")

def profile(request, name):
    return render(request, "hello/profile.html", {
        "name": name.capitalize()
    })