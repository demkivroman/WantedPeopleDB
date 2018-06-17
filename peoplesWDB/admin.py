# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.wanted_person import WantedPerson
from .models.comment import Comment

# Register your models here.

admin.site.register(WantedPerson)
admin.site.register(Comment)
