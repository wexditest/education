from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    context={}

    return render(request, "home/home.html", context)
    # return HttpResponse("Hello, world!")