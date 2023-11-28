from django.urls import path
from .views import BlogPostView, BlogPostCommentView, BlogPostCategory
urlpatterns = [
    # POST REQUEST
    path('post/new/', BlogPostView.as_view()),
    path('category/new', BlogPostCategory.as_view()),
    path('post/comment/', BlogPostCommentView.as_view()),
    
    # GET REQUEST
    path('post/all/', BlogPostView.as_view()),
    path('category/all/', BlogPostCategory.as_view()),
    path('post/comment/all/', BlogPostCommentView.as_view()),

]
