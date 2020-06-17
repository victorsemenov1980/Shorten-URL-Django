from django.db import models

# Create your models here.

class url(models.Model):
    url=models.URLField()
    custom=models.CharField(max_length=15)