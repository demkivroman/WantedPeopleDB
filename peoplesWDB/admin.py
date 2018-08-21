# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.wanted_person import WantedPerson
from .models.comment import Comment
from .models.profile import Profile

class WantedPersonAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    list_display_links = ['first_name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','get_firstName']
    
    def get_firstName(self,obj):
        return obj.comments.first_name
    

# Register your models here.

admin.site.register(WantedPerson, WantedPersonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)
