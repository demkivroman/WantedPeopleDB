from django.forms import ModelForm
from ..models.wanted_person import WantedPerson

class AddWanPerson(ModelForm):
    class Meta:
        model = WantedPerson
        fields = '__all__'
