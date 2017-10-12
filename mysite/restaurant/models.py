# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name=models.CharField(max_length=120)
	location=models.CharField(max_length=120,null=True,blank=False)
	catagory=models.CharField(max_length=120,null=True,blank=False)
	date=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
