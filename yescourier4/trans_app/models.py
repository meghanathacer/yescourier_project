# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Consignment(models.Model):

	from_c = models.CharField('From', max_length=256)
	where_c = models.CharField('To',max_length=256)
	weight_c = models.IntegerField('Weight')
	price_c = models.IntegerField('Price')
	address_hname = models.CharField('Home Address',max_length=256)
	address_sname = models.CharField('Street',max_length=256)
	address_dname = models.CharField('District',max_length=256)
	address_brname = models.CharField('Near Branch',max_length=256)
	consignment_id = models.CharField(max_length=256)
	customer_id = models.ForeignKey(User,null=True,blank=True,default=None)
	status_n= models.BooleanField('Status',default=False)
	date_n = models.DateTimeField(auto_now_add=True)



	def __str__(self):
		return self.consignment_id


	def get_absolute_url(self):
		return reverse("trans_app:trans_confirm",kwargs={'pk':self.pk})
