from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class AdminUser(models.Model):
    profile_pic = models.FileField(default="")

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse('sailor-detail', kwargs={'pk': self.pk})
    