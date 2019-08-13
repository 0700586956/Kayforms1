from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mainpage(request):
    return render(request=request,
                 template_name="main/mainpage.html",
                 context={})

def signup(request):
    return render(request=request,
                 template_name="main/signup.html",
                 context={})
                
def login(request):
    return render(request=request,
                 template_name="main/login.html",
                 context={})