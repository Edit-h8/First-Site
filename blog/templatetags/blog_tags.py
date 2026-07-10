from django import template
from blog.models import post
from blog.models import category
register = template.Library()

@register.simple_tag(name="cou_post")
def counter_post():
    posts = post.objects.all().filter(status=1).count()
    return posts


@register.inclusion_tag('blog/blog-popular-posts.html')
def lastes_post():
    posts = post.objects.filter(status = 1).order_by("-published_data")[:3]
    return {'posts' : posts}


@register.inclusion_tag('blog/blog-category-post.html')
def category_post():
    posts = post.objects.filter(status = 1)
    categories = category.objects.all()
    cat_dicshe = {}
    for name in categories:
        cat_dicshe[name]= posts.filter(category = name).count()
    return {"categories" : cat_dicshe}
