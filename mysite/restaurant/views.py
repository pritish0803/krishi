# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.db.models import Q
from django.shortcuts import render
from .models import Restaurant
from django.views.generic import TemplateView,ListView

class contentview(TemplateView):
	
	template_name="restaurant/content.html"
class homeview(ListView):
	
	#template_name="restaurant/restaurant_view.html"
	queryset=Restaurant.objects.all()
	
class aboutview(TemplateView):
	
	template_name="restaurant/about.html"
class restaurant_view(ListView):
	#template_name="restaurant.html"
	def get_queryset(self):
		slug=self.kwargs.get("slug")
		if slug:
			queryset=Restaurant.objects.filter(
				Q(catagory__iexact=slug)|
				Q(catagory__icontains=slug)
		)
		else:
			queryset=Restaurant.objects.all()
		return queryset

