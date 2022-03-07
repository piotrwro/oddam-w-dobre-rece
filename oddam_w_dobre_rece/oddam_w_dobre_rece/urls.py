"""oddam_w_dobre_rece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from home.views import Index, Form, FormConf, Login, Register, Userprofile



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('form/', Form.as_view(), name='form'),
    path('formconf/', FormConf.as_view(), name='form-confirmation'),
    path('login/', Login.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view( template_name='index.html'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('userprofile', Userprofile.as_view(), name='userprofile')

]
