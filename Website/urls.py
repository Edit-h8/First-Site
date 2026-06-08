from django.urls import path
from .views import home, contact, about, element

app_name = "website"

urlpatterns = [
    path("", home, name="index"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("elements", element, name="elements"),
]
