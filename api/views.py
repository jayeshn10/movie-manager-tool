
import io
import random
import string
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api.serializers import MovieSerializer, RegisterUserSerializer
from rest_framework.decorators import api_view

from core.models import Movie
from moviepy.editor import *


# Create your views here.
class RegisterUserAPI(APIView):
    def post(self, request):
        serializers = RegisterUserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginUserAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                    'token': token.key
                })
        else:
            return Response({
                "error":"username or password is incorrect"
            },status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ApiHome(request):
    data = {
            'hello/': 'api List',
            'api/': 'api List',
            'api/login': 'Login user',
            'api/register': 'Register user',
            'api/movie': 'List all movies Method=GET, create Method=POST',
            'api/movie/<id>': 'view single movie Method=GET, update Method=PUT, delete Method=DELETE',
            'api/video': 'video generation Method=POST',
        }
    return Response(data)

class MovieAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):
        if id:
            if Movie.objects.filter(id=id).exists():
                movie = Movie.objects.get(id=id)
                data  = {} 
                data["id"] = movie.id
                data["title"] = movie.title
                data["release_date"] = movie.release_date
                data["movie_type"] = {"value": movie.movie_type, "text": movie.get_movie_type_display()}
                data["director"] = movie.director
                data["producer"] = movie.producer
                data["writer"] = movie.writer
                data["rating"] ={"value": movie.rating, "text": movie.get_rating_display()}
                return Response(data)
            else:
                return Response({"message":"Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            movies = Movie.objects.all()
            data_list = []
            for movie in movies:
                data  = {} 
                data["id"] = movie.id
                data["title"] = movie.title
                data["type"] = {"value": movie.type, "text": movie.get_type_display()}
                data["director"] = movie.director
                data["producer"] = movie.producer
                data["writer"] = movie.writer
                data["rating"] ={"value": movie.rating, "text": movie.get_rating_display()}
                data_list.append(data)
            return Response(data_list)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            movie = Movie.objects.create(**data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        if Movie.objects.filter(id=id).exists():
            movie = Movie.objects.get(id=id)
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                movie.title = data["title"]
                movie.type = data["type"]
                movie.director = data["director"]
                movie.producer = data["producer"]
                movie.writer = data["writer"]
                movie.rating = data["rating"]
                movie.save()
                return Response(data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if Movie.objects.filter(id=id).exists():
            movie = Movie.objects.get(id=id)
            movie.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message":"Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def VideoAPI(request):
    video_file = request.data.get("video")
    temp_video_path = os.path.join(settings.MEDIA_ROOT, 'temp', 'uploaded_video_{}.mp4'.format(''.join(random.choices(string.ascii_lowercase, k=5))))
        
    with open(temp_video_path, 'wb') as temp_video_file:
        temp_video_file.write(video_file.read())

    video = VideoFileClip(temp_video_path)
    txt_clip = ( TextClip("Jayesh Nandgaonkar",fontsize=40,color='white').set_position('center').set_duration(10) )
    result = CompositeVideoClip([video, txt_clip])
    
    output_video_path = os.path.join(settings.MEDIA_ROOT, 'temp', 'output_{}.mp4'.format(''.join(random.choices(string.ascii_lowercase, k=5))))

    result.write_videofile(output_video_path, fps=25, codec='libx264')

    with open(output_video_path, 'rb') as output_file:
        output_video_io = io.BytesIO(output_file.read())

    response = HttpResponse(output_video_io.getvalue(), content_type='video/mp4')
    response['Content-Disposition'] = 'inline; filename=output.mp4'
    os.remove(temp_video_path)
    os.remove(output_video_path)
    return response