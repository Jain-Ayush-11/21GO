from random import randint
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Journal, Post, User, Wallpaper, Relapse
from .serializers import JournalSerializer, PostSerializer, UserSerializer, WallpaperSerializer, RelapseSerializer

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
        wallpaper = []
        for i in range(self.kwargs['pk']+1):
            wallpaper.append(Wallpaper.objects.filter(day=i)[randint(0, Wallpaper.objects.filter(day=i).count()-1)])
        return wallpaper

class RelapseRecord(generics.CreateAPIView):
    serializer_class = RelapseSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data['user'])
        best = (int)(request.data['best'])
        print(best)
        if best is not None:
            if best>user.best:
                user.best=best
        user.attempts += 1
        user.save()
        return super().post(request, *args, **kwargs)

class CalenderStats(generics.ListAPIView):
    serializer_class = RelapseSerializer

    def get_queryset(self):
        return Relapse.objects.filter(user = self.kwargs['pk'])

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class JournalView(generics.ListCreateAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        return Journal.objects.filter(user = self.kwargs['pk'])

class JournalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
