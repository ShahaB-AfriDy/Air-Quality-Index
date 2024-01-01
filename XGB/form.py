# forms.py
from django import forms

class XGB_Form(forms.Form):
    # PM2.5	PM10	NO2	CO	SO2	O3
    PM2_5 = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"PM2.5"}),label='')
    PM10 = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"PM10"}),label='')
    NO2 = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'NO2'}),label='')
    CO = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'CO'}),label='')
    SO2 = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"SO2"}),label='')
    O3 = forms.FloatField(min_value=0,max_value=500,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'O3'}),label='')




