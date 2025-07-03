from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000)

class Comment(models.Model):

    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=250)
    article = models.IntegerField() # to which article this comment belongs to