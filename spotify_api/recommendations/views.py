from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.db.models import Q
from .models import *

def input(request):
    return render(request, 'recommendations/input.html')

def output(request):
    return render(request, 'recommendations/output.html')