from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User ,on_delete=models.CASCADE)
    details = models.TextField()
    profile_picture = models.FileField()

    def __str__(self):
        return self.name.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    article_author = models.ForeignKey(Author , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category , on_delete= models.CASCADE)
    posted_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    image = models.FileField()

    def __str__(self):
        return self.title
