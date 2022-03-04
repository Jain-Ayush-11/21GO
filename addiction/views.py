from rest_framework import generics
from . import serializers
from .models import User, Wallpaper

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class HomeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class WallpaperGet(generics.ListAPIView):
    serializer_class = serializers.WallpaperSerializer

    def get_queryset(self):
        return Wallpaper.objects.filter(day__lte = self.kwargs['pk'])
