from django.shortcuts import render
from django.views.generic.base import TemplateView
from ..models.wanted_person import WantedPerson
from ..models.comment import Comment
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
