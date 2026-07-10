from django.shortcuts import render , get_object_or_404
from blog.models import post , category
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
# Create your views here.


def home(request , cat_name=None , author_username=None):
    posts = post.objects.filter(status = 1)

    if cat_name:
        posts = posts.filter(category__name=cat_name)
    
    if author_username:
        posts = posts.filter(aother__username = author_username)
    
    posts = Paginator(posts , 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except EmptyPage:
        posts = posts.page(1)
    except PageNotAnInteger :
         posts = posts.page(1)
   
         
    contact = {'posts' : posts , 'category' : category}
    return render(request, "blog/blog-home.html" , contact)



def single(request , pid):
    posts = get_object_or_404(post, pk=pid , status = 1)

    next_post = post.objects.filter(id__gt=pid).order_by('id').first()

    previous_post = post.objects.filter(id__lt=pid).order_by('-id').first()


    context = {'post' : posts, 'next_post' : next_post , 'previous_post':previous_post}
    return render(request, "blog/blog-single.html" , context )



def search(request):
        posts = post.objects.filter(status = 1)
        if request.method == "GET":
            if s := request.GET.get('s'):
                 posts = posts.filter(contact__contains = s)

        contact = {'posts' : posts}
        return render(request , "blog/blog-home.html" , contact)