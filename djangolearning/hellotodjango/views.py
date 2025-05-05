from django.shortcuts import render

# Create your views here.
def all_info(req):
    return render(req,'hellotodjango/index.html')

def python(request):
    return render(request,"hellotodjango/python.html")