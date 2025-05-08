from django.shortcuts import render
from .models import ChaiVariety
# Create your views here.
def all_info(req):
    return render(req,'hellotodjango/index.html')

def python(request):
    chais= ChaiVariety.objects.all()
    return render(request,"hellotodjango/python.html",{'chais':chais})