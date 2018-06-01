from django.db import models


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

        blank = True,
        verbose_name = "Photo")

    birthday = models.DateField(
        blank = True,
        verbose_name = "Birthday")

    phone = models.CharField(
        max_length = 30,
        blank = True,
        verbose_name = "Phone")

    email = models.EmailField(
        blank = True,
        verbose_name = "Email")

    note = models.TextField(
        blank = True,
        verbose_name = "Note")

def __unicode__(self):
    return '%s' % (self.first_name)
