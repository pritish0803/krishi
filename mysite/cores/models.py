# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,  help_text='Optional.',null=False,default="enter")
    last_name = models.CharField(max_length=30,  help_text='Optional.',null=False,default="enter")
    birth_date = models.DateField(null=True)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.',null=True)
    address = models.CharField(max_length=500, null=False,default="enter")
    pin = models.IntegerField(null=False,default=10)
    aadhar = models.IntegerField(null=False,default=11)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
