from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Location
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Location.objects.order_by('location_name')

def add(request):
    # used to view details of one location
    return HttpResponse("There should be a form here.")

class DetailView(generic.DetailView):
    model = Location
    template_name = 'forms/detail.html'