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

#class Info(models.Model):
	#user_name=models.ForeignKey(Profile,on_delete=models.CASCADE)
	



class Crop(models.Model):
	crop_name=models.CharField(max_length=30)
	catagory=models.CharField(max_length=30,help_text='Kharif or Rabi')
	crop_price_cur=models.IntegerField()
	crop_price_prev=models.IntegerField(help_text='1 year ago per kg')
	crop_price_prev2=models.IntegerField(help_text='2 year ago per kg',default=100)
	crop_price_prev3=models.IntegerField(help_text='3 year ago per kg',default=100)
	
	def __unicode__(self):
		return self.crop_name
class Warehouse(models.Model):
	warehouse_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity=models.IntegerField()
	price=models.IntegerField(help_text='monthly price')
	warehouse_pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.warehouse_name

class Market(models.Model):
	market_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity=models.IntegerField()
	market_pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.market_name
class Transportation(models.Model):
	transport_company_name=models.CharField(max_length=30)
	location=models.CharField(max_length=30)
	capacity_per_person=models.IntegerField(help_text='per person capacity')
	trip_price_per_km=models.IntegerField(help_text='per km')
	pincode=models.IntegerField(default=751020)
	def __unicode__(self):
		return self.transport_company_name
class market_crop_price(models.Model):
	market_id=models.ForeignKey(Market,on_delete=models.CASCADE)
	crop_id=models.ForeignKey(Crop,on_delete=models.CASCADE)
	price_per_kg=models.IntegerField()
	price_per_kg_prev1=models.IntegerField(help_text='1 year ago')
	price_per_kg_prev2=models.IntegerField(help_text='2 year ago')
	price_per_kg_prev3=models.IntegerField(help_text='3 year ago')

	def __unicode__(self):
		return self.price_per_kg
