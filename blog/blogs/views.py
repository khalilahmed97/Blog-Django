from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

from .serializers import Post, PostComment, BlogCategory


class BlogPostCategory(APIView):
    def get(self, request):
        if request.method == "GET":
            serializer = BlogCategory()
            category = serializer.getAllCategory()
            return JsonResponse( {
                    'category' : category
                }, status= status.HTTP_200_OK)

    def post(self, request):
        if request.method == "POST":
            try:
                data = request.data
                serializer = BlogCategory(data=data)

                if not serializer.is_valid():
                    return Response({
                        'data': serializer.errors,
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)
            
                serializer.save()
                return Response( {
                    'data':{},
                    'message': 'YOUR BLOG POST CATEGORY IS CREATED'
                }, status= status.HTTP_201_CREATED)


            except Exception as e:
                return Response({
                        'data': {},
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)

        
class BlogPostView(APIView):
    def get(self, request):
        if request.method == "GET":
            serializer = Post()
            posts = serializer.getAllPosts()
            return JsonResponse( {
                    'posts' : posts
                }, status= status.HTTP_200_OK)

    
    def post(self, request):
        if request.method == "POST":
            try:
                data = request.data
                serializer = BlogPost(data= data)

                if not serializer.is_valid():
                    return Response({
                        'data': serializer.errors,
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                serializer.save()
                return Response( {
                    'data':{},
                    'message': 'YOUR BLOG POST IS CREATED'
                }, status= status.HTTP_201_CREATED)

            except Exception as e:
                return Response({
                        'data': {},
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)


class BlogPostCommentView(APIView):
    def get(self, request):
        if request.method == "GET":
            serializer = PostComment()
            comments = serializer.getAllComments()
            return JsonResponse( {
                    'comments' : comments
                }, status= status.HTTP_200_OK)

    def post(self, request):
        if request.method == "POST":
            try:
                data = request.data
                serializer = PostComment(data= data)

                if not serializer.is_valid():
                    return Response({
                        'data': serializer.errors,
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                serializer.save()
                return Response( {
                    'data':{},
                    'message': 'YOUR COMMENT IS ADDED TO THE POST'
                }, status= status.HTTP_201_CREATED)


            except Exception as e:
                return Response({
                        'data': {},
                        'message': 'SOMETHING WENT WRONG :('
                    }, status=status.HTTP_400_BAD_REQUEST)




