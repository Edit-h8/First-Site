from django.shortcuts import render
from blog.models import post
from Website.models import Coment
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
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print(name +"\n"+ email +"\n"+ subject +"\n"+ message)

        c = Coment()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        

    return render(request, "test.html")
