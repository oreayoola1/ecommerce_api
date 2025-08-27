from django.urls import path
from .views import RegisterUser, LoginUser
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('token/', obtain_auth_token, name='api_token_auth'),
]