from django.urls import path
from RFR import views

urlpatterns = [
    path('RFR_Model/',views.RFR_Model,name='RFR_Model'),
    path('RFR-result/',views.RFR_Result,name='RFR_result'),
]
