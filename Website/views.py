from django.shortcuts import render
from blog.models import post
from Website.models import Coment
from Website.forms import Coment_form
from django.http import HttpResponse
# Create your views here.


def home(request):
    posts = post.objects.filter(status=1).order_by("-published_data")[:5]
    contactx = {'posts' : posts}
    return render(request, "website/index.html" , contactx)


def contact(request):
    return render(request, "website/contact.html")


def about(request):
    return render(request, "website/about.html")


def test(request):

    if request.method == "POST":
        form = Coment_form(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("done!")
        else :
            HttpResponse("is not Valid !")
        
    form = Coment_form()    

    return render(request, "test.html" , {'form' : form})
