from django.contrib import admin
from blog.models import post , category

# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ['titel','aother','counted_viow','status' , 'created_data' , 'published_data']
    search_fields = ['titel' , 'contact']
    list_filter = ['status' , 'aother']
    empty_value_display = '-empty-'

admin.site.register(category)
