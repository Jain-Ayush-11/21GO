from rest_framework.response import Response
from rest_framework import generics
from . import serializers
from .models import User, Wallpaper
from .serializers import UserSerializer, WallpaperSerializer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if User.objects.filter(username=request.data['username']).exists():
            return Response(UserSerializer(instance=User.objects.get(username = request.data['username'])).data)
        return super().post(request, *args, **kwargs)

class HomeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class WallpaperGet(generics.ListAPIView):
    serializer_class = WallpaperSerializer

    def get_queryset(self):
        return Wallpaper.objects.filter(day__lte = self.kwargs['pk'])
