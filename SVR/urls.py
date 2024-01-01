from django.urls import path
from SVR import views

urlpatterns = [
    path('SVR_Model/',views.SVR_Model,name='SVR_Model'),
    path('SVR-result/',views.SVR_Result,name='SVR_result'),
]
