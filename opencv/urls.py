from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.test),
]
