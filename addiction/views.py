from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import User, Wallpaper
from .serializers import UserSerializer, WallpaperSerializer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if User.objects.filter(username=request.data['username'], email=request.data['email']).exists():
            return Response(UserSerializer(instance=User.objects.get(username = request.data['username'])).data)
        if User.objects.filter(username=request.data['username']).exists():
            return Response({'message': 'User with the username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=request.data['email']).exists():
            return Response({'message': 'User with the email already exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return super().post(request, *args, **kwargs)

class HomeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WallpaperGet(generics.ListAPIView):
    serializer_class = WallpaperSerializer

    def get_queryset(self):
        return Wallpaper.objects.filter(day__lte = self.kwargs['pk'])
