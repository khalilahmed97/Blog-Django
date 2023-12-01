from django.urls import path
from .views import BlogPost,Comment,Category
urlpatterns = [
    # POST REQUEST
    path('post/new/', BlogPost.as_view()),
    path('category/new', Category.as_view()),
    path('post/comment/', Comment.as_view()),
    
    # GET REQUEST
    path('post/all/', BlogPost.as_view()),
    path('category/all/', Category.as_view()),
    path('post/comment/all/', Comment.as_view()),


    path('post/<str:id>/', BlogPost.as_view()),
    path('category/<str:id>/', Category.as_view()),

    # COMMENTS (AUTHOR AND POST)
    path('author/comment/<str:id>/', Comment.as_view()),
]
