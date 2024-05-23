from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is pratice_app home page")
    return render(request,'pratice_app/home.html')