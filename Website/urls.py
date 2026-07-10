from django.urls import path
from .views import home, contact, about, test

app_name = "website"

urlpatterns = [
    path("", home, name="index"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("test" , test , name="test")
]
