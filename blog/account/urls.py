from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('token/generate', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
