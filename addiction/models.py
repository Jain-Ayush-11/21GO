from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    best = models.IntegerField(default=0)
    attempts = models.IntegerField(default=1)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username