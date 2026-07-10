from django.contrib import admin
from django.urls import path
from .views import *


app_name = "blog"

urlpatterns = [
    path("", home, name="index"),
    path("<int:pid>", single, name="single"),
    path("category/<str:cat_name>", home , name="category"),
    path("author/<str:author_username>", home , name="author"),
    path("search" , search , name="search"),
]
