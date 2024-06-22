from http.client import HTTPResponse
from django.shortcuts import render, redirect ,HttpResponse
from django.http import HttpResponse
from app.forms import monii
from app.models import moni



def index(request):
    if request.method =="POST":
        form = monii(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = monii

    context = {
        'form': form
    }
    return render(request, 'index.html',context)