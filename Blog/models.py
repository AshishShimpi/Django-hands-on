from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
   
    title       = models.CharField(max_length =50 ,blank =False)
    last_edited = models.DateTimeField(auto_now=True)
    Author      = models.CharField(max_length =50 ,blank =True)
    discription = models.TextField(default= 'There is no description', blank=True)

    def get_absolute_url(self):
        return reverse("Blog:article_view",kwargs={"id": self.id})