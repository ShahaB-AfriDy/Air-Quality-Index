from django.urls import path
from XGB import views

urlpatterns = [
    path('XGB_Model/',views.XGB_Model,name='XGB_Model'),
    path('XGB-result/',views.XGB_Result,name='XGB_result'),
]
