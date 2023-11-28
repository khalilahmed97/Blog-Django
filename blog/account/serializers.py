from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("EMAIL IS ALREADY TAKEN :(")
        
        password = data['password']
        confirm_password = data['confirm_password']

        if (password != confirm_password):
            raise serializers.ValidationError("PASSWORDS DONT MATCH :(")
        
        return data
    
    def create(self, validated_data):
        

        user = User.objects.create(name = validated_data['name'],
                                   email = validated_data['email'].lower()
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return validated_data
    

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if not User.objects.filter(email = data["email"].lower()).exists():
            raise serializers.ValidationError("INVALID CREDENTIALS :(")
        
        return data
    
    
    def get_jwt_token(self, user):
    
        refresh = RefreshToken.for_user(user)
        
        return {"message": "LOGIN SUCCESSFULL !", "data": {"token": {
        'refresh': str(refresh),
        'access': str(refresh.access_token)}
    }}


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def logout_user(self, data):

        try:
            refresh_token =RefreshToken(data["refreh_token"])
            token = RefreshToken(refresh_token)
            token.blacklist()

            return {"message": "SUCCESSFULL !"}
        
        except Exception as e:
            print(e)
