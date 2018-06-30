from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    photo = models.ImageField(
          upload_to = 'img/',
          blank = True,
          verbose_name = "Ptofile photo")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
