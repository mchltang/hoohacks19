from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Spot, Building
from .naps import SpotForm



def index(request):
    #this is the landing page
    spot_list = Spot.objects.all()
    context = {'spot_list': spot_list}
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

def add_spot(request):
    if request.method == "POST":
        form = SpotForm(request.POST)
        if form.is_valid():
            spot = form.save(commit=False)
            spot.save()
            return redirect('/map/')
    else:
        form = SpotForm()
    return render(request, 'naps/add_spot.html', {'form': form})
