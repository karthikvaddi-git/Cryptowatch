
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('',v.register,name='register'),
 #   path('bot',include("whatsappbot.urls"))

    ]