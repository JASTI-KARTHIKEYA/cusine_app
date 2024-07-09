from django.shortcuts import render
from django.http import HttpResponse
from .models import Starters,main_course,desserts

# def index(request):
#     return render(request,"food/index1.html")

def index(request):
    context={'active-link':'index'}
    return render(request, 'index.html')

def starters(request):
    starter = Starters.objects.all()
    context = {
        'starter': starter,'active-link':'starters'
    }
    return render(request, 'starters.html', context)

def maincourse(request):
    mains = main_course.objects.all()
    context = {
        'mains': mains,'active-link':'mains'
    }
    return render(request, 'Main_course.html', context)

def deserts(request):
    dess = desserts.objects.all()
    context = {
        'dess': dess,'active-link':'deserts'
    }
    return render(request, 'Desserts.html', context)