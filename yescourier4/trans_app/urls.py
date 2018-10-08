from django.conf.urls import url
from trans_app import views

app_name = 'trans_app'

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', views.TransConfirmView.as_view(),name='trans_confirm'),
	url(r'^pickup/$', views.TransCreateView.as_view(),name='pickup'),
	url(r'^trans_list_search/$', views.TransListViewSearch.as_view(),name='trans_list_search'),
	url(r'^trans_list/$', views.TransListView.as_view(),name='trans_list'),
	url(r'^trans_list1/$', views.TransListView1.as_view(),name='trans_list1'),
	url(r'^print_pdf/$', views.generate_pdf ,name='print_pdf'),



	url(r'^ad/$', views.AdminListView.as_view(),name='ad'),
	url(r'^ad/(?P<pk>\d+)/$', views.AdminDetailView.as_view(),name='ads'),
	

	url(r'^ad/update/(?P<pk>\d+)/$', views.AdminUpdateView.as_view(),name='update'),




]