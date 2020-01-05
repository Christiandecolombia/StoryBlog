from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User

# Render Templates


def index(request):
    print("*********************views/index")
    return render(request, 'main/index.html')


def frontpage(request):
    print("*********************views/frontpage")
    return render(request, 'main/frontpage.html')


def storypage(request):
    print("*********************views/storypage")
    return render(request, 'main/storypage.html')

# Post Form

# Post register user


def register(request):
    print("*********************views/register")
    if request.method == "POST": 
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/')
        else:
            userid=User.objects.create(
                    firsName = request.POST['firstnName'],
                    lastName = request.POST['lastName'],
                    email = request.POST['email'],
                    password = request.POST['password']
                    )
            request.session['userid']=userid.id
            request.session['firstName'] = userid.fname

            return redirect('/main/frontpage')