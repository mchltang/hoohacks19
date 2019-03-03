from django.urls import path
from . import views

app_name = 'naps'
urlpatterns = [
    # ex: /napSpots/
    path('', views.index, name='index'),
    
    path('addSpot/', views.addSpot, name='addSpot'),

    path('list/', views.list, name='list'),
    # ex: /napSpots/5/
    path('<int:spot_id>/', views.detail, name='detail'),

]
