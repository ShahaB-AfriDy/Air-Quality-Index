from django.urls import path
from MLR import views

urlpatterns = [
    path('MLR_Model/',views.MLR_Model,name='MLR_Model'),
    path('MLR-result/',views.MLR_Result,name='MLR_result'),
]
