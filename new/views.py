from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def contact_us(request):
    return HttpResponse("Name   Email    Phone")
def about_us(request):
    return HttpResponse("Tools   pricing   resources   about    customer")

def intro(request):
    return HttpResponse("hello i am nitu")

def index(request):
    person = [
        {'name':'john','age':25},
        {'name':'alice','age':29},
        {'name':'ria','age':43},
        {'name':'rita','age':14},
        
    ]
    context = {
        "name":"Hello hello",
        "age":25,
        "persons":person
    }
    
    return render(request,'index.html',context)
