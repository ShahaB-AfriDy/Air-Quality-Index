from django.urls import path
from Graph import views

urlpatterns = [
    path('Graphs/',views.Graphs,name='Graphs'),
]
