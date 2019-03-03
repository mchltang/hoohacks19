from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Spot, Building



def index(request):
    #this is the landing page
    building_list = Building.objects.order_by('name')
    context = {'building_list': building_list}
    return render(request, 'naps/index.html', context)

def list(request):
    #this is the landing page
    building_list = Building.objects.order_by('name')
    context = {'building_list': building_list}
    return render(request, 'naps/list.html', context)

def detail(request, spot_id):
    #this is the detail page for a nap spot
    spot = get_object_or_404(Spot, pk=spot_id)
    return render(request, 'naps/detail.html', {'spot': spot})

def addSpot(request):
    #this is where users can submit a spots
    return render(request, 'naps/addSpot.html')
