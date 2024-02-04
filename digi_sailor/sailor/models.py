from django.db import models

# Create your models here.
class AdminUser(models.Model):
    profile_pic = models.FileField(default="")