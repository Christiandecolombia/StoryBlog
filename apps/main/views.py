from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.models import User
from .models import Story
from .forms import UserCreateForm

################################################################
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            print("*************views/is_valid")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session['userid']=user.userid
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            print("*************views/is_valid/login")
            return redirect('/main/frontpage')
    else:
        print("*************views/UserCreateForm")
        form = UserCreateForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)
################################################################
# Render Templates
def logout(request):
    print("*********************views/logout")
    request.session.clear()
    return redirect('/')

    

def index(request):
    print("*********************views/index")
    return render(request, 'main/index.html')

def frontpage(request):
    print("*********************views/frontpage")
    return render(request, 'main/frontpage.html')


def storypage(request):
    print("*********************views/storypage")
    return render(request, 'main/storypage.html')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect ('/main/frontpage')
        
    else:
        # Return an 'invalid login' error message.
        return redirect ('/')

        
################################################################

# Post Story

# class Story(models.Model):
#     title = models.CharField(max_length=25)
#     mainbody = models.TextField()
#     pubDate = datetime.datetime.now()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     objects = Storymanager()

def addstory(request):
    return render(request, 'main/addstory.html')

    # if render.method == "POST":
        
    # else 
    # print("*********************views/addstory")
    # return render(request, 'main/addstory.html')

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