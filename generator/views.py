from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get("numbers"):
        
        character.extend(list('0123456789'))

    if request.GET.get("special"):
        character.extend(list('!@#$%&*()?><'))

    length = int(request.GET.get("length",12))
    thepassword =''

    for i in range(length):
        thepassword += random.choice(character)

    return render(request,'generator/password.html', {"password" : thepassword})
    
def about(request):
    return render(request,'generator/about.html')
