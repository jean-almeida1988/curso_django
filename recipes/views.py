from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')

def contact(request):
    return render(request, 'recipes/contacts.html')

def about(request):
    return HttpResponse('About')

