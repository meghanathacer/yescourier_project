# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import CreateView,DetailView,ListView,TemplateView,UpdateView

from . import models
from .forms import SampleForm

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

from django.core.urlresolvers import reverse_lazy
# Create your views here.

class TransListView1(TemplateView):
	template_name = 'trans_app/trans_list1.html'


class TransCreateView(CreateView):
	form_class=SampleForm
	model = models.Consignment
	template_name = 'trans_app/consignment_form.html'

	def post(self,request):
		x = super(TransCreateView,self).post(self,request)
		self.object.customer_id = request.user
		self.object.save()	
		return x


class TransConfirmView(DetailView):
    context_object_name = 'consignment_details'
    model = models.Consignment
    template_name = 'trans_app/consignment_detail.html'

class TransListView(ListView):
	template_name = 'trans_app/consignment_list.html'
	model = models.Consignment
	context_object_name = "object"

	def get_queryset(self):
		x = super(TransListView,self).get_queryset()
		print(x)
		print(self.request.user.username)

		x = x.filter(customer_id=self.request.user)
		print(x)
		return x

class TransListViewSearch(ListView):
	template_name = 'trans_app/consignment_list.html'
	model = models.Consignment
	context_object_name = "object"

	def get_queryset(self):
		x = super(TransListViewSearch,self).get_queryset()
		print(x)
		print(self.request.user.username)

		x = x.filter(consignment_id=self.request.GET.get('search'))
		print(x)
		return x

def generate_pdf(request):
    
    html_string = render_to_string('trans_app/consignment_detail.html',)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    return response



class AdminListView(ListView):
	context_object_name = 'consignments'
	model = models.Consignment
	template_name = 'trans_app/admin_list.html'

class AdminDetailView(DetailView):
	context_object_name = 'consignment_detail'
	model = models.Consignment
	template_name = 'trans_app/admin_details.html'

class AdminUpdateView(UpdateView):
	fields = ('status_n',)
	model = models.Consignment
	template_name = 'trans_app/admin_update.html'
	success_url = reverse_lazy('trans_app:ad')
