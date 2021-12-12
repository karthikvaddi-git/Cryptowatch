
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('register',v.register,name='register'),
    path('',v.home,name='home'),
    path('logintoweb/',v.logintoweb,name='logintoweb'),
    path('cointrack',v.cointrack,name='cointrack'),
    path('logoutweb',v.logoutfun,name='logoutfun'),
#    path('whatsappbot',v.whatsappbot,name='whatsappbot')

    ]

