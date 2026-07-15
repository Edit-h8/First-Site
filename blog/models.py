from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
 # Create your models here.

class category(models.Model):
    name = models.CharField( max_length=220)

    def __str__ (self):
        return self.name
    

class post(models.Model):
    
    # tag
    aother = models.ForeignKey( User , on_delete=models.CASCADE )
    titel = models.CharField(max_length=220)
    contact = models.TextField()
    category = models.ManyToManyField(category)
    counted_viow = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_data = models.DateTimeField( auto_now=False, auto_now_add=False , null= True)
    image = models.ImageField(upload_to='blog/' , default='blog/default.jpg')
    created_data = models.DateTimeField(auto_now_add=True)
    Updated_data = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f"{self.titel}"
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    
    
