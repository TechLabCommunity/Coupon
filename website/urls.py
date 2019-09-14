from django.contrib import admin
from django.urls import path
from website.views import register, guarda_coupon
urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', guarda_coupon, name='verify')
]