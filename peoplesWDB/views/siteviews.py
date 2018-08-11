from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from ..models.wanted_person import WantedPerson
from ..models.comment import Comment
from ..models.profile import Profile
from ..forms.profile import profilePhoto
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import date
import pdb

class CommentSave(TemplateView):
    template_name = "comment.html"

    def post(self, request, *args, **kwargs):
        com = request.POST['comment_val']
        person = WantedPerson.objects.get(pk=request.POST['person_id'])
        user = User.objects.get(pk=request.POST['user_id'])
        today = date.today()
        comment_obj = Comment(comment=com,
                                date=today,
                                  comments=person,
                                    user=user)
        comment_obj.save()
        return JsonResponse({'key': 'success'})


    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(CommentSave, self).get_context_data(**kwargs)

        person = WantedPerson.objects.get(pk = kwargs.get('pk'))
        context['person'] = person
        context['comments_list'] = Comment.objects.filter(comments=person)
        """pdb.set_trace()"""
        return context

def signup_addphoto(request):
    pdb.set_trace()
    return redirect('account_signup')

""" Class for making profile """

class UserProfile(TemplateView):
    template_name = "profile.html"

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(pk = user_id)
        photo = request.FILES.get('photo')
        user_photo = Profile.objects.filter(user = user_id)
        if len(user_photo) > 0:
            obj = Profile.objects.get(user = user_id)
            obj.photo = photo
            obj.save()
        else:
            obj = Profile(photo = photo, user = user)
            obj.save()
        return HttpResponseRedirect(reverse('user_profile', kwargs = {'pk':user_id}))

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        user_id = kwargs.get('pk')
        user = User.objects.get(pk = user_id)
        user_photo = Profile.objects.filter(user = user_id)
        if len(user_photo) > 0:
            context['user_photo'] = user_photo[0].photo

        context['user'] = user
        context['persons'] = WantedPerson.objects.filter(user = user_id)
        context['comments'] = Comment.objects.filter(user = user_id)
        context['profileForm'] = profilePhoto()

        return context
