from django.contrib import admin
from blog.models import post , category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(post)
class postAdmin(SummernoteModelAdmin):
    list_display = ['titel','aother','counted_viow','status' , 'created_data' , 'published_data']
    search_fields = ['titel' , 'contact']
    list_filter = ['status' , 'aother']
    empty_value_display = '-empty-'
    summernote_fields = ('contact',)
admin.site.register(category)
