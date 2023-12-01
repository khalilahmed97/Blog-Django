from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .serializers import Post, PostComment, BlogCategory


class Category(APIView):
    def get(self, request, id=None):
        serializer = BlogCategory()
        if request.method == "GET" and id is None:
            category = serializer.getAllCategory()
            return JsonResponse( {
                    'category' : category
                }, status= status.HTTP_200_OK)
        
        if request.method == "GET" and id is not None:
            category = serializer.getCategory(pk=id)
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

@permission_classes([IsAuthenticated])
class BlogPost(APIView):
    def get(self, request, id=None):
        serializer = Post()
        if request.method == "GET" and id is None:
            posts = serializer.getAllPosts()
            return JsonResponse( {
                    'posts' : posts
                }, status= status.HTTP_200_OK)
        
        if request.method == "GET" and id is not None:
            post = serializer.getPost(pk=id)
            return JsonResponse( {
                    'posts' : post
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

@permission_classes([IsAuthenticated])
class Comment(APIView):
    def get(self, request, id=None):
        serializer = PostComment()

        if request.method == "GET" and id is None:
            comments = serializer.getAllComments()
            return JsonResponse( {
                    'comments' : comments
                }, status= status.HTTP_200_OK)
        

        if request.method == "GET" and id is not None:    
            comments = serializer.getCommentsofSpecificAuthor(pk=id)
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




