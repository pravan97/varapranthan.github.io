"""xyz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from newapp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name="home"),
    path('view/', view, name="view"),
    path('add/', index, name="add"),
    path('', main, name="main"),
    # path('', loggin, name="login"),
    path('signup/', signup, name="signup"),
    url(r'^delete/(\d+)/$', delete, name='delete'),
    path('works/', works, name="works"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    # url(r'^works/(\d+)/$', works, name='works'),
    url(r'^edit/(\d+)/$', edit, name='edit'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),


]
