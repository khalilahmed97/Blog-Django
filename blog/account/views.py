from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'SOMETHING WENT WRONG :('
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response( {
                'data':{},
                'message': 'YOUR ACCOUNT IS CREATED'
            }, status= status.HTTP_201_CREATED)


        except Exception as e:
            print(e)
            return Response({
                    'data': {},
                    'message': 'SOMETHING WENT WRONG :('
                }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            user = User.objects.filter(email= data["email"]).first()
            if not user:
                return Response({
                    'data': serializer.errors,
                    'message': 'INVALID CREDENTIALS :('
                }, status=status.HTTP_400_BAD_REQUEST) 
            
            
            if not user.check_password(data["password"]):
                return Response({
                    'data': serializer.errors,
                    'message': 'INVALID PASSWORD :('
                }, status=status.HTTP_400_BAD_REQUEST) 
        
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'SOMETHING WENT WRONG :('
                }, status=status.HTTP_400_BAD_REQUEST) 
        
            response = serializer.get_jwt_token(user)
            return Response(
                response, status= status.HTTP_200_OK)


        except Exception as e:
            print(e)
            return Response({
                    'data': {},
                    'message': 'SOMETHING WENT WRONG :('
                }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request):
        try:
             data = request.data
            
             serializer = LogoutSerializer(data=data)
             if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'SOMETHING WENT WRONG :('
                }, status=status.HTTP_400_BAD_REQUEST) 
        
             response = serializer.logout_user(data=data)
             return Response(
                response, status= status.HTTP_205_RESET_CONTENT)
            
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)