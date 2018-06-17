from django.db import models

class Comment(models.Model):

    comment = models.TextField(
        blank = False,
        verbose_name = "comment")

    date = models.DateField(
        blank = False,
        verbose_name = "comment_date")

    comments = models.ForeignKey('WantedPerson', 
        on_delete=models.CASCADE)
