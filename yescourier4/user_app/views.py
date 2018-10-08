# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import urllib
# import urllib2
import requests
from requests import post
import json


from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,View
from django.contrib.auth import authenticate,login
from django.conf import settings

from . import forms

# Create your views here.



class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('user_app/login.html')
	template_name = 'user_app/signup.html'



class LoginView(View):
	def get(self,request):
		template_name = 'user_app/login.html'
		context = {'form':AuthenticationForm(),'error':None}
		if request.user.is_authenticated():
			return redirect('home')
		return render(request,template_name,context)

	def post(self,request):
		f1 = request.POST.get('username')
		f2 = request.POST.get('password')
		user = authenticate(username=f1,password=f2)
		if user:
			if user.is_active:
				recaptcha_response = request.POST.get('g-recaptcha-response')
				# url = 'https://www.google.com/recaptcha/api/siteverify'
				data = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
				}

				r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
				result = r.json()

				# data = urllib.parse.urlencode(values).encode()
				# req = urllib.request.Request(url, data=data)
				# response = urllib.request.urlopen(req)
				# result = json.load(response.read().decode())
				if result['success']:
					login(request,user)
				else:
					print("//"*20,"Invalid reCaptcha")
				return redirect('home')
		template_name = 'user_app/login.html'
		context = {'form':AuthenticationForm(),'error':'Email or password incorrect!!'}
		return render(request,template_name,context)


