from django.shortcuts import render
from blog.models import post
from Website.forms import Coment_form
from django import http
from django.contrib import messages
# Create your views here.


def home(request):
    posts = post.objects.filter(status=1).order_by("-published_data")[:5]
    contactx = {'posts' : posts}
    return render(request, "website/index.html" , contactx)


def contact(request):
    if request.method == "POST":
        form = Coment_form(request.POST)
        
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , "your message Accept successfuly!")
        
        else : 
            messages.add_message(request , messages.ERROR , "your message Do Not Accept !")
    
    form = Coment_form()
    return render(request, "website/contact.html" , {'form' : form})


def about(request):
    return render(request, "website/about.html")


def test(request):

    if request.method == "POST":
        form = Coment_form(request.POST)

        if form.is_valid():
            form.save()
            return http.HttpResponse("done!")
        else :
            http.HttpResponse("is not Valid !")
        
    form = Coment_form()    

    return render(request, "test.html" , {'form' : form})
