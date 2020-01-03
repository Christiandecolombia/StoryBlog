from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    print("*********************views/index")
    return render(request, 'main/index.html')

def frontpage(request):
    print("*********************views/frontpage")
    return render(request, 'main/frontpage.html')
    