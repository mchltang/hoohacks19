from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Location
from django.views import generic
from .forms import LocationForm

def index(request):
    location_list = Location.objects.all()
    context = {'location_list': location_list}
    return render(request, 'forms/index.html', context)
    # template_name = 'forms/index.html'
    # return render(request, template_name)

def location_new(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('/forms/')
    else:
        form = LocationForm()
    return render(request, 'forms/new_location.html', {'form': form})