from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
from .models import Consignment

import hashlib


def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(10, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()[:10]

class SampleForm(forms.ModelForm):
	class Meta:
		model=Consignment
		exclude=['consignment_id','customer_id','status_n']
	def save(self, commit=True):
		cons = super(SampleForm, self).save(commit=False)
		# user.is_active=False]
		
		if commit:
			
			cryptstr = generate_activation_key("jnyhbtgvrf")
			cons.consignment_id=cryptstr
			cons.save()
			
		return cons

