from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {'name' : 'Zedd' , 'age' : 11},
        {'name' : 'Khan' , 'age' : 20},
        {'name' : 'Vickey' , 'age' : 14},
        {'name' : 'Srk' , 'age' : 40},
        {'name' : 'Salman' , 'age' : 45}
    ]

    return render(request, 'home/index.html' , context = {'page' : 'Django 2023 tut' , 'peoples' : peoples })

def about(request):
    context = {'page' : 'About'}
    return render(request, 'home/about.html' , context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'home/contact.html' , context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Success!</h1>")