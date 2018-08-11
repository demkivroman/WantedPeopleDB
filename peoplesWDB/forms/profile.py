from django.forms import ModelForm
from ..models.profile import Profile
from django import forms

class profilePhoto(ModelForm):
    class Meta:
        model = Profile
        fields =['photo']
        
        widgets = {
            'photo': forms.FileInput(attrs={'id': 'photoAdd'}),
        }
