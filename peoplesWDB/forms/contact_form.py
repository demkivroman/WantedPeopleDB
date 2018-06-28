from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(label='Email', 
                              required = True,
                              widget = forms.EmailInput(attrs={'size': 35}))
    message = forms.CharField(label = 'Message', 
                              required = True, 
                              widget = forms.Textarea(attrs={'cols': 90, 'rows': 5}))
