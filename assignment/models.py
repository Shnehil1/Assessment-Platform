from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
import datetime


class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document)


class Assignment(models.Model):
    name= models.CharField(max_length=250)
    technology= models.CharField(max_length=100)
    directory= models.CharField(max_length=500, default="NA")

    def __str__(self):
        return self.name + '-' + self.technology


class Assestment(models.Model):
    name= models.CharField(max_length=250)
    technology= models.CharField(max_length=100)
    username= models.CharField(max_length=100, default="NA")
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)


    def __str__(self):
        return self.name + '-' + self.technology

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=100)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)