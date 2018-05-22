"""MemeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from Main_Meme.views import *

urlpatterns = [
    url(r'^upload/$',uploadMeme,name='upload'),
    url(r'^profile/$',TemplateView.as_view(template_name="Profile.html"),name="profile"),
    url(r'^meme/(?P<meme_id>\d+)/$', memedetails,name="meme"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('memecreator/',TemplateView.as_view(template_name="memecreator.html"),name="memecreator"),
    path('', home, name="home")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
