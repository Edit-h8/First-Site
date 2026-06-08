from django.contrib import admin
from django.urls import path
from .views import home, single

app_name = "blog"

urlpatterns = [
    path("", home, name="index"),
    path("single", single, name="single"),
]
