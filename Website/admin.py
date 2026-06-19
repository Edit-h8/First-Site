from django.contrib import admin
from Website.models import Coment

# Register your models here.

@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'created_time']
    list_filter = ['email']
    search_fields = ['name' , 'message']