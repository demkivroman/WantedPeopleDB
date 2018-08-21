from django.db import models
from ..models import WantedPerson
from django.contrib.auth.models import User

class Comment(models.Model):

    comment = models.TextField(
        blank = False,
        verbose_name = "comment")

    date = models.DateField(
        blank = False,
        verbose_name = "comment_date")

    comments = models.ForeignKey(WantedPerson,
        null = True, 
        on_delete=models.CASCADE)

    user = models.ForeignKey(User,
        null = True,
        on_delete = models.CASCADE)
