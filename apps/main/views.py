from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html', {})

def frontpage(request):
    return render(request, 'main/frontpage.html')
