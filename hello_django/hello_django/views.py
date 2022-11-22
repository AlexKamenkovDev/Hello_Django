from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 6 + 5
    return render(request, 'about.html', {'greeting': a})


def home(request):
    return HttpResponse("This is my homepage")


def mytry(request):
    return render(request, 'mytry.html')
