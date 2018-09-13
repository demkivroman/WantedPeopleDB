from django.views.generic.base import TemplateView
from ..forms.add_want_pers_form import AddWanPerson
from ..forms.contact_form import ContactForm
from ..forms.profile import profilePhoto
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from wantedDB.settings import ADMIN_EMAIL
from django.contrib.auth.models import User

from ..models.wanted_person import WantedPerson
from ..models.comment import Comment
from ..util.util_func import util_main_searc
from django.http import JsonResponse
import json

import pdb

class AddPersonForm(TemplateView):
    template_name = "forms/add_form.html"


def contact_form(request):
    if request.method == 'POST':
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('contact'))
        if request.POST.get('send_button') is not None:
            sender = request.POST.get('sender').strip()
            message = request.POST.get('message').strip()
            try:
                send_mail(sender,message,sender,[ADMIN_EMAIL])
            except Exception:
                message = "Error. Message is not sent. Try again later"
                messages.warning(request, message)
                return HttpResponseRedirect(reverse('contact'))
            else:
                message = "Message sent successfully"
                messages.info(request,message)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
        return render(request, 'forms/contact_form.html', {'form': form})

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
            data['country'] = request.POST.get('country').strip()
            data['city'] = request.POST.get('city').strip()
            data['note'] = request.POST.get('note').strip()
            user = request.POST.get('user').strip()
            if user:
                data['user'] = User.objects.get(pk=user)
            # create and save person object
            person = WantedPerson(**data)
            person.save()

            messages.success(request, 'Add successfully :)')
            return HttpResponseRedirect(reverse('home'))

         
    else:
        form = AddWanPerson()
        return render(request, 'forms/add_form.html', {'form':form, 'admin': ADMIN_EMAIL})

# function of searching in database
def db_search(request):
    data = request.GET['mainsearch'].strip()
    if data:
        search_result = util_main_searc(data)
        if not search_result:
            messages.warning(request, 'No results')
    else:
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'search_result.html', {'search_result': search_result})

# function for delete persons by user_data
def deletePersons(request):
    arr = request.POST.getlist('checkedPer[]')
    names = []
    for item in arr:
        per = WantedPerson.objects.get(pk=item)
        if per.last_name:
            names.append(per.first_name + " " + per.last_name)
        else:
            names.append(per.first_name)
        per.delete()
    return JsonResponse({'deletedPersons': names})

# function for edit person through profile
def editPerson(request):
    perIdEdit = request.GET.get('personIdEdit')
    if request.method == "GET":
        obj = WantedPerson.objects.get(pk=perIdEdit)
        serList = {}
        serList['first_name'] = obj.first_name
        serList['last_name'] = obj.last_name
        serList['phone'] = obj.phone
        serList['email'] = obj.email
        serList['country'] = obj.country
        serList['city'] = obj.city
        serList['note'] = obj.note
        serList['birthday'] = obj.birthday
        return JsonResponse({'key':serList},safe = False)

    if request.method == "POST":
        obj = WantedPerson.objects.get(pk=request.POST.get('perId','').strip())
        obj.first_name = request.POST.get('first_name','').strip()
        obj.last_name = request.POST.get('last_name','').strip()
        obj.birthday = request.POST.get('birthday','').strip()
        photo = request.FILES.get('photo')
        if photo:
            obj.photo = request.FILES.get('photo')
        obj.phone = request.POST.get('phone','').strip()
        obj.email = request.POST.get('email','').strip()
        obj.country = request.POST.get('country','').strip()
        obj.city = request.POST.get('city','').strip()
        obj.note = request.POST.get('note','').strip()
        obj.save()
        return HttpResponseRedirect(request.POST.get('currentURL').strip())

def deleteComments(request):
    """pdb.set_trace()"""
    arr = request.POST.getlist('checkedCom[]')
    for item in arr:
        com = Comment.objects.get(pk=item)
        com.delete()
    return JsonResponse({'key': 'success'})

