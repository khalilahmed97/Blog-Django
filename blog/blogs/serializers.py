from rest_framework import serializers
from .models import BlogPost, Comment, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogCategory(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def validate(self, blogPostData):
        name = blogPostData['name']
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("CATEGORY IS ALREADY PRESENT :(")
        
        return blogPostData
    
    def create(self, blogPostData):
        name = blogPostData['name']
        category = Category.objects.create(name=name)
        category.save()
        return category
    
    def getAllCategory(self):
        categories = BlogPost.objects.all()
        return list(categories.values())
    

class Post(serializers.Serializer):
    
    author = serializers.CharField()
    title = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=1000)

    def create(self, blogPostData):

        try:
            author_email = blogPostData['author'].lower()
            category = blogPostData['category']
            author = User.objects.get(email=author_email)
        except User.DoesNotExist:
            # Handle the case where the user does not exist, e.g., by raising a validation error
            raise serializers.ValidationError("User with email {} does not exist.".format(author_email))

        
        post = BlogPost.objects.create(author=author, title=blogPostData['title'], body=blogPostData['body'])
        post.categories.add(category)
        post.save()

        return post
    
    def getAllPosts(self):
        posts = BlogPost.object.all()
        return list(posts.values())


class PostComment(serializers.Serializer):
   
    author = serializers.CharField(max_length=100)
    post = serializers.CharField()
    comment = serializers.CharField()

    def create(self, data):
        try:
            comment_author = data['author']
            author = User.objects.get(email=comment_author)
        except User.DoesNotExist:
            # Handle the case where the user does not exist, e.g., by raising a validation error
            raise serializers.ValidationError("User with email {} does not exist.".format(comment_author))

        # post = BlogPost.objects.get(author=comment_author)

        
        title = data['post']
        post = BlogPost.objects.get(title=title)
        if not post:
            raise serializers.ValidationError("Post with title {} does not exist.".format(title))
        
        comment = Comment.objects.create(author=author, post=post, body=data["comment"])
        comment.save()

        return post
    

    def getAllComments(self):
        comments = Comment.objects.all()
        return list(comments.values())