from django.db import models

# Create your models here.


class post(models.Model):
    #auther
    titel = models.CharField(max_length=220)
    contact = models.TextField()
    # tag
    # category

    counted_viow = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_data = models.TimeField(null=True)
    created_data = models.TimeField(auto_now_add=True)
    Updated_data = models.TimeField(auto_now=True)    

    def __str__(self):
        return f"{self.titel}"
    
