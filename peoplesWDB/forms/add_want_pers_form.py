from django.forms import ModelForm
from ..models.wanted_person import WantedPerson

class AddWanPerson(ModelForm):
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data:
            raise ValidationError('Field is required')

        return data

    class Meta:
        model = WantedPerson
        fields = '__all__'
