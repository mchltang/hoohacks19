from django.urls import path
from . import views

app_name = 'naps'
urlpatterns = [
    # ex: /napSpots/
    path('', views.index, name='index'),
    # ex: /napSpots/5/
    path('<int:spot_id>/', views.detail, name='detail'),
]
