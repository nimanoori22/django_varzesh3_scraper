from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class MyNewsFb(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    lead = models.CharField(max_length=250)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
    
    class Admin:
        pass