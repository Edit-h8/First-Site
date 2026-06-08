from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "website/index.html")


def contact(request):
    return render(request, "website/contact.html")


def about(request):
    return render(request, "website/about.html")


def element(request):
    return render(request, "website/elements.html")
