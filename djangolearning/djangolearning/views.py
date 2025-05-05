from django.http import HttpResponse
from django.shortcuts import render
# def home(request):
#     # return HttpResponse("hello world home")
#     return render(request,"index.html")

# def about(request):
#     return HttpResponse("hello world about")

# def contact(request):
#     return HttpResponse("hello world contact")

def intro(request):
    return render(request,"intro.html")