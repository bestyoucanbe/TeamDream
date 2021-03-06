"""teamdream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from teamdreamapp.models import *
from teamdreamapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # The following url is set-up to help in logging the user in--look at templates/registration/login.html file
    url(r'accounts/', include('django.contrib.auth.urls')),
    # The following url is set up to help logout the user--look at the views/auth/logout.py file
    url(r'^logout/$', logout_user, name='logout'),
    # The following url is set up to look-up all the urls listed in urls.py file of the teamdreamapp
    url(r'^', include('teamdreamapp.urls')),
]
