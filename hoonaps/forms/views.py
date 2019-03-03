from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Location
from django.views import generic

def index(request):
    template_name = 'forms/index.html'
    return render(request, template_name)