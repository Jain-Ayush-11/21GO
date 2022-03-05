from .models import Journal, Post, User, Wallpaper, Relapse
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WallpaperSerializer(ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = '__all__'

class RelapseSerializer(ModelSerializer):
    class Meta:
        model = Relapse
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        date = str(response.pop('date'))
        response['date'] = date[8]+date[9]
        response['month'] = date[5]+date[6]
        response['year'] = date[0]+date[1]+date[2]+date[3]
        response.pop('user')
        return response

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user']=instance.user.username
        return response

class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        date = str(response.pop('time_created'))
        response['date'] = date[8]+date[9]
        response['month'] = date[5]+date[6]
        response['year'] = date[0]+date[1]+date[2]+date[3]
        response.pop('user')
        return response
