"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from productapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #clear

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/',views.indexpage,name='index'),#register
    path('register/',views.registerpage,name='register'),#register
    path('',views.loginpage,name='login'),#login
    path('home/',views.homepage,name='home'),#register
    path('iit/',views.iitpage,name='iit'),#register
    path('nit/',views.nitpage,name='nit'),#register
    path('deemed/',views.deemedpage,name='deemed'),#register
    path('TamilNadu/',views.TamilNadupage,name='TamilNadu'),#register
    path('Maharashtra/',views.Maharashtrapage,name='Maharashtra'),#register
    path('AP/',views.APpage,name='AP'),#register
    path('',include('productapp.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()#clear

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    