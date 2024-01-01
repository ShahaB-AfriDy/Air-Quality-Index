
from django.urls import path 
from App_main import views


urlpatterns = [
    path(route='',view=views.Home,name='home'),
    path(route='about/',view=views.About,name='About'),
]
