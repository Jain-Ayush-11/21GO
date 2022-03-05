from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    best = models.IntegerField(default=0)
    attempts = models.IntegerField(default=1)
    time_left = models.BigIntegerField(default=(21*24*60*60*1000))
    end_time = models.BigIntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Wallpaper(models.Model):
    image = models.URLField(max_length=700)
    day = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.day}'