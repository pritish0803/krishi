# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from cores.forms import SignUpForm

@login_required
def home(request):
	return render(request, 'home.html')

def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			if form.is_valid():
				user=form.save()
				user.refresh_from_db()  
            			user.profile.birth_date=form.cleaned_data.get('birth_date')
            			user.save()
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=user.username, password=raw_password)
				login(request, user)
				return redirect('home')
	else:
        	form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def Crops_view(request):
    if request.method=='GET':
        if request.GET.get('crop'):
			crop=request.GET.get('crop')
			all_crop=Crop.objects.get(crop_name=crop)
