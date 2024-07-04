from django.shortcuts import render
from django.http import HttpResponse
from flan.models import Flan

# Create your views here.
def index(request):
    # este comando me trae todos los objetos flanes
    #flans = Flan.objects.all()
    flans = Flan.objects.filter(is_private=False)
    context ={'flans':flans }
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')

def welcome(request):
    flans = Flan.objects.filter(is_private=True)
    context ={'flans':flans }
    return render(request, 'web/welcome.html', context)
