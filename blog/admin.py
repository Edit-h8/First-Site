from django.contrib import admin
from blog.models import post

# Register your models here.

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ['titel','counted_viow','status' , 'created_data' , 'published_data']
    search_fields = ['titel' , 'contact']
    list_filter = ['status']
    empty_valu_display = '-empty-'