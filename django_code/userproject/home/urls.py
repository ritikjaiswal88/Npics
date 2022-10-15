from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('u',views.index, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]