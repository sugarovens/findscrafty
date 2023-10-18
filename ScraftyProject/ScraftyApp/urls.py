from django.urls import path
from . import views

urlpatterns = [
    path('scrafty/', views.find_scrafty, name='find_scrafty'),
]