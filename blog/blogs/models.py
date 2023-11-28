from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
    
    def __str__(self):
        return self.name
    
class BlogPost (models.Model):

    class Meta:
        verbose_name = ("Blog Post")
        ordering = ("-created_at",)

    post_id = models.AutoField(null=False, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    categories = models.ManyToManyField(Category, related_name="posts_list", blank=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.email



class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, 
        related_name="post_comments",
        null=True,
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.author.email