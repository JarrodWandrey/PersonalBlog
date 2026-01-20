from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserLike(models.Model):
    post = models.ForeignKey(Post, related_name='user_likes', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    liked_at = models.DateTimeField(auto_now_add=True)