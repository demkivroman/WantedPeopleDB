from django.views.generic.base import TemplateView
from ..forms.add_want_pers_form import AddWanPerson
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import messages

from ..models.wanted_person import WantedPerson

import pdb

class AddPersonForm(TemplateView):
    template_name = "forms/add_form.html"


class ContactForm(TemplateView):
    template_name = "forms/contact_form.html"

def add_wanted_person(request):
    if request.method == 'POST':
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('add_person'))
        if request.POST.get('add_button') is not None:
            data = {}
            data['first_name'] = request.POST.get('first_name').strip()
            data['last_name'] = request.POST.get('last_name').strip()
            data['photo'] = request.FILES.get('photo')
            birthday = request.POST.get('birthday').strip()
            if not birthday:
                data['birthday'] = None
            else:
                data['birthday'] = request.POST.get('birthday').strip()
            data['phone'] = request.POST.get('phone').strip()
            data['email'] = request.POST.get('email').strip()
            data['note'] = request.POST.get('note').strip()
            # create and save person object
            person = WantedPerson(**data)
            person.save()

            messages.success(request, 'Add successfully :)')
            return HttpResponseRedirect(reverse('home'))

         
    else:
        form = AddWanPerson()
        return render(request, 'forms/add_form.html', {'form':form})
