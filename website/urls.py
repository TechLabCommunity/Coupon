from django.contrib import admin
from django.urls import path
from website.views import register
urlpatterns = [
    path('register/', register, name='register')
]