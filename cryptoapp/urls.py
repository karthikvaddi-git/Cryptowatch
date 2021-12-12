
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('',v.register,name='register'),
    path('logintoweb/',v.logintoweb,name='logintoweb'),
    path('cointrack',v.cointrack,name='cointrack')

    ]