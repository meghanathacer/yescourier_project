"""yescouriers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
#from django.conf import settings
#rom django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(),name='home'),
    url(r'^about/', views.AboutPage.as_view(),name='about'),
    url(r'^contact/', views.ContactPage.as_view(),name='contact'),
    url(r'user_app/', include('user_app.urls', namespace='user_app')),
    url(r'trans_app/', include('trans_app.urls', namespace='trans_app')),
    url(r'user_app/',include('django.contrib.auth.urls')),
    url(r'^thanks/$', views.ThanksPage.as_view(),name='thanks'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

]

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
