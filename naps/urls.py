from django.urls import path
from . import views

app_name = 'naps'
urlpatterns = [
    # ex: /nap_spots/
    path('', views.index, name='index'),

    path('add_spot/', views.add_spot, name='add_spot'),

    path('list/', views.list, name='list'),
    # ex: /nap_spots/5/
    path('<int:spot_id>/', views.detail, name='detail'),

]
