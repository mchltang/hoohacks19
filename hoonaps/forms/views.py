from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Location
from django.views import generic

def index(request):
    location_list = Location.objects.all()
    context = {'location_list': location_list}
    return render(request, 'forms/index.html', context)
    # template_name = 'forms/index.html'
    # return render(request, template_name)