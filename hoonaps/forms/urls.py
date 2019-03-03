from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.location_new, name='location_new'),
]