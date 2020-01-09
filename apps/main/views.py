from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User, Story

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

def addstory(request):
    print("*********************views/addstory")
    return render(request, 'main/addstory.html')

# Post Form

# Post register user
def postRegister(request):
    print("*********************views/register/POST")
    if request.method == "POST": 
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/')
        else:
            userid=User.objects.create(
                    firstName = request.POST['firstName'],
                    lastName = request.POST['lastName'],
                    email = request.POST['email'],
                    password = request.POST['password']
                    )
            request.session['userid']=userid.id
            request.session['firstName'] = userid.firstName
            request.session['lastName'] = userid.lastName

            return redirect('/main/frontpage')

# Post login user
def postLogin(request):
    print("*********************views/login/POST")
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/')
        else:
            userid=User.objects.get(email = request.POST['logEmail'])
            request.session['userid']=userid.id
            request.session['firstName'] = userid.firstName

            return redirect('/main/frontpage')

# Post Story

# class Story(models.Model):
#     title = models.CharField(max_length=25)
#     mainbody = models.TextField()
#     pubDate = datetime.datetime.now()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     objects = Storymanager()
def postAddStory(request):
    print("*********************views/postAddStory/POST")
    if request.method == "POST":
        errors = User.objects.story_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect ('/main/addstory')
        else:
            User.objects.create(
                title = request.POST['title'],
                mainbody = request.POST['story'],
                user = User.objects.get(id=request.session['userid']),
                )
            return redirect('/main/frontpage')