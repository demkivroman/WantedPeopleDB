from django.forms import ModelForm
from ..models.wanted_person import WantedPerson
from django import forms

class AddWanPerson(ModelForm):
    class Meta:
        model = WantedPerson
        fields = '__all__'
        widgets = {
            'note': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'email': forms.EmailInput(attrs={'size': 30}),
            'phone': forms.TextInput(attrs={'size': 25})
        }
