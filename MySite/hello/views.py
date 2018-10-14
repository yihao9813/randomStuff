from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

print("http://127.0.0.1:8000/hello/VSCode")

def home(request):
    return HttpResponse("Hello,Django!")

def hello_there(request, name):
    return render(
        request,"hello/hello_there.html",{
            'name':name,
            'date':datetime.now()
        }
    )
# Create your views here.