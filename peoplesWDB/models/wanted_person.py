from django.db import models
from django.contrib.auth.models import User


class WantedPerson(models.Model):

    first_name = models.CharField(
        max_length = 50,
        blank = False,
        verbose_name = "FirstName")

    last_name = models.CharField(
        max_length = 50,
        blank = True,
        verbose_name = "LastName")

    photo = models.ImageField(
        upload_to = 'img/',
        blank = False,
        verbose_name = "Photo")

    birthday = models.DateField(
        blank = True,
        null = True,
        verbose_name = "Birthday")

    phone = models.CharField(
        max_length = 30,
        blank = True,
        verbose_name = "Phone")

    email = models.EmailField(
        blank = True,
        verbose_name = "Email")

    country = models.CharField(
        max_length = 50,
        blank = True,
        verbose_name = "Country")

    city = models.CharField(
        max_length = 50,
        blank = True,
        verbose_name = "city")

    note = models.TextField(
        blank = True,
        verbose_name = "Note")

    user = models.ForeignKey(User,
        blank = True,
        null = True,
        on_delete=models.CASCADE)

def __unicode__(self):
    return '%s' % (self.first_name)
