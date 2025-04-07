from django.db import models

# Create your models here.


class userpost(models.Model):
    username = models.CharField(max_length=50, default='None')
    title = models.CharField(max_length=150)
    description = models.TextField()
