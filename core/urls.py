from django.urls import path

from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie/', movie, name='movie'),
    path('hello/', Hello, name='hello'),
    path('login/', loginuser, name='login'),
    path('register/', registeruser, name='register'),
    path('video/', video, name='video')
]