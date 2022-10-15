from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("s1", views.s1, name='s1'),
    path("s2", views.s2, name='s2'),
]