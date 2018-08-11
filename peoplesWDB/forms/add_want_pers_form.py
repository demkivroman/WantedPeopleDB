from django.forms import ModelForm
from ..models.wanted_person import WantedPerson
from django import forms

class AddWanPerson(ModelForm):
    class Meta:
        model = WantedPerson
        fields = ['first_name','last_name','photo','first_name','birthday','phone',
                 'email','country','city','note']
        widgets = {
            'note': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'email': forms.EmailInput(attrs={'size': 30}),
            'phone': forms.TextInput(attrs={'size': 25}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

