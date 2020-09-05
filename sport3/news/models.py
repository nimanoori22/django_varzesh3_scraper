from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from datetime import datetime
# Create your models here.

class MyNewsFb(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    lead = models.CharField(max_length=250)
    content = RichTextField()
    mydate = models.DateField(null=True, blank=True)
    mytime = models.TimeField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='news_pics')

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-mydate', '-mytime']