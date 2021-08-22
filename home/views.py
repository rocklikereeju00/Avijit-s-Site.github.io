# I am create this file
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
from datetime import datetime

def page(request):
    return render(request, 'index.html' )


def index(request):
    context = {
        "variable1": "HI I am Avijit",
        "variable2": "HI I am a web developer"
    }
    return render(request, 'index.html', context )


def about(request):
    return render(request, 'about.html' )

def eCommerce(request):
   return render(request, 'eCommerce.html' )


def Personal(request):
    return render(request, 'Personal.html')

def services(request): 
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        city = request.POST.get('city')
        subject=request.POST.get('subject')
        contact = Contact(name=name, email=email, phone=phone, comment=comment, city=city,subject=subject, date= datetime.today())
        contact.save()

    return render(request, 'contact.html')

def removing(request):
    return HttpResponse("removing")


def capitalize(request):
    return HttpResponse("capitalize")


def line_remover(request):
    return HttpResponse("line_remover")


def spa(request):
    return HttpResponse("spa")
