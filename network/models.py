from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.ManyToManyField(User, related_name = 'likes')

class Follower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'followee')
    followers = models.ManyToManyField(User, related_name = 'followers', blank=True)
    following = models.ManyToManyField(User, related_name = 'following', blank=True)
    