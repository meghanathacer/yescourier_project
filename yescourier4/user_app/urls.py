from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import password_reset


app_name='user_app'

urlpatterns = [
	url(r'^login/$',views.LoginView.as_view(),name='login'),

	url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    
    url(r'^signup/$',views.SignUp.as_view(), name='signup'),
    
    url(r'^reset_password/$', password_reset, name='reset_password'),

    

]