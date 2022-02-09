from .models import Detail
from django import forms

class Detail_form(forms.ModelForm):
    
    class Meta:
        model = Detail
        fields = '__all__'
        labels = {'pic': ''}
        