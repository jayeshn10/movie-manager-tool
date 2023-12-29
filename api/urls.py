from django.urls import path

from api.views import *

urlpatterns = [
    path('', ApiHome, name='api-home'),
    path('login/', LoginUserAPI.as_view(), name='login-api'),
    path('register/', RegisterUserAPI.as_view(), name='register-api'),
    path('movie/', MovieAPI.as_view(), name='movie'),
    path('movie/<int:id>', MovieAPI.as_view(), name='movie-details'),
    path('video/', VideoAPI, name='video-api')
]