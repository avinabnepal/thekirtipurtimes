from django.db import models

from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.TextField(choices=[('N', 'None'), ('M', 'Male'), ('F', 'Female')], default='N')

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    time_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
