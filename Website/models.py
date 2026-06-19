from django.db import models

# Create your models here.

class Coment(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length = 254 ,null=True)
    message = models.TextField()
    created_time = models.TimeField(auto_now_add=True)
    Update_time = models.TimeField(auto_now=True)
    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return self.name
