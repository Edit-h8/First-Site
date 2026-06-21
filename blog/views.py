from django.shortcuts import render , get_object_or_404
from blog.models import post
# Create your views here.


def home(request):
    posts = post.objects.filter(status = 1)
    contact = {'posts' : posts}
    return render(request, "blog/blog-home.html" , contact)

def single(request , pid):
    posts = get_object_or_404(post, pk=pid)
    context = {'post' : posts}
    return render(request, "blog/blog-single.html" , context)

def test(request , pid):
    Get_element = get_object_or_404(post,pk=pid)
    context = {'elment' : Get_element}
    return render(request, "test.html" , context)
