from .models import User, Wallpaper
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WallpaperSerializer(ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = '__all__'