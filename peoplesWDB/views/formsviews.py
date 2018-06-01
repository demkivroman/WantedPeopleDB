from django.views.generic.base import TemplateView
from ..forms.add_want_pers_form import AddWanPerson
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

class AddPersonForm(TemplateView):
    template_name = "forms/add_form.html"


class ContactForm(TemplateView):
    template_name = "forms/contact_form.html"


def add_wanted_person(request):

    if request.method == 'POST':
        form = AddWanPerson(request.POST)
    else:
        form = AddWanPerson()
        return render(request, 'forms/add_form.html', {'form':form})
