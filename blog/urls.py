from django.contrib import admin
from django.urls import path
from .views import *


app_name = "blog"

urlpatterns = [
    path("", home, name="index"),
    path("<int:pid>", single, name="single"),
    path("post-<int:pid>", test , name='test'),
]
